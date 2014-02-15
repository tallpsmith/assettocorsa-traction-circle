
#import ac

class MovingAveragePlotter:
    def __init__(self, averagedOverNumPoints=5):
        self.averagedOverNumPoints = averagedOverNumPoints

    def averagePoint(self, averagedPoints, totals, counter):
        averagedPoints.append({"x": totals['x'] / counter, "y": totals['y'] / counter,
                               "z": totals['z'] / counter})

    def plotMovingAverage(self, dataPoints):
        totals = {"x": 0, "y": 0, "z": 0}
        counter = 0
        previousPointIndex = 0

        numPoints = len(dataPoints)

        averagedPoints = []
        if(numPoints < self.averagedOverNumPoints):
            return averagedPoints

        for point in dataPoints:
            #ac.log("len={0}, previous={1}".format(numPoints, previousPointIndex))
            if (counter >= self.averagedOverNumPoints):
                self.averagePoint(averagedPoints, totals, counter)
                if(previousPointIndex<numPoints):
                    totals['x'] -= dataPoints[previousPointIndex]['x']
                    totals['y'] -= dataPoints[previousPointIndex]['y']
                    totals['z'] -= dataPoints[previousPointIndex]['z']
                previousPointIndex += 1
            else:
                counter += 1
            totals['x'] += point['x']
            totals['y'] += point['y']
            totals['z'] += point['z']

        self.averagePoint(averagedPoints, totals, counter)

        return averagedPoints
