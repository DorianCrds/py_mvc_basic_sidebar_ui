# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_view.ui'
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

class Ui_contentBodyDashboardView(object):
    def setupUi(self, contentBodyDashboardView):
        if not contentBodyDashboardView.objectName():
            contentBodyDashboardView.setObjectName(u"contentBodyDashboardView")
        contentBodyDashboardView.resize(719, 573)
        self.verticalLayout = QVBoxLayout(contentBodyDashboardView)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentBodyViewWidget = QWidget(contentBodyDashboardView)
        self.contentBodyViewWidget.setObjectName(u"contentBodyViewWidget")
        self.gridLayout = QGridLayout(self.contentBodyViewWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.dashboardExampleOneWidget = QWidget(self.contentBodyViewWidget)
        self.dashboardExampleOneWidget.setObjectName(u"dashboardExampleOneWidget")

        self.gridLayout.addWidget(self.dashboardExampleOneWidget, 0, 0, 1, 1)

        self.dashboardExampleTwoWidget = QWidget(self.contentBodyViewWidget)
        self.dashboardExampleTwoWidget.setObjectName(u"dashboardExampleTwoWidget")

        self.gridLayout.addWidget(self.dashboardExampleTwoWidget, 0, 1, 1, 2)

        self.dashboardExampleFourWidget = QWidget(self.contentBodyViewWidget)
        self.dashboardExampleFourWidget.setObjectName(u"dashboardExampleFourWidget")

        self.gridLayout.addWidget(self.dashboardExampleFourWidget, 1, 2, 1, 1)

        self.dashboardExampleThreeWidget = QWidget(self.contentBodyViewWidget)
        self.dashboardExampleThreeWidget.setObjectName(u"dashboardExampleThreeWidget")

        self.gridLayout.addWidget(self.dashboardExampleThreeWidget, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.contentBodyViewWidget)


        self.retranslateUi(contentBodyDashboardView)

        QMetaObject.connectSlotsByName(contentBodyDashboardView)
    # setupUi

    def retranslateUi(self, contentBodyDashboardView):
        contentBodyDashboardView.setWindowTitle(QCoreApplication.translate("contentBodyDashboardView", u"Form", None))
    # retranslateUi

