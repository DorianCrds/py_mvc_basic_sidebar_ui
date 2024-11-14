from PySide6.QtWidgets import QWidget

from src.views.ui_designer.ui_settings_view import Ui_contentBodySettingsView


class SettingsView(QWidget, Ui_contentBodySettingsView):
    def __init__(self):
        super(SettingsView, self).__init__()
        self.setupUi(self)

    def populate_themes_combobox(self, theme_options):
        for theme_option in theme_options:
            self.themeSettingsComboBox.addItem(theme_option)

    def reload_view(self):
        pass