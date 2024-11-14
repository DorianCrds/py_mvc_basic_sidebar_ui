from PySide6.QtWidgets import QWidget

from src.views.ui_designer.ui_dashboard_view import Ui_contentBodyDashboardView


class DashboardView(QWidget, Ui_contentBodyDashboardView):
    def __init__(self):
        super(DashboardView, self).__init__()
        self.setupUi(self)

    def reload_view(self):
        pass