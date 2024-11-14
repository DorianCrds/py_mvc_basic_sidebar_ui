# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'side_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_sideBar(object):
    def setupUi(self, sideBar):
        if not sideBar.objectName():
            sideBar.setObjectName(u"sideBar")
        sideBar.resize(94, 897)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sideBar.sizePolicy().hasHeightForWidth())
        sideBar.setSizePolicy(sizePolicy)
        sideBar.setMinimumSize(QSize(0, 700))
        self.sideBarVerticalLayout = QVBoxLayout(sideBar)
        self.sideBarVerticalLayout.setSpacing(0)
        self.sideBarVerticalLayout.setObjectName(u"sideBarVerticalLayout")
        self.sideBarVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideBarMainWidget = QWidget(sideBar)
        self.sideBarMainWidget.setObjectName(u"sideBarMainWidget")
        self.verticalLayout = QVBoxLayout(self.sideBarMainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuCollapseToolButton = QToolButton(self.sideBarMainWidget)
        self.menuCollapseToolButton.setObjectName(u"menuCollapseToolButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menuCollapseToolButton.sizePolicy().hasHeightForWidth())
        self.menuCollapseToolButton.setSizePolicy(sizePolicy1)
        self.menuCollapseToolButton.setMinimumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.menuCollapseToolButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons_32x32/resources/icons/burger.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuCollapseToolButton.setIcon(icon)
        self.menuCollapseToolButton.setIconSize(QSize(20, 20))
        self.menuCollapseToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuCollapseToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuCollapseToolButton)

        self.firstSeparatorParentWidget = QWidget(self.sideBarMainWidget)
        self.firstSeparatorParentWidget.setObjectName(u"firstSeparatorParentWidget")
        sizePolicy1.setHeightForWidth(self.firstSeparatorParentWidget.sizePolicy().hasHeightForWidth())
        self.firstSeparatorParentWidget.setSizePolicy(sizePolicy1)
        self.firstSeparatorParentWidget.setMinimumSize(QSize(0, 20))
        self.firstSeparatorParentWidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.firstSeparatorParentWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.firstSeparatorChildWidget = QWidget(self.firstSeparatorParentWidget)
        self.firstSeparatorChildWidget.setObjectName(u"firstSeparatorChildWidget")
        sizePolicy1.setHeightForWidth(self.firstSeparatorChildWidget.sizePolicy().hasHeightForWidth())
        self.firstSeparatorChildWidget.setSizePolicy(sizePolicy1)
        self.firstSeparatorChildWidget.setMinimumSize(QSize(0, 2))
        self.firstSeparatorChildWidget.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.firstSeparatorChildWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.firstSeparatorParentWidget)

        self.menuDashboardToolButton = QToolButton(self.sideBarMainWidget)
        self.menuDashboardToolButton.setObjectName(u"menuDashboardToolButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menuDashboardToolButton.sizePolicy().hasHeightForWidth())
        self.menuDashboardToolButton.setSizePolicy(sizePolicy2)
        self.menuDashboardToolButton.setMinimumSize(QSize(50, 50))
        self.menuDashboardToolButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons_32x32/resources/icons/diagram.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuDashboardToolButton.setIcon(icon1)
        self.menuDashboardToolButton.setIconSize(QSize(20, 20))
        self.menuDashboardToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.menuDashboardToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuDashboardToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuDashboardToolButton)

        self.menuOptionOneToolButton = QToolButton(self.sideBarMainWidget)
        self.menuOptionOneToolButton.setObjectName(u"menuOptionOneToolButton")
        sizePolicy1.setHeightForWidth(self.menuOptionOneToolButton.sizePolicy().hasHeightForWidth())
        self.menuOptionOneToolButton.setSizePolicy(sizePolicy1)
        self.menuOptionOneToolButton.setMinimumSize(QSize(50, 50))
        self.menuOptionOneToolButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons_32x32/resources/icons/choice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuOptionOneToolButton.setIcon(icon2)
        self.menuOptionOneToolButton.setIconSize(QSize(20, 20))
        self.menuOptionOneToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuOptionOneToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuOptionOneToolButton)

        self.menuOptionTwoToolButton = QToolButton(self.sideBarMainWidget)
        self.menuOptionTwoToolButton.setObjectName(u"menuOptionTwoToolButton")
        sizePolicy1.setHeightForWidth(self.menuOptionTwoToolButton.sizePolicy().hasHeightForWidth())
        self.menuOptionTwoToolButton.setSizePolicy(sizePolicy1)
        self.menuOptionTwoToolButton.setMinimumSize(QSize(50, 50))
        self.menuOptionTwoToolButton.setFont(font)
        self.menuOptionTwoToolButton.setIcon(icon2)
        self.menuOptionTwoToolButton.setIconSize(QSize(20, 20))
        self.menuOptionTwoToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuOptionTwoToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuOptionTwoToolButton)

        self.menuOptionThreeToolButton = QToolButton(self.sideBarMainWidget)
        self.menuOptionThreeToolButton.setObjectName(u"menuOptionThreeToolButton")
        sizePolicy1.setHeightForWidth(self.menuOptionThreeToolButton.sizePolicy().hasHeightForWidth())
        self.menuOptionThreeToolButton.setSizePolicy(sizePolicy1)
        self.menuOptionThreeToolButton.setMinimumSize(QSize(50, 50))
        self.menuOptionThreeToolButton.setFont(font)
        self.menuOptionThreeToolButton.setIcon(icon2)
        self.menuOptionThreeToolButton.setIconSize(QSize(20, 20))
        self.menuOptionThreeToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuOptionThreeToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuOptionThreeToolButton)

        self.menuSecondVSpacer = QSpacerItem(20, 450, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.menuSecondVSpacer)

        self.secondSeparatorParentWidget = QWidget(self.sideBarMainWidget)
        self.secondSeparatorParentWidget.setObjectName(u"secondSeparatorParentWidget")
        sizePolicy1.setHeightForWidth(self.secondSeparatorParentWidget.sizePolicy().hasHeightForWidth())
        self.secondSeparatorParentWidget.setSizePolicy(sizePolicy1)
        self.secondSeparatorParentWidget.setMinimumSize(QSize(0, 20))
        self.secondSeparatorParentWidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.secondSeparatorParentWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.secondSeparatorChildWidget = QWidget(self.secondSeparatorParentWidget)
        self.secondSeparatorChildWidget.setObjectName(u"secondSeparatorChildWidget")
        sizePolicy1.setHeightForWidth(self.secondSeparatorChildWidget.sizePolicy().hasHeightForWidth())
        self.secondSeparatorChildWidget.setSizePolicy(sizePolicy1)
        self.secondSeparatorChildWidget.setMinimumSize(QSize(0, 2))

        self.gridLayout_2.addWidget(self.secondSeparatorChildWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.secondSeparatorParentWidget)

        self.menuInfoToolButton = QToolButton(self.sideBarMainWidget)
        self.menuInfoToolButton.setObjectName(u"menuInfoToolButton")
        sizePolicy1.setHeightForWidth(self.menuInfoToolButton.sizePolicy().hasHeightForWidth())
        self.menuInfoToolButton.setSizePolicy(sizePolicy1)
        self.menuInfoToolButton.setMinimumSize(QSize(50, 50))
        self.menuInfoToolButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons_32x32/resources/icons/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuInfoToolButton.setIcon(icon3)
        self.menuInfoToolButton.setIconSize(QSize(20, 20))
        self.menuInfoToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuInfoToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuInfoToolButton)

        self.menuSettingsToolButton = QToolButton(self.sideBarMainWidget)
        self.menuSettingsToolButton.setObjectName(u"menuSettingsToolButton")
        sizePolicy1.setHeightForWidth(self.menuSettingsToolButton.sizePolicy().hasHeightForWidth())
        self.menuSettingsToolButton.setSizePolicy(sizePolicy1)
        self.menuSettingsToolButton.setMinimumSize(QSize(50, 50))
        self.menuSettingsToolButton.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons_32x32/resources/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuSettingsToolButton.setIcon(icon4)
        self.menuSettingsToolButton.setIconSize(QSize(20, 20))
        self.menuSettingsToolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.menuSettingsToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.menuSettingsToolButton)


        self.sideBarVerticalLayout.addWidget(self.sideBarMainWidget)


        self.retranslateUi(sideBar)

        QMetaObject.connectSlotsByName(sideBar)
    # setupUi

    def retranslateUi(self, sideBar):
        sideBar.setWindowTitle(QCoreApplication.translate("sideBar", u"Form", None))
        self.menuCollapseToolButton.setText(QCoreApplication.translate("sideBar", u"  MENU", None))
        self.menuDashboardToolButton.setText(QCoreApplication.translate("sideBar", u"  DASHBOARD", None))
        self.menuOptionOneToolButton.setText(QCoreApplication.translate("sideBar", u"  OPTION 1", None))
        self.menuOptionTwoToolButton.setText(QCoreApplication.translate("sideBar", u"  OPTION 2", None))
        self.menuOptionThreeToolButton.setText(QCoreApplication.translate("sideBar", u"  OPTION 3", None))
        self.menuInfoToolButton.setText(QCoreApplication.translate("sideBar", u"  INFORMATIONS", None))
        self.menuSettingsToolButton.setText(QCoreApplication.translate("sideBar", u"  SETTINGS", None))
    # retranslateUi

