# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_view.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_contentBodySettingsView(object):
    def setupUi(self, contentBodySettingsView):
        if not contentBodySettingsView.objectName():
            contentBodySettingsView.setObjectName(u"contentBodySettingsView")
        contentBodySettingsView.resize(983, 581)
        self.verticalLayout = QVBoxLayout(contentBodySettingsView)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentBodyViewWidget = QWidget(contentBodySettingsView)
        self.contentBodyViewWidget.setObjectName(u"contentBodyViewWidget")
        self.gridLayout = QGridLayout(self.contentBodyViewWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsMainWidget = QWidget(self.contentBodyViewWidget)
        self.themeSettingsMainWidget.setObjectName(u"themeSettingsMainWidget")
        self.horizontalLayout = QHBoxLayout(self.themeSettingsMainWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.contentBodySettingsViewLeftHSpacer = QSpacerItem(122, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.contentBodySettingsViewLeftHSpacer)

        self.themeSettingsComboBox = QComboBox(self.themeSettingsMainWidget)
        self.themeSettingsComboBox.setObjectName(u"themeSettingsComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeSettingsComboBox.sizePolicy().hasHeightForWidth())
        self.themeSettingsComboBox.setSizePolicy(sizePolicy)
        self.themeSettingsComboBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.themeSettingsComboBox)

        self.contentBodySettingsViewRightHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.contentBodySettingsViewRightHSpacer)


        self.gridLayout.addWidget(self.themeSettingsMainWidget, 0, 0, 1, 1)

        self.contentSettingsExampleOneWidget = QWidget(self.contentBodyViewWidget)
        self.contentSettingsExampleOneWidget.setObjectName(u"contentSettingsExampleOneWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.contentSettingsExampleOneWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(458, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.contentSettingsExampleOneWidget, 0, 1, 1, 1)

        self.contentSettingsExampleTwoWidget = QWidget(self.contentBodyViewWidget)
        self.contentSettingsExampleTwoWidget.setObjectName(u"contentSettingsExampleTwoWidget")

        self.gridLayout.addWidget(self.contentSettingsExampleTwoWidget, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.contentBodyViewWidget)


        self.retranslateUi(contentBodySettingsView)

        QMetaObject.connectSlotsByName(contentBodySettingsView)
    # setupUi

    def retranslateUi(self, contentBodySettingsView):
        contentBodySettingsView.setWindowTitle(QCoreApplication.translate("contentBodySettingsView", u"Form", None))
    # retranslateUi

