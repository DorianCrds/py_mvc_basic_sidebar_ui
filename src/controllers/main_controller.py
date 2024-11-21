from src.views.main_window import MainWindow


class MainController:
    def __init__(self):

        # Initializes view
        self.main_window = MainWindow()

        # Initializes services

        # Initializes models

    def show_view(self) -> None:
        """
        Render view.
        """
        self.main_window.show()