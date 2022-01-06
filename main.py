
import sys
from PySide6.QtGui import QCursor
import pyqtgraph as pg
import pandas as pd

from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCore
from ui_files.chartView import Ui_MainWindow
from json import loads
from refrence.timeRef import MyStringAxis


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.plot1 = self.ui.graphicsView.addPlot(row=1,col=0)
        self.plot2 = self.ui.graphicsView_2.addPlot(row=1,col=0)
        self.dataTuple = self.getData()
        self.yData = self.dataTuple[1]
        self.xData = self.dataTuple[0]
        self.setPlots()
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.plot1.addItem(self.vLine, ignoreBounds=True)
        self.proxy = pg.SignalProxy(self.plot1.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
        self.ui.searchBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.resetChart.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.analyzeBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.resetChart.clicked.connect(self.resetChartClick)
   
       
    def update(self):
        self.region.setZValue(10)
        minX, maxX = self.region.getRegion()
        self.plot1.setXRange(minX, maxX, padding=0)    

    #this will replace getData
    def serachBtnClick(self) -> tuple: 
        pass

    def getData(self):
        with(open("data.txt") as dataFile):
            d = loads(dataFile.readline())
            dates = pd.DataFrame(d).filter(["_date"]).values.tolist()
            closing = pd.DataFrame(d).filter(["_close"]).values.tolist()
            
        return ([dateI[0] for dateI in dates], [closingP[0] for closingP in closing ] )

    def setPlots(self):
        self.region = pg.LinearRegionItem()
        self.region.setZValue(10)
        
        self.region.sigRegionChanged.connect(self.update)

        self.plot2.addItem(self.region,ignoreBounds=True)
        xDict = dict(enumerate(self.xData))
        xAxisItem1 = MyStringAxis(xDict, orientation="bottom")
        xAxisItem2 = MyStringAxis(xDict, orientation="bottom")
        
        self.plot2.setAxisItems({"bottom": xAxisItem1})
        self.plot1.setAxisItems({"bottom": xAxisItem2})
        self.plot2.plot(list(xDict.keys()), self.yData)
        self.plot1.plot(list(xDict.keys()), self.yData)
        self.region.setRegion((0,  len(self.xData) * .1 ))

    # this paints the verticle line in plot 1.
    # but it is buggy when the zoom is increased or decreased.
    # this seems to be a bug with pyqtgraph.
    def mouseMoved(self,evt):
        vb = self.plot1.vb
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.plot1.sceneBoundingRect().contains(pos):
            mousePoint = vb.mapSceneToView(pos)
            index = int(mousePoint.x())
            if index > 0 and index < len(self.xData):
                self.ui.priceLabel.setText("<span style='font-size: 12pt; color:white;'>Date=%s,   <span style='color: green'>Price=%0.1f</span>" % (self.xData[index], self.yData[index]))
                self.vLine.setPos(mousePoint.x())
        
    def resetChartClick(self, event):
        self.plot2.setXRange(0, len(self.dataTuple[0]), padding=0)
        self.plot2.setYRange(0, max(self.dataTuple[1]), padding=0)
        self.plot1.setYRange(0, max(self.dataTuple[1]), padding=0)
        self.region.setRegion((0,  len(self.xData) * .1 ))
        
        minX, maxX = self.region.getRegion()
        self.plot1.setXRange(minX, maxX, padding=0)  


    def analyzeBtnClick(self):
        pass

if __name__ == "__main__":
    app = pg.mkQApp("test")
    window = Window()
    window.show()
    sys.exit(app.exec())
