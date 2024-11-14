from PySide6.QtWidgets import QWidget

from src.views.ui_designer.ui_info_view import Ui_contentBodyInfoView


class InfoView(QWidget, Ui_contentBodyInfoView):
    def __init__(self):
        super(InfoView, self).__init__()
        self.setupUi(self)

    def reload_view(self):
        pass