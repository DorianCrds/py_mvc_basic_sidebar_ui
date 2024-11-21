from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget

from src.controllers.settings_controller import SettingsController
from src.views.dashboard_view import DashboardView
from src.views.info_view import InfoView
from src.views.settings_view import SettingsView
from src.views.widgets.content_widget import ContentWidget, ContentFooterWidget
from src.views.widgets.side_bar_widget import SideBarWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.style_sheet_str = """
        #MainWindow {
            background-color: {content_background_color};
        }

        #contentBodyViewWidget QWidget {
            background-color: {content_widget_background};
            color: {content_widget_text_color};
            border-radius: 5px;
            padding: 10px;
        }

        #contentBodyViewWidget QComboBox {
            background-color: {combobox_background_color};
            color: {combobox_text_color};
            border: 1px solid {combobox_border_color};
            padding: 5px;
            padding-right: 20px;
        }

        #contentBodyViewWidget QComboBox::down-arrow {
            image: url("{combobox_icon_path}");
            width: 12px;
            height: 12px;
        }

        #contentBodyViewWidget QComboBox QAbstractItemView {
            background-color: {combobox_background_color};
            color: {combobox_text_color};
            selection-background-color: {menu_button_hover_color};
            border: 1px solid {combobox_border_color};
        }
        
        #contentBodyViewWidget QComboBox QAbstractItemView::item:hover {
            background-color: {combobox_hover_background_color};
            color: {combobox_hover_text_color};
            border-left: 2px solid {combobox_hover_border_color};
        }
        
        #contentBodyViewWidget QComboBox QAbstractItemView::item:selected {
            background-color: {combobox_selected_background_color};
            color: {combobox_selected_text_color};
            border-left: 2px solid {combobox_selected_border_color};
        }
        """

        # Setup controllers
        self.settings_controller = SettingsController()

        # Setup main window
        self.setObjectName("MainWindow")

        self.resize(1200, 780)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.main_layout.setSpacing(6)

        # Setup left part with a menu
        self.menuMainWidget = SideBarWidget()
        self.menuMainWidget.setObjectName("menuMainWidget")
        self.main_layout.addWidget(self.menuMainWidget)

        # Setup right part with content space
        self.content_main_widget = ContentWidget()
        self.content_main_widget.contentHeaderBackToolButton.hide()
        self.main_layout.addWidget(self.content_main_widget)

        # Instanciates available views for content
        self.dashboard_view = DashboardView()
        self.info_view = InfoView()
        self.settings_view = SettingsView()
        self.settings_view.populate_themes_combobox(self.settings_controller.get_all_themes_names())
        self.settings_view.themeSettingsComboBox.setCurrentText(self.settings_controller.get_current_theme_name())

        self.content_footer_widget = ContentFooterWidget()

        # Initial view : Dashboard
        self.current_content_body_widget = None
        self.set_content_body_widget(self.dashboard_view)

        # Applies theme for UI using app settings
        self.apply_theme()

        # Setup connections
        self.menuMainWidget.menuDashboardToolButton.clicked.connect(self.on_dashboard_button_clicked)
        self.menuMainWidget.menuInfoToolButton.clicked.connect(self.on_info_button_clicked)
        self.menuMainWidget.menuSettingsToolButton.clicked.connect(self.on_settings_button_clicked)
        self.settings_view.themeSettingsComboBox.currentIndexChanged.connect(self.on_theme_changed)

    def clear_content_body_layout(self):
        if self.current_content_body_widget:
            self.content_main_widget.verticalLayout.removeWidget(self.current_content_body_widget)
            self.current_content_body_widget.setParent(None)
            self.current_content_body_widget = None

    def set_content_body_widget(self, new_widget: QWidget):
        self.clear_content_body_layout()
        self.current_content_body_widget = new_widget
        self.content_main_widget.verticalLayout.addWidget(self.current_content_body_widget)
        self.content_main_widget.verticalLayout.addWidget(self.content_footer_widget)

    def on_dashboard_button_clicked(self):
        self.set_content_body_widget(self.dashboard_view)
        self.dashboard_view.reload_view()

    def on_info_button_clicked(self):
        self.set_content_body_widget(self.info_view)
        self.info_view.reload_view()

    def on_settings_button_clicked(self):
        self.set_content_body_widget(self.settings_view)
        self.settings_view.reload_view()

    def on_theme_changed(self):
        self.settings_controller.set_new_theme(self.settings_view.themeSettingsComboBox.currentText())
        self.apply_theme()

    def apply_theme(self):
        self.setStyleSheet(self.settings_controller.load_style_sheet_for_theme(self.style_sheet_str))
        self.content_main_widget.setStyleSheet(self.settings_controller.load_style_sheet_for_theme(self.content_main_widget.style_sheet_str))
        self.content_main_widget.icon_dir_path = "./resources/icons/" + self.settings_controller.get_current_theme_name() + "/"
        self.content_main_widget.set_icon_for_theme()
        # self.content_main_widget.setStyleSheet(self.settings_controller.load_style_sheet_for_theme(self.content_footer_widget.style_sheet_str))
        self.menuMainWidget.setStyleSheet(self.settings_controller.load_style_sheet_for_theme(self.menuMainWidget.style_sheet_str))
        self.menuMainWidget.icons_dir_path = "./resources/icons/" + self.settings_controller.get_current_theme_name() + "/"
        self.menuMainWidget.set_icons_for_theme()
