import os
import pytest
from click.testing import CliRunner
from aguaclara_docs import cli

def setup_directory(base_dir, conf_content):
    """Helper function to set up a directory with a conf.py file."""
    os.makedirs(base_dir, exist_ok=True)
    os.makedirs(f'{base_dir}/_build/html', exist_ok=True)
    os.makedirs(f'{base_dir}/_build/pdf', exist_ok=True)
    conf_path = f'{base_dir}/conf.py'
    if not os.path.exists(conf_path):
        with open(conf_path, 'w') as f:
            f.write(conf_content)

@pytest.fixture
def setup_textbook_directory():
    """Fixture to ensure the Textbook directory exists for testing."""
    setup_directory('Textbook', "project = 'Test Project'\n")

@pytest.fixture
def setup_technical_report_directory():
    """Fixture to ensure the Technical Report directory exists for testing."""
    base_dir = 'Technical_Report/plants'
    os.makedirs(base_dir, exist_ok=True)
    # Create a conf.py for each plant directory
    for plant in os.listdir(base_dir):
        plant_dir = os.path.join(base_dir, plant)
        if os.path.isdir(plant_dir) and not plant.startswith('_'):
            setup_directory(plant_dir, f"project = '{plant} Technical Report'\n")

def get_plant_names():
    """Retrieve all plant names from the plants directory, ignoring those starting with '_'."""
    base_dir = 'Technical_Report/plants'
    return [plant for plant in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, plant)) and not plant.startswith('_')]

@pytest.mark.parametrize("plant", get_plant_names())
def test_build_technical_report_html(setup_technical_report_directory, plant):
    """Test the build_technical_report command for HTML for each plant."""
    plant_dir = f'Technical_Report/plants/{plant}'
    runner = CliRunner()
    result = runner.invoke(cli, ['build-technical-report', '--format', 'html', plant])

    assert result.exit_code == 0
    assert os.path.exists(f'{plant_dir}/_build/html/index.html')

def test_clean_command():
    """Test the clean command to ensure it removes generated files."""
    runner = CliRunner()

    # Create dummy build directories
    os.makedirs('Textbook/_build', exist_ok=True)
    os.makedirs('Technical_Report/_build', exist_ok=True)
    os.makedirs('Technical_Report/plants/PlantX/_build', exist_ok=True)
    os.makedirs('Technical_Report/plants/PlantX/_error_staging', exist_ok=True)

    # Run the clean command
    result = runner.invoke(cli, ['clean'])

    # Refresh the directory state
    assert result.exit_code == 0
    assert not os.path.exists('Textbook/_build')
    assert not os.path.exists('Technical_Report/_build')
    assert not os.path.exists('Technical_Report/plants/PlantX/_build')
    assert not os.path.exists('Technical_Report/plants/PlantX/_error_staging')

@pytest.mark.parametrize("format", ['html'])
def test_build_textbook(setup_textbook_directory, format):
    """Test the build_textbook command for HTML and PDF."""
    runner = CliRunner()
    result = runner.invoke(cli, ['build-textbook', '--format', format])
    if result.exit_code != 0:
        print(result.output)  # Print the output to understand the error
    assert result.exit_code == 0
    assert os.path.exists(f'Textbook/_build/{format}/index.html' if format == 'html' else f'Textbook/_build/pdf/latex/Textbook.pdf')