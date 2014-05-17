class GPlotter():
    def __init__(self, windowSizeX, windowSizeY, maxXRange, maxZRange):
        self.windowSizeY = windowSizeY
        self.windowSizeX = windowSizeX
        self.windowSize = min(windowSizeY, windowSizeX)
        self.maxZRange = maxZRange
        self.maxXRange = maxXRange

    def plotAll(self, dataPoints):
        allPoints = []
        for point in dataPoints:
            allPoints.append(self.plotG(point['x'], point['z']))

        return allPoints


    def plotG(self, xGValue, zGValue):
        # normalize the acceleration to the Maximum G size, and offset that from the center point
        xPoint = ((xGValue / self.maxXRange) * (0.5 * self.windowSize)) + (0.5 * self.windowSizeX)
        yPoint = ((zGValue / self.maxZRange) * (0.5 * self.windowSize)) + (0.5 * self.windowSizeY)

        return xPoint, yPoint