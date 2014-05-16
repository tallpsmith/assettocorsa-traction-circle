import ac
import traceback
from colourfader import ColourFader
from moving_average_plotter import MovingAveragePlotter


class TractionCircleView:
    FINAL_COLOUR_DATA_POINTS = {'red': 77, 'green': 184, 'blue': 77}
    START_COLOUR_DATA_POINTS = {'red': 31, 'green': 77, 'blue': 31}
    FINAL_COLOUR_MOVING_AVERAGE = {'red': 255, 'green': 255, 'blue': 255}
    START_COLOUR_MOVING_AVERAGE = {'red': 64, 'green': 64, 'blue': 64}

    def __init__(self, window, tractionCircleModel, gPlotter, movingAvgPlotter):
        self.WIDTH = 2.0
        self.HEIGHT = 2.0
        self.gPlotter = gPlotter
        self.tractionCircleModel = tractionCircleModel
        self.dataPointsColourFader = ColourFader(self.START_COLOUR_DATA_POINTS, self.FINAL_COLOUR_DATA_POINTS)
        self.movingAverageColourFader = ColourFader(self.START_COLOUR_MOVING_AVERAGE, self.FINAL_COLOUR_MOVING_AVERAGE)
        self.movingAvgPlotter = movingAvgPlotter

    def drawScatterPlot(self, colourFades, dataPoints):
        i = 0
        for dataPoint in dataPoints:
            x, y = self.gPlotter.plotG(dataPoint['x'], dataPoint['z'])
            ac.glColor3f(colourFades[i]['red'], colourFades[i]['green'], colourFades[i]['blue'])
            i = i + 1
            ac.glQuad(x, y, self.WIDTH, self.HEIGHT)
        ac.glColor3f(1.0, 1.0, 1.0)

    def drawMovingAverage(self, colourFades, dataPoints):
        moving_average = self.movingAvgPlotter.plotMovingAverage(dataPoints)
        ac.glColor3f(1.0, 1.0, 1.0)

        i = 0
        ac.glBegin(1)
        for point in moving_average:
            ac.glColor3f(colourFades[i]['red'], colourFades[i]['green'], colourFades[i]['blue'])
            x, y = self.gPlotter.plotG(point['x'], point['z'])
            i = i + 1
            ac.glVertex2f(x,y)
        ac.glEnd()

    def render(self):
        try:
            dataPoints = self.tractionCircleModel.dataPoints()
            dataPointsColourFades = self.dataPointsColourFader.fade(len(dataPoints))
            movingAverageColourFades = self.movingAverageColourFader.fade(len(dataPoints))

            self.drawScatterPlot(dataPointsColourFades, dataPoints)
            self.drawMovingAverage(movingAverageColourFades, dataPoints)

        except Exception as e:
            ac.log(str(traceback.format_exc()))



