from pathlib import Path
import shutil
import tempfile
import click
from sphinx.application import Sphinx
from io import StringIO
import sys

@click.group()
def cli():
    """CLI for building documentation."""
    pass

def build_docs(source_dir, build_dir, buildername, paths=None):
    """Helper function to build documentation using Sphinx."""
    source_dir = Path(source_dir)
    build_dir = Path(build_dir)

    if not source_dir.exists():
        click.echo(f"Error: The source directory '{source_dir}' does not exist.")
        return {"status": "error", "warnings": 0}

    # Create a temporary staging directory
    with tempfile.TemporaryDirectory() as staging_dir:
        staging_dir = Path(staging_dir)
        # Copy the source directory to the staging directory
        shutil.copytree(source_dir, staging_dir, dirs_exist_ok=True)

        # Copy specified paths to the root of the temporary directory
        if paths:
            for target_path, dest_path in paths.items():
                target_path = Path(target_path)
                full_dest_path = staging_dir / dest_path

                if target_path.exists():
                    merge_folders(target_path, full_dest_path)
                else:
                    click.echo(f"Warning: Path '{target_path}' does not exist and will not be copied.")

        # Set the configuration and doctree directories
        conf_dir = staging_dir
        doctree_dir = build_dir / '.doctrees'

        build_dir.mkdir(parents=True, exist_ok=True)

        # Capture the output
        output = StringIO()
        sys.stdout = output

        try:
            app = Sphinx(
                srcdir=str(staging_dir),
                confdir=str(conf_dir),
                outdir=str(build_dir),
                doctreedir=str(doctree_dir),
                buildername=buildername
            )
            app.build()

            # Restore stdout
            sys.stdout = sys.__stdout__

            # Analyze the output for warnings
            build_output = output.getvalue()
            warning_count = build_output.lower().count('warning')

            click.echo(f"{buildername.upper()} documentation has been built successfully with {warning_count} warnings.")
            return {"status": "success", "warnings": warning_count}

        except Exception as e:
            # Restore stdout
            sys.stdout = sys.__stdout__

            # Handle the error by copying the staging directory to an error_staging folder
            error_staging_dir = build_dir / 'error_staging'
            error_staging_dir.mkdir(parents=True, exist_ok=True)
            shutil.copytree(staging_dir, error_staging_dir / staging_dir.name, dirs_exist_ok=True)

            click.echo(f"Error: Failed to build {buildername.upper()} documentation.")
            click.echo(e)
            raise e

def merge_folders(source_folder, target_folder):
    """Merge contents of source_folder into target_folder, appending Python files and overwriting others."""
    source_folder = Path(source_folder)
    target_folder = Path(target_folder)

    for source_file in source_folder.rglob('*'):
        if source_file.is_file():
            relative_path = source_file.relative_to(source_folder)
            target_file = target_folder / relative_path

            target_file.parent.mkdir(parents=True, exist_ok=True)

            if source_file.suffix == '.py':
                # Append contents if the file is a Python file
                with open(source_file, 'r') as src, open(target_file, 'a') as tgt:
                    tgt.write(src.read())
            else:
                # Overwrite for non-Python files
                shutil.copy2(source_file, target_file)

@cli.command()
@click.option('--format', type=click.Choice(['html', 'pdf']), default='html', help='Output format')
@click.argument('plant')
def build_technical_report(format, plant):
    """Build documentation for the Technical Report for a specific plant."""
    plant_dir = Path(f'Technical_Report/plants/{plant}').resolve()
    template_dir = Path('Technical_Report/templates/standard').resolve()
    build_dir = Path(f'Technical_Report/plants/{plant}/_build/{format}').resolve()
    buildername = 'html' if format == 'html' else 'latexpdf'
    build_docs(template_dir, build_dir, buildername, paths={'Images': 'Images', '.': plant_dir})

@cli.command()
def clean():
    """Clean all generated files."""
    directories_to_clean = [
        'Textbook',
        'Technical_Report',
        'Technical_Report/plants'
    ]

    for base_dir in directories_to_clean:
        base_dir = Path(base_dir)
        for dir_path in base_dir.rglob('*'):
            if dir_path.is_dir() and dir_path.name in ['_build', '_error_staging']:
                shutil.rmtree(dir_path, ignore_errors=True)
                click.echo(f"Removed directory: {dir_path}")

@cli.command()
@click.option('--format', type=click.Choice(['html', 'pdf']), default='html', help='Output format')
def build_textbook(format):
    """Build documentation for the Textbook."""
    source_dir = Path('Textbook').resolve()
    build_dir = Path(f'Textbook/_build/{format}').resolve()
    buildername = 'html' if format == 'html' else 'latexpdf'
    build_docs(source_dir, build_dir, buildername, paths={'Images': 'Images'})

if __name__ == '__main__':
    cli()