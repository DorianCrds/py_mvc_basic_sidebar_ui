# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'content.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_contentMainWidget(object):
    def setupUi(self, contentMainWidget):
        if not contentMainWidget.objectName():
            contentMainWidget.setObjectName(u"contentMainWidget")
        contentMainWidget.resize(1040, 832)
        self.verticalLayout = QVBoxLayout(contentMainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.contentHeaderWidget = QWidget(contentMainWidget)
        self.contentHeaderWidget.setObjectName(u"contentHeaderWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentHeaderWidget.sizePolicy().hasHeightForWidth())
        self.contentHeaderWidget.setSizePolicy(sizePolicy)
        self.contentHeaderWidget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.contentHeaderWidget)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.contentHeaderBackToolButton = QToolButton(self.contentHeaderWidget)
        self.contentHeaderBackToolButton.setObjectName(u"contentHeaderBackToolButton")
        self.contentHeaderBackToolButton.setIconSize(QSize(12, 12))
        self.contentHeaderBackToolButton.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.contentHeaderBackToolButton)

        self.contentHeaderLabel = QLabel(self.contentHeaderWidget)
        self.contentHeaderLabel.setObjectName(u"contentHeaderLabel")

        self.horizontalLayout_2.addWidget(self.contentHeaderLabel)

        self.contentHeaderBackHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.contentHeaderBackHorizontalSpacer)


        self.verticalLayout.addWidget(self.contentHeaderWidget)


        self.retranslateUi(contentMainWidget)

        QMetaObject.connectSlotsByName(contentMainWidget)
    # setupUi

    def retranslateUi(self, contentMainWidget):
        contentMainWidget.setWindowTitle(QCoreApplication.translate("contentMainWidget", u"Form", None))
        self.contentHeaderBackToolButton.setText(QCoreApplication.translate("contentMainWidget", u"...", None))
        self.contentHeaderLabel.setText(QCoreApplication.translate("contentMainWidget", u"TextLabel", None))
    # retranslateUi

