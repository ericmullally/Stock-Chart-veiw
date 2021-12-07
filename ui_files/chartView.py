# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chartView.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(857, 628)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"background-color:black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.searchTxt = QLineEdit(self.centralwidget)
        self.searchTxt.setObjectName(u"searchTxt")
        self.searchTxt.setStyleSheet(u"background-color:white;")

        self.gridLayout.addWidget(self.searchTxt, 3, 0, 1, 1)

        self.graphicsView_2 = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.gridLayout.addWidget(self.graphicsView_2, 2, 0, 1, 2)

        self.resetChart = QPushButton(self.centralwidget)
        self.resetChart.setObjectName(u"resetChart")
        self.resetChart.setAutoFillBackground(False)
        self.resetChart.setStyleSheet(u"background-color:black;\n"
"color:white;\n"
"border: 1px solid green;\n"
"padding: 3px;")

        self.gridLayout.addWidget(self.resetChart, 4, 0, 1, 1)

        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 2)

        self.searchBtn = QPushButton(self.centralwidget)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setStyleSheet(u"background-color:black;\n"
"color:white;\n"
"border: 1px solid green;\n"
"padding: 3px;\n"
"\n"
"\n"
"")

        self.gridLayout.addWidget(self.searchBtn, 3, 1, 1, 1)

        self.priceLabel = QLabel(self.centralwidget)
        self.priceLabel.setObjectName(u"priceLabel")

        self.gridLayout.addWidget(self.priceLabel, 0, 0, 1, 2)

        self.analyzeBtn = QPushButton(self.centralwidget)
        self.analyzeBtn.setObjectName(u"analyzeBtn")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyzeBtn.sizePolicy().hasHeightForWidth())
        self.analyzeBtn.setSizePolicy(sizePolicy)
        self.analyzeBtn.setStyleSheet(u"background-color:black;\n"
"color:white;\n"
"border: 1px solid green;\n"
"padding: 3px;")

        self.gridLayout.addWidget(self.analyzeBtn, 4, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 857, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchTxt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Stock Symbol", None))
        self.resetChart.setText(QCoreApplication.translate("MainWindow", u"Reset Charts", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.priceLabel.setText("")
        self.analyzeBtn.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
    # retranslateUi

