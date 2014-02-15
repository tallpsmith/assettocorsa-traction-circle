class MovingAveragePlotter:
    def __init__(self, averagedOverNumPoints=5):
        self.averagedOverNumPoints = averagedOverNumPoints
        self.previousPointIndex = None
        self.totals = {"x": 0, "y": 0, "z": 0}
        self.counter = 0
        self.previousPointIndex = 0

    def averagePoint(self, averagedPoints):
        averagedPoints.append({"x": self.totals['x'] / self.counter, "y": self.totals['y'] / self.counter,
                               "z": self.totals['z'] / self.counter})

    def plotMovingAverage(self, dataPoints):

        averagedPoints = []
        for point in dataPoints:

            if (self.counter >= self.averagedOverNumPoints):
                self.averagePoint(averagedPoints)
                self.totals['x'] -= dataPoints[self.previousPointIndex]['x']
                self.totals['y'] -= dataPoints[self.previousPointIndex]['y']
                self.totals['z'] -= dataPoints[self.previousPointIndex]['z']
                self.previousPointIndex += 1
            else:
                self.counter += 1
            self.totals['x'] += point['x']
            self.totals['y'] += point['y']
            self.totals['z'] += point['z']

        self.averagePoint(averagedPoints)

        return averagedPoints
