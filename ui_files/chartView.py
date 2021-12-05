# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chartView.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        brush2 = QBrush(QColor(0, 120, 215, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        brush4 = QBrush(QColor(240, 240, 240, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        brush5 = QBrush(QColor(227, 227, 227, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        brush6 = QBrush(QColor(160, 160, 160, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        brush7 = QBrush(QColor(105, 105, 105, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush4)
        brush8 = QBrush(QColor(245, 245, 245, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)

        self.graphicsView_2 = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.gridLayout.addWidget(self.graphicsView_2, 2, 0, 1, 2)

        self.resetChart = QPushButton(self.centralwidget)
        self.resetChart.setObjectName(u"resetChart")
        self.resetChart.setAutoFillBackground(False)
        self.resetChart.setStyleSheet(u"background-color:black;\n"
"color:white;\n"
"")

        self.gridLayout.addWidget(self.resetChart, 4, 0, 1, 1)

        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 2)

        self.searchBtn = QPushButton(self.centralwidget)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setStyleSheet(u"background-color:black;\n"
"color:white;\n"
"")

        self.gridLayout.addWidget(self.searchBtn, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.resetChart.setText(QCoreApplication.translate("MainWindow", u"Reset Charts", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

