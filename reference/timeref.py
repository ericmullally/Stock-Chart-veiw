import math
import pyqtgraph as pg
import numpy as np

class MyStringAxis(pg.AxisItem):
    def __init__(self, xdict, *args, **kwargs):
        pg.AxisItem.__init__(self, *args, **kwargs)
        self.x_values = np.asarray(xdict.keys()).tolist()
        self.x_strings = list(xdict.values())
     

    def tickStrings(self, values, scale, spacing):
        strings = []
        for v in values:
            
            vs =  math.floor(v * scale)
            # if we have vs in our values, show the string
            # otherwise show nothing
            if vs in self.x_values:
                # Find the string with x_values closest to vs
                vstr = self.x_strings[vs]
            else:
                vstr = ""
            strings.append(vstr)
        return strings