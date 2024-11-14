from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from src.views.ui_designer.ui_content import Ui_contentMainWidget
from src.views.ui_designer.ui_content_footer import Ui_contentFooterMainWidget


class ContentWidget(QWidget, Ui_contentMainWidget):
    def __init__(self):
        super(ContentWidget, self).__init__()
        self.setupUi(self)

        self.style_sheet_str = """
            #contentHeaderWidget {
                background-color: {content_widget_background};
                color: {content_widget_text_color};
                border-radius: 5px;
            }
            
            #contentHeaderWidget QLabel {
                color: {content_widget_text_color}; 
            }
            
            QToolButton {
                padding: 5px;
            }
            
            #contentFooterChildWidget {
                background-color: {content_widget_background};
                color: {content_widget_text_color};
                border-radius: 5px;
            }
            
            #contentFooterChildWidget QLabel {
                color: {content_widget_text_color}; 
            }
        """

        self.icon_dir_path = ""
        self.back_icon = QIcon()

        self.set_icon_for_theme()

        self.contentHeaderLabel.setText("Basic Qt UI with dynamic sidebar menu")

        self.contentHeaderBackToolButton.clicked.connect(self.on_back_button_clicked)

    def load_icons_for_theme(self):
        self.back_icon = QIcon(self.icon_dir_path + "left_arrow.png")

    def apply_icon_for_buttons(self):
        self.contentHeaderBackToolButton.setIcon(self.back_icon)

    def set_icon_for_theme(self):
        self.load_icons_for_theme()
        self.apply_icon_for_buttons()

    def on_back_button_clicked(self):
        pass

class ContentFooterWidget(QWidget, Ui_contentFooterMainWidget):
    def __init__(self):
        super(ContentFooterWidget, self).__init__()
        self.setupUi(self)

        self.authorLabel.setText("By CARDOSO Dorian")
        self.versionLabel.setText("v1.0.0")