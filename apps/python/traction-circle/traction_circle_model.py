from collections import deque


dataList = deque()


class TractionCircleModel(object):
    def addDataPoint(self, x, y, z):
        dataList.append({"x": x, "y": y, "z": z})

    def dataPoints(self):
        return deque(dataList)






