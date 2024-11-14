# Python MVC Example with PySide6 and Qt Designer

This project is a basic example of the **MVC (Model-View-Controller)** architecture implemented in Python using **PySide6** (the official Python bindings for Qt6) and **Qt Designer** for the graphical user interface (GUI) design.

## Project Overview

The goal of this project is to demonstrate how to organize a Python application following the MVC design pattern. The MVC architecture helps separate the concerns of the application, making the code easier to maintain, test, and extend.

### Key Components

1. **Model**: The model handles the business logic, data processing, and interactions with the underlying data storage. It encapsulates the data that the application works with and exposes methods for manipulating and retrieving this data.
   
2. **View**: The view is responsible for rendering the user interface (UI) and presenting data to the user. In this project, the views are created using **Qt Designer**, and the `.ui` files are converted into Python code using the `pyside6-uic` tool.
   
3. **Controller**: The controller acts as an intermediary between the model and the view. It processes user input, manipulates the data in the model, and updates the view as necessary.

### Tools and Technologies

- **Python**: The core programming language used in this project.
- **PySide6**: Provides the Python bindings for the Qt6 framework, allowing you to create cross-platform GUIs.
- **Qt Designer**: A graphical tool used to design the user interface, which generates `.ui` files that are later converted into Python code.
- **pyside6-uic**: A command-line tool to convert `.ui` files created with Qt Designer into Python code.
- **pyside6-rcc**: Used to convert resource files (e.g., icons, images) specified in `.qrc` files into Python code.

### Project Structure

```bash
├── src
│   ├── models            # Contains the application's business logic and data models
│   ├── views
│   │   ├── ui_files      # Contains .ui files created with Qt Designer
│   │   ├── ui_designer   # Python files converted from .ui files (auto-generated)
│   │   ├── main_window.py # The main window of the application (controller part)
│   └── controllers       # Contains controllers that handle user input and update the model/view
└── utils
    └── convert_ui_and_qrc.py # Utility script to convert .ui and .qrc files into Python code
```

## How the Project Works

- **Model**: The business logic is defined in the `models` directory. The model is decoupled from the view and controller, allowing for independent testing and modifications.

- **View**: The UI is designed using **Qt Designer**, which creates `.ui` files stored in the `ui_files` directory. These `.ui` files are then converted into Python classes located in the `ui_designer` directory. These classes define the GUI structure but contain no business logic.

- **Controller**: The controller (`main_window.py`) connects the model and the view. It handles user interactions, updates the model based on user input, and ensures the view reflects any changes in the model.

## Running the Project

To run this project, you need to have **Python 3.11** and **PySide6** installed. You can install the dependencies by running:

```bash
pip install -r requirements.txt
```
Then, you can start the application by running:
```bash
python -m src.main
```

## Utility Scripts

A utility script (`convert_ui_and_qrc.py`) is provided to automatically convert `.ui` files and `.qrc` resource files into Python code. You can run this script using:

```bash
python utils/convert_ui_and_qrc.py
```
This script will:

- Clear the `/ui_designer` directory.
- Convert all `.ui` files from `/ui_files` into Python classes.
- Convert the `.qrc` file containing application resources into Python code.

## Why MVC?

Using the MVC architecture ensures:

- **Separation of Concerns**: Each part of the application has a clear responsibility. The model handles data and logic, the view manages the user interface, and the controller acts as the middleman.

- **Reusability**: Views can be reused with different controllers, and models can be tested independently of the UI.

- **Maintainability**: Changes to one part of the system (e.g., the UI) do not affect the business logic or data handling.

