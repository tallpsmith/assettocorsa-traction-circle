from collections import deque


class TractionCircleModel(object):
    dataList = deque()

    def addDataPoint(self, x, y, z):
        self.dataList.append({"x": x, "y": y, "z": z})

    def dataPoints(self):
        return deque(self.dataList)






