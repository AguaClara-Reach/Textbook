import polib
import glob
import os

def clear_msgstr_in_po_file(po_file):
    """
    Clears the msgstr in a .po file.
    """
    po = polib.pofile(po_file)

    for entry in po:
        entry.msgstr = ""  # Clear the msgstr field

    po.save(po_file)  # Save the modified .po file
    print(f"Cleared msgstr in: {po_file}")

def clear_msgstr_in_directory(directory_path):
    # Get all .po files in the directory
    po_files = glob.glob(os.path.join(directory_path, '*.po'))
    
    if not po_files:
        print("No .po files found in the directory.")
        return

    for po_file in po_files:
        clear_msgstr_in_po_file(po_file)

# Path to the directory containing .po files
po_directory = 'po_files/es/LC_MESSAGES'  # Change this to the directory of your .po files

# Run the clearing of msgstr fields
clear_msgstr_in_directory(po_directory)
