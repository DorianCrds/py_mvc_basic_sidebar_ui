# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'content_footer.ui'
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
    QSpacerItem, QWidget)

class Ui_contentFooterMainWidget(object):
    def setupUi(self, contentFooterMainWidget):
        if not contentFooterMainWidget.objectName():
            contentFooterMainWidget.setObjectName(u"contentFooterMainWidget")
        contentFooterMainWidget.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(contentFooterMainWidget.sizePolicy().hasHeightForWidth())
        contentFooterMainWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(contentFooterMainWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentFooterChildWidget = QWidget(contentFooterMainWidget)
        self.contentFooterChildWidget.setObjectName(u"contentFooterChildWidget")
        sizePolicy.setHeightForWidth(self.contentFooterChildWidget.sizePolicy().hasHeightForWidth())
        self.contentFooterChildWidget.setSizePolicy(sizePolicy)
        self.contentFooterChildWidget.setMinimumSize(QSize(0, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.contentFooterChildWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.authorLabel = QLabel(self.contentFooterChildWidget)
        self.authorLabel.setObjectName(u"authorLabel")

        self.horizontalLayout_2.addWidget(self.authorLabel)

        self.horizontalSpacer = QSpacerItem(218, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.versionLabel = QLabel(self.contentFooterChildWidget)
        self.versionLabel.setObjectName(u"versionLabel")

        self.horizontalLayout_2.addWidget(self.versionLabel)


        self.horizontalLayout.addWidget(self.contentFooterChildWidget)


        self.retranslateUi(contentFooterMainWidget)

        QMetaObject.connectSlotsByName(contentFooterMainWidget)
    # setupUi

    def retranslateUi(self, contentFooterMainWidget):
        contentFooterMainWidget.setWindowTitle(QCoreApplication.translate("contentFooterMainWidget", u"Form", None))
    # retranslateUi

