import time

class TractionCircleUpdater:
    def __init__(self, AC, view, model, timeSource=time, maxTimeRange=5000):
        self.AC = AC
        self.view = view
        self.model = model
        self.timeSource = timeSource
        self.maxTimeRange = maxTimeRange

    def doUpdate(self, deltaT):
        x, y, z = self.AC.getAccelerations()

        self.model.addDataPoint(x, y, z)

        timeSpan = self.timeSource.time() - self.maxTimeRange
        self.model.filterPoints(timeSpan)
        self.view.render()