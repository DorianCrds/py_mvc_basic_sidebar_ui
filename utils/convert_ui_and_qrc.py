import os
import shutil
import subprocess

# Path to the project root (one level above the utils directory)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Paths to directories and files
UI_FILES_DIR = os.path.join(BASE_DIR, 'src', 'views', 'ui_files')
UI_DESIGNER_DIR = os.path.join(BASE_DIR, 'src', 'views', 'ui_designer')
RESOURCE_QRC = os.path.join(BASE_DIR, 'src', 'views', 'ui_files', 'src.views.ui_designer.resources.qrc')  # Resources.qrc file
RESOURCE_PY = os.path.join(UI_DESIGNER_DIR, 'resources_rc.py')  # Python file generated from the qrc


def clear_ui_designer_dir():
    """Clears the /ui_designer directory of all existing files."""
    if os.path.exists(UI_DESIGNER_DIR):
        for filename in os.listdir(UI_DESIGNER_DIR):
            file_path = os.path.join(UI_DESIGNER_DIR, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error while deleting file {file_path}: {e}")

    init_file_path = os.path.join(UI_DESIGNER_DIR, '__init__.py')
    try:
        with open(init_file_path, 'w') as f:
            pass  # Simply create an empty file
        print(f"File {init_file_path} recreated.")
    except Exception as e:
        print(f"Error while creating file {init_file_path}: {e}")


def convert_ui_files():
    """Converts .ui files into Python files in the /ui_designer directory."""
    if os.path.exists(UI_FILES_DIR):
        for filename in os.listdir(UI_FILES_DIR):
            if filename.endswith(".ui"):
                ui_file_path = os.path.join(UI_FILES_DIR, filename)
                py_output_name = f"ui_{filename.replace('.ui', '.py')}"
                py_output_path = os.path.join(UI_DESIGNER_DIR, py_output_name)

                # Command to convert .ui to .py
                command = f"pyside6-uic {ui_file_path} -o {py_output_path}"
                try:
                    subprocess.run(command, check=True, shell=True)
                    print(f"Converted {filename} to {py_output_name}")
                except subprocess.CalledProcessError as e:
                    print(f"Error while converting {filename}: {e}")


def convert_qrc_file():
    """Converts the .qrc file into a Python file in /ui_designer named resources_rc.py."""
    if os.path.exists(RESOURCE_QRC):
        # Command to convert .qrc to .py
        command = f"pyside6-rcc {RESOURCE_QRC} -o {RESOURCE_PY}"
        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Converted {RESOURCE_QRC} to {RESOURCE_PY}")
        except subprocess.CalledProcessError as e:
            print(f"Error while converting {RESOURCE_QRC}: {e}")
    else:
        print(f"The file {RESOURCE_QRC} was not found.")


if __name__ == "__main__":
    # Step 1: Clear the /ui_designer directory
    clear_ui_designer_dir()

    # Step 2: Convert .ui files
    convert_ui_files()

    # Step 3: Convert the resources.qrc file
    convert_qrc_file()
