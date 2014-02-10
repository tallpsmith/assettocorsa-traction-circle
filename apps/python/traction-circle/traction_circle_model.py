import time
from collections import deque


class TractionCircleModel(object):

    def __init__(self, timeSource=time):
        self.timeSource = timeSource
        self.dataList = deque()

    def addDataPoint(self, x, y, z):
        self.dataList.append({"time": self.timeSource.time(), "x": x, "y": y, "z": z})

    def dataPoints(self):
        return deque(self.dataList)

    def filterPoints(self, timeSpan):
        self.dataList = filter(lambda x: x["time"]>= timeSpan, self.dataList)






