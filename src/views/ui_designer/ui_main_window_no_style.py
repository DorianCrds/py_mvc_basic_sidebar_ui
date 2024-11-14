# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_no_style.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 784)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.menuMainWidget = QWidget(self.centralwidget)
        self.menuMainWidget.setObjectName(u"menuMainWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuMainWidget.sizePolicy().hasHeightForWidth())
        self.menuMainWidget.setSizePolicy(sizePolicy)
        self.menuMainWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.menuMainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.menuMainWidget)

        self.contentMainWidget = QWidget(self.centralwidget)
        self.contentMainWidget.setObjectName(u"contentMainWidget")
        self.verticalLayout_2 = QVBoxLayout(self.contentMainWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentHeaderWidget = QWidget(self.contentMainWidget)
        self.contentHeaderWidget.setObjectName(u"contentHeaderWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.contentHeaderWidget.sizePolicy().hasHeightForWidth())
        self.contentHeaderWidget.setSizePolicy(sizePolicy1)
        self.contentHeaderWidget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.contentHeaderWidget)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.contentHeaderLogoLabel = QLabel(self.contentHeaderWidget)
        self.contentHeaderLogoLabel.setObjectName(u"contentHeaderLogoLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contentHeaderLogoLabel.sizePolicy().hasHeightForWidth())
        self.contentHeaderLogoLabel.setSizePolicy(sizePolicy2)
        self.contentHeaderLogoLabel.setMinimumSize(QSize(32, 32))
        self.contentHeaderLogoLabel.setMaximumSize(QSize(30, 30))
        self.contentHeaderLogoLabel.setPixmap(QPixmap(u":/logo/resources/logos/logo.png"))
        self.contentHeaderLogoLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.contentHeaderLogoLabel)

        self.contentHeaderViewNameLabel = QLabel(self.contentHeaderWidget)
        self.contentHeaderViewNameLabel.setObjectName(u"contentHeaderViewNameLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.contentHeaderViewNameLabel.sizePolicy().hasHeightForWidth())
        self.contentHeaderViewNameLabel.setSizePolicy(sizePolicy3)
        self.contentHeaderViewNameLabel.setStyleSheet(u"font-size: 14px; font-weight: bold; color: black;")

        self.horizontalLayout_2.addWidget(self.contentHeaderViewNameLabel)


        self.verticalLayout_2.addWidget(self.contentHeaderWidget)

        self.contentBodyWidget = QWidget(self.contentMainWidget)
        self.contentBodyWidget.setObjectName(u"contentBodyWidget")

        self.verticalLayout_2.addWidget(self.contentBodyWidget)


        self.horizontalLayout.addWidget(self.contentMainWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.contentHeaderLogoLabel.setText("")
        self.contentHeaderViewNameLabel.setText(QCoreApplication.translate("MainWindow", u"VIEW NAME", None))
    # retranslateUi

