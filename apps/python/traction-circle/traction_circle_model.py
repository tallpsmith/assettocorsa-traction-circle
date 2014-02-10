import time
from collections import deque


class TractionCircleModel(object):
    dataList = deque()

    def __init__(self, timeSource=time):
        self.timeSource = timeSource

    def addDataPoint(self, x, y, z):
        self.dataList.append({"time": self.timeSource.time(), "x": x, "y": y, "z": z})

    def dataPoints(self):
        return deque(self.dataList)






