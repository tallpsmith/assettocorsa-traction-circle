import ac
import traceback
from colourfader import ColourFader
from moving_average_plotter import MovingAveragePlotter


class TractionCircleView:
    FINAL_COLOUR = {'red': 77, 'green': 184, 'blue': 77}
    START_COLOUR = {'red': 31, 'green': 77, 'blue': 31}

    def __init__(self, window, tractionCircleModel, gPlotter, movingAvgPlotter):
        self.WIDTH = 2.0
        self.HEIGHT = 2.0
        self.gPlotter = gPlotter
        self.tractionCircleModel = tractionCircleModel
        self.colourFader = ColourFader(self.START_COLOUR, self.FINAL_COLOUR)
        self.movingAvgPlotter = movingAvgPlotter

    def drawScatterPlot(self, colourFades, dataPoints):
        i = 0
        for dataPoint in dataPoints:
            x, y = self.gPlotter.plotG(dataPoint['x'], dataPoint['z'])
            ac.glColor3f(colourFades[i]['red'], colourFades[i]['green'], colourFades[i]['blue'])
            i = i + 1
            ac.glQuad(x, y, self.WIDTH, self.HEIGHT)
        ac.glColor3f(1.0, 1.0, 1.0)

    def drawMovingAverage(self, dataPoints):
        moving_average = self.movingAvgPlotter.plotMovingAverage(dataPoints)
        ac.glColor3f(1.0, 1.0, 1.0)

        ac.glBegin(1)
        for point in moving_average:
            x, y = self.gPlotter.plotG(point['x'], point['z'])
            ac.glVertex2f(x,y)
        ac.glEnd()

    def render(self):
        try:
            dataPoints = self.tractionCircleModel.dataPoints()
            colourFades = self.colourFader.fade(len(dataPoints))

            self.drawScatterPlot(colourFades, dataPoints)
            self.drawMovingAverage(dataPoints)

        except Exception as e:
            ac.log(str(traceback.format_exc()))



