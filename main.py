
import sys
import pyqtgraph as pg
import pandas as pd

from PySide6.QtWidgets import QMainWindow
from ui_files.chartView import Ui_MainWindow
from datetime import date
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

        
      
       
    def update(self):
        self.region.setZValue(10)
        minX, maxX = self.region.getRegion()
        self.plot1.setXRange(minX, maxX, padding=0)    


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



if __name__ == "__main__":
    app = pg.mkQApp("test")
    window = Window()
    window.show()
    sys.exit(app.exec())
