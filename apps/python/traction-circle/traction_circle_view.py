import ac, acsys
import traceback
from math import sin, cos, pi
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
        self.currentSize = 0.10
        self.gPlotter = gPlotter
        self.tractionCircleModel = tractionCircleModel
        self.dataPointsColourFader = ColourFader(self.START_COLOUR_DATA_POINTS, self.FINAL_COLOUR_DATA_POINTS)
        self.movingAverageColourFader = ColourFader(self.START_COLOUR_MOVING_AVERAGE, self.FINAL_COLOUR_MOVING_AVERAGE)
        self.movingAvgPlotter = movingAvgPlotter

    def drawCircle(self, radius, center):
        ac.glBegin(acsys.GL.Triangles)
        prevx, prevy = self.gPlotter.plotG(center['x'], center['z'])
        for i in range(101):
            ac.glVertex2f(*self.gPlotter.plotG(center['x'], center['z']))
            ac.glVertex2f(prevx, prevy)
            x, y = self.gPlotter.plotG(center['x'] + (sin(2*pi*i/100.)*radius), center['z'] + (cos(2*pi*i/100.)*radius))
            ac.glVertex2f(x, y)
            prevx, prevy = x, y
        ac.glEnd()

    def drawScatterPlot(self, colourFades, dataPoints):
        for dataPoint, colour in zip(dataPoints, colourFades):
            x, y = self.gPlotter.plotG(dataPoint['x'], dataPoint['z'])
            ac.glColor3f(colour['red'], colour['green'], colour['blue'])
            ac.glQuad(x, y, self.WIDTH, self.HEIGHT)
        ac.glColor3f(1.0, 1.0, 1.0)

    def drawLinePlot(self, colourFades, dataPoints):
        ac.glBegin(1)
        for dataPoint, colour in zip(dataPoints, colourFades):
            ac.glColor3f(colour['red'], colour['green'], colour['blue'])
            x, y = self.gPlotter.plotG(dataPoint['x'], dataPoint['z'])
            ac.glVertex2f(x,y)
        ac.glEnd()

    def drawPoint(self, radius, dataPoint):
        ac.glColor3f(0.2, 1.0, 0.2)
        self.drawCircle(radius, dataPoint)
        ac.glColor3f(1.0, 1.0, 1.0)
        self.drawCircumference(radius, dataPoint)

    def render(self):
        try:
            dataPoints = self.tractionCircleModel.dataPoints()
            moving_average = self.movingAvgPlotter.plotMovingAverage(dataPoints)
            dataPointsColourFades = self.dataPointsColourFader.fade(len(dataPoints))
            movingAverageColourFades = self.movingAverageColourFader.fade(len(dataPoints))

            self.drawScatterPlot(dataPointsColourFades, dataPoints)
            self.drawLinePlot(movingAverageColourFades, moving_average)
            if len(moving_average) > 0:
                self.drawPoint(self.currentSize, moving_average[-1])

        except Exception as e:
            ac.log(str(traceback.format_exc()))



