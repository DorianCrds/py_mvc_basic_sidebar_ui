import sys

from PySide6.QtWidgets import QApplication

from src.controllers.main_controller import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_controller = MainController()
    main_controller.show_view()
    sys.exit(app.exec())
