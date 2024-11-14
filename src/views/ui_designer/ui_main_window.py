# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)
import src.views.ui_designer.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 784)
        MainWindow.setStyleSheet(u"background-color: #e5e5e5;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.menuMainWidget = QWidget(self.centralwidget)
        self.menuMainWidget.setObjectName(u"menuMainWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuMainWidget.sizePolicy().hasHeightForWidth())
        self.menuMainWidget.setSizePolicy(sizePolicy)
        self.menuMainWidget.setMinimumSize(QSize(0, 700))
        self.menuMainWidget.setStyleSheet(u"#menuMainWidget {\n"
"    background-color: #0077b6;\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.menuMainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.menuCollapseToolButton = QToolButton(self.menuMainWidget)
        self.menuCollapseToolButton.setObjectName(u"menuCollapseToolButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menuCollapseToolButton.sizePolicy().hasHeightForWidth())
        self.menuCollapseToolButton.setSizePolicy(sizePolicy1)
        self.menuCollapseToolButton.setMinimumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.menuCollapseToolButton.setFont(font)
        self.menuCollapseToolButton.setStyleSheet(u"QToolButton {\n"
"    background-color: #0077b6;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #005B8C;\n"
"	border-right: 3px solid white;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons_32x32/resources/icons/burger.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuCollapseToolButton.setIcon(icon)
        self.menuCollapseToolButton.setIconSize(QSize(24, 24))
        self.menuCollapseToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuCollapseToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuCollapseToolButton)

        self.firstSeparatorParentWidget = QWidget(self.menuMainWidget)
        self.firstSeparatorParentWidget.setObjectName(u"firstSeparatorParentWidget")
        sizePolicy1.setHeightForWidth(self.firstSeparatorParentWidget.sizePolicy().hasHeightForWidth())
        self.firstSeparatorParentWidget.setSizePolicy(sizePolicy1)
        self.firstSeparatorParentWidget.setMinimumSize(QSize(0, 20))
        self.firstSeparatorParentWidget.setMaximumSize(QSize(16777215, 16777215))
        self.firstSeparatorParentWidget.setStyleSheet(u"background-color: rgb(0, 119, 182);")
        self.gridLayout = QGridLayout(self.firstSeparatorParentWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.firstSeparatorChildWidget = QWidget(self.firstSeparatorParentWidget)
        self.firstSeparatorChildWidget.setObjectName(u"firstSeparatorChildWidget")
        sizePolicy1.setHeightForWidth(self.firstSeparatorChildWidget.sizePolicy().hasHeightForWidth())
        self.firstSeparatorChildWidget.setSizePolicy(sizePolicy1)
        self.firstSeparatorChildWidget.setMinimumSize(QSize(0, 2))
        self.firstSeparatorChildWidget.setMaximumSize(QSize(16777215, 16777215))
        self.firstSeparatorChildWidget.setStyleSheet(u"background-color: #e5e5e5;")

        self.gridLayout.addWidget(self.firstSeparatorChildWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.firstSeparatorParentWidget)

        self.menuDashboardToolButton = QToolButton(self.menuMainWidget)
        self.menuDashboardToolButton.setObjectName(u"menuDashboardToolButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menuDashboardToolButton.sizePolicy().hasHeightForWidth())
        self.menuDashboardToolButton.setSizePolicy(sizePolicy2)
        self.menuDashboardToolButton.setMinimumSize(QSize(50, 50))
        self.menuDashboardToolButton.setFont(font)
        self.menuDashboardToolButton.setStyleSheet(u"QToolButton {\n"
"    background-color: #0077b6;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #005B8C;\n"
"	border-right: 3px solid white;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons_32x32/resources/icons/diagram.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuDashboardToolButton.setIcon(icon1)
        self.menuDashboardToolButton.setIconSize(QSize(24, 24))
        self.menuDashboardToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.menuDashboardToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuDashboardToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuDashboardToolButton)

        self.menuOptionOneToolButton = QToolButton(self.menuMainWidget)
        self.menuOptionOneToolButton.setObjectName(u"menuOptionOneToolButton")
        sizePolicy1.setHeightForWidth(self.menuOptionOneToolButton.sizePolicy().hasHeightForWidth())
        self.menuOptionOneToolButton.setSizePolicy(sizePolicy1)
        self.menuOptionOneToolButton.setMinimumSize(QSize(50, 50))
        self.menuOptionOneToolButton.setFont(font)
        self.menuOptionOneToolButton.setStyleSheet(u"QToolButton {\n"
"    background-color: #0077b6;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #005B8C;\n"
"	border-right: 3px solid white;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons_32x32/resources/icons/choice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuOptionOneToolButton.setIcon(icon2)
        self.menuOptionOneToolButton.setIconSize(QSize(24, 24))
        self.menuOptionOneToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuOptionOneToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuOptionOneToolButton)

        self.menuOptionTwoToolButton = QToolButton(self.menuMainWidget)
        self.menuOptionTwoToolButton.setObjectName(u"menuOptionTwoToolButton")
        sizePolicy1.setHeightForWidth(self.menuOptionTwoToolButton.sizePolicy().hasHeightForWidth())
        self.menuOptionTwoToolButton.setSizePolicy(sizePolicy1)
        self.menuOptionTwoToolButton.setMinimumSize(QSize(50, 50))
        self.menuOptionTwoToolButton.setFont(font)
        self.menuOptionTwoToolButton.setStyleSheet(u"QToolButton {\n"
"    background-color: #0077b6;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #005B8C;\n"
"	border-right: 3px solid white;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        self.menuOptionTwoToolButton.setIcon(icon2)
        self.menuOptionTwoToolButton.setIconSize(QSize(24, 24))
        self.menuOptionTwoToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuOptionTwoToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuOptionTwoToolButton)

        self.menuOptionThreeToolButton = QToolButton(self.menuMainWidget)
        self.menuOptionThreeToolButton.setObjectName(u"menuOptionThreeToolButton")
        sizePolicy1.setHeightForWidth(self.menuOptionThreeToolButton.sizePolicy().hasHeightForWidth())
        self.menuOptionThreeToolButton.setSizePolicy(sizePolicy1)
        self.menuOptionThreeToolButton.setMinimumSize(QSize(50, 50))
        self.menuOptionThreeToolButton.setFont(font)
        self.menuOptionThreeToolButton.setStyleSheet(u"QToolButton {\n"
"    background-color: #0077b6;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #005B8C;\n"
"	border-right: 3px solid white;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        self.menuOptionThreeToolButton.setIcon(icon2)
        self.menuOptionThreeToolButton.setIconSize(QSize(24, 24))
        self.menuOptionThreeToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuOptionThreeToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuOptionThreeToolButton)

        self.menuSecondVSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.menuSecondVSpacer)

        self.secondSeparatorParentWidget = QWidget(self.menuMainWidget)
        self.secondSeparatorParentWidget.setObjectName(u"secondSeparatorParentWidget")
        sizePolicy1.setHeightForWidth(self.secondSeparatorParentWidget.sizePolicy().hasHeightForWidth())
        self.secondSeparatorParentWidget.setSizePolicy(sizePolicy1)
        self.secondSeparatorParentWidget.setMinimumSize(QSize(0, 20))
        self.secondSeparatorParentWidget.setMaximumSize(QSize(16777215, 16777215))
        self.secondSeparatorParentWidget.setStyleSheet(u"background-color: rgb(0, 119, 182);")
        self.gridLayout_2 = QGridLayout(self.secondSeparatorParentWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.secondSeparatorChildWidget = QWidget(self.secondSeparatorParentWidget)
        self.secondSeparatorChildWidget.setObjectName(u"secondSeparatorChildWidget")
        sizePolicy1.setHeightForWidth(self.secondSeparatorChildWidget.sizePolicy().hasHeightForWidth())
        self.secondSeparatorChildWidget.setSizePolicy(sizePolicy1)
        self.secondSeparatorChildWidget.setMinimumSize(QSize(0, 2))
        self.secondSeparatorChildWidget.setStyleSheet(u"background-color: #e5e5e5;")

        self.gridLayout_2.addWidget(self.secondSeparatorChildWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.secondSeparatorParentWidget)

        self.menuInfoToolButton = QToolButton(self.menuMainWidget)
        self.menuInfoToolButton.setObjectName(u"menuInfoToolButton")
        sizePolicy1.setHeightForWidth(self.menuInfoToolButton.sizePolicy().hasHeightForWidth())
        self.menuInfoToolButton.setSizePolicy(sizePolicy1)
        self.menuInfoToolButton.setMinimumSize(QSize(50, 50))
        self.menuInfoToolButton.setFont(font)
        self.menuInfoToolButton.setStyleSheet(u"QToolButton {\n"
"    background-color: #0077b6;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #005B8C;\n"
"	border-right: 3px solid white;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons_32x32/resources/icons/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuInfoToolButton.setIcon(icon3)
        self.menuInfoToolButton.setIconSize(QSize(24, 24))
        self.menuInfoToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuInfoToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuInfoToolButton)

        self.menuSettingsToolButton = QToolButton(self.menuMainWidget)
        self.menuSettingsToolButton.setObjectName(u"menuSettingsToolButton")
        sizePolicy1.setHeightForWidth(self.menuSettingsToolButton.sizePolicy().hasHeightForWidth())
        self.menuSettingsToolButton.setSizePolicy(sizePolicy1)
        self.menuSettingsToolButton.setMinimumSize(QSize(50, 50))
        self.menuSettingsToolButton.setFont(font)
        self.menuSettingsToolButton.setStyleSheet(u"QToolButton {\n"
"    background-color: #0077b6;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #005B8C;\n"
"	border-right: 3px solid white;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons_32x32/resources/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuSettingsToolButton.setIcon(icon4)
        self.menuSettingsToolButton.setIconSize(QSize(24, 24))
        self.menuSettingsToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuSettingsToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuSettingsToolButton)


        self.horizontalLayout.addWidget(self.menuMainWidget)

        self.contentMainWidget = QWidget(self.centralwidget)
        self.contentMainWidget.setObjectName(u"contentMainWidget")
        self.verticalLayout_2 = QVBoxLayout(self.contentMainWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentHeaderWidget = QWidget(self.contentMainWidget)
        self.contentHeaderWidget.setObjectName(u"contentHeaderWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.contentHeaderWidget.sizePolicy().hasHeightForWidth())
        self.contentHeaderWidget.setSizePolicy(sizePolicy3)
        self.contentHeaderWidget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.contentHeaderWidget)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.contentHeaderLogoLabel = QLabel(self.contentHeaderWidget)
        self.contentHeaderLogoLabel.setObjectName(u"contentHeaderLogoLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.contentHeaderLogoLabel.sizePolicy().hasHeightForWidth())
        self.contentHeaderLogoLabel.setSizePolicy(sizePolicy4)
        self.contentHeaderLogoLabel.setMinimumSize(QSize(32, 32))
        self.contentHeaderLogoLabel.setMaximumSize(QSize(30, 30))
        self.contentHeaderLogoLabel.setPixmap(QPixmap(u":/logo/resources/logos/logo.png"))
        self.contentHeaderLogoLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.contentHeaderLogoLabel)

        self.contentHeaderViewNameLabel = QLabel(self.contentHeaderWidget)
        self.contentHeaderViewNameLabel.setObjectName(u"contentHeaderViewNameLabel")
        sizePolicy1.setHeightForWidth(self.contentHeaderViewNameLabel.sizePolicy().hasHeightForWidth())
        self.contentHeaderViewNameLabel.setSizePolicy(sizePolicy1)
        self.contentHeaderViewNameLabel.setStyleSheet(u"font-size: 14px; font-weight: bold; color: black;")

        self.horizontalLayout_2.addWidget(self.contentHeaderViewNameLabel)


        self.verticalLayout_2.addWidget(self.contentHeaderWidget)

        self.contentBodyWidget = QWidget(self.contentMainWidget)
        self.contentBodyWidget.setObjectName(u"contentBodyWidget")
        self.contentBodyWidget.setStyleSheet(u"background-color: white; border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.contentBodyWidget)


        self.horizontalLayout.addWidget(self.contentMainWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuCollapseToolButton.setText(QCoreApplication.translate("MainWindow", u"  MENU", None))
        self.menuDashboardToolButton.setText(QCoreApplication.translate("MainWindow", u"  DASHBOARD", None))
        self.menuOptionOneToolButton.setText(QCoreApplication.translate("MainWindow", u"  OPTION 1", None))
        self.menuOptionTwoToolButton.setText(QCoreApplication.translate("MainWindow", u"  OPTION 2", None))
        self.menuOptionThreeToolButton.setText(QCoreApplication.translate("MainWindow", u"  OPTION 3", None))
        self.menuInfoToolButton.setText(QCoreApplication.translate("MainWindow", u"  INFORMATIONS", None))
        self.menuSettingsToolButton.setText(QCoreApplication.translate("MainWindow", u"  SETTINGS", None))
        self.contentHeaderLogoLabel.setText("")
        self.contentHeaderViewNameLabel.setText(QCoreApplication.translate("MainWindow", u"VIEW NAME", None))
    # retranslateUi

