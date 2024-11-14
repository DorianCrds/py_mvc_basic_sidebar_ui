# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_view.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_contentBodyInfoView(object):
    def setupUi(self, contentBodyInfoView):
        if not contentBodyInfoView.objectName():
            contentBodyInfoView.setObjectName(u"contentBodyInfoView")
        contentBodyInfoView.resize(1089, 749)
        self.verticalLayout = QVBoxLayout(contentBodyInfoView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentBodyViewWidget = QWidget(contentBodyInfoView)
        self.contentBodyViewWidget.setObjectName(u"contentBodyViewWidget")
        self.gridLayout = QGridLayout(self.contentBodyViewWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.infoExampleOne = QWidget(self.contentBodyViewWidget)
        self.infoExampleOne.setObjectName(u"infoExampleOne")

        self.gridLayout.addWidget(self.infoExampleOne, 0, 0, 1, 1)

        self.infoExampleTwo = QWidget(self.contentBodyViewWidget)
        self.infoExampleTwo.setObjectName(u"infoExampleTwo")

        self.gridLayout.addWidget(self.infoExampleTwo, 0, 1, 1, 1)

        self.infoExampleThree = QWidget(self.contentBodyViewWidget)
        self.infoExampleThree.setObjectName(u"infoExampleThree")

        self.gridLayout.addWidget(self.infoExampleThree, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.contentBodyViewWidget)


        self.retranslateUi(contentBodyInfoView)

        QMetaObject.connectSlotsByName(contentBodyInfoView)
    # setupUi

    def retranslateUi(self, contentBodyInfoView):
        contentBodyInfoView.setWindowTitle(QCoreApplication.translate("contentBodyInfoView", u"Form", None))
    # retranslateUi

