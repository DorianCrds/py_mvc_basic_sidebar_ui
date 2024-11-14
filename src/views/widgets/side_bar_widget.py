from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from src.views.ui_designer.ui_side_bar import Ui_sideBar


class SideBarWidget(QWidget, Ui_sideBar):
    def __init__(self) -> None:
        super(SideBarWidget, self).__init__()
        self.setupUi(self)

        self.style_sheet_str = """
        #sideBarMainWidget {
            background-color: {menu_background_color};
            border-radius: 8px;
            color: {menu_text_color};
        }
        
        QToolButton {
            background-color: {menu_button_color};
            color: {menu_button_text_color};
            border-radius: 8px;
        }
        
        QToolButton:hover {
            background-color: {menu_button_hover_color};
        	border-right: 3px solid {menu_button_text_color};
        }
        
        #firstSeparatorChildWidget, #secondSeparatorChildWidget {
            background-color: {menu_button_icon_color};
        }
        """

        self.buttons_list = [
            self.menuCollapseToolButton,
            self.menuDashboardToolButton,
            self.menuOptionOneToolButton,
            self.menuOptionTwoToolButton,
            self.menuOptionThreeToolButton,
            self.menuInfoToolButton,
            self.menuSettingsToolButton
        ]

        self.icons_dir_path = ""
        self.burger_icon = QIcon()
        self.left_arrow_icon = QIcon()
        self.diagram_icon = QIcon()
        self.options_icon = QIcon()
        self.info_icon = QIcon()
        self.gear_icon = QIcon()

        self.is_collapsed = True

        self.set_icons_for_theme()

        self.menuCollapseToolButton.clicked.connect(self.on_collapsed_button_clicked)

    def load_icons_for_theme(self):
        self.burger_icon = QIcon(self.icons_dir_path + "burger.png")
        self.left_arrow_icon = QIcon(self.icons_dir_path + "left_arrow.png")
        self.diagram_icon = QIcon(self.icons_dir_path + "diagram.png")
        self.options_icon = QIcon(self.icons_dir_path + "options.png")
        self.info_icon = QIcon(self.icons_dir_path + "info.png")
        self.gear_icon = QIcon(self.icons_dir_path + "gear.png")

    def apply_icons_for_buttons(self):
        self.apply_icon_for_collapsed_button()

        self.menuDashboardToolButton.setIcon(self.diagram_icon)
        self.menuOptionOneToolButton.setIcon(self.options_icon)
        self.menuOptionTwoToolButton.setIcon(self.options_icon)
        self.menuOptionThreeToolButton.setIcon(self.options_icon)
        self.menuInfoToolButton.setIcon(self.info_icon)
        self.menuSettingsToolButton.setIcon(self.gear_icon)

    def apply_icon_for_collapsed_button(self):
        if self.is_collapsed:
            self.menuCollapseToolButton.setIcon(self.burger_icon)
        else:
            self.menuCollapseToolButton.setIcon(self.left_arrow_icon)

    def set_icons_for_theme(self):
        self.load_icons_for_theme()
        self.apply_icons_for_buttons()

    def set_tool_buttons_style(self) -> None:
        for buttons in self.buttons_list:
            if self.is_collapsed:
                new_style = Qt.ToolButtonIconOnly
                specific_buttons_style_sheet = "padding-left: 0;"
            else:
                new_style = Qt.ToolButtonTextBesideIcon
                specific_buttons_style_sheet = "padding-left: 10px; padding-right: 3px"

            buttons.setToolButtonStyle(new_style)
            buttons.setStyleSheet(specific_buttons_style_sheet)

    def on_collapsed_button_clicked(self):
        if self.is_collapsed:
            self.is_collapsed = False
        else:
            self.is_collapsed = True
        self.set_tool_buttons_style()
        self.apply_icon_for_collapsed_button()
