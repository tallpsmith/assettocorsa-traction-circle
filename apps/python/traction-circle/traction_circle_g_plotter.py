

class GPlotter():

    def __init__(self, windowSizeX, windowSizeY, maxXRange, maxZRange):
        self.windowSizeY = windowSizeY
        self.windowSizeX = windowSizeX
        self.maxZRange = maxZRange
        self.maxXRange = maxXRange

    def plotG(self, xGValue, zGValue):
        xPoint = (xGValue/ self.maxXRange) * self.windowSizeX
        yPoint = (zGValue/ self.maxZRange) * self.windowSizeY

        return xPoint, yPoint