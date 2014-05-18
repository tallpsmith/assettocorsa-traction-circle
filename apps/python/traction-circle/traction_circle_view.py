import ac, acsys
import traceback
from math import sin, cos, pi
from colourfader import ColourFader
from moving_average_plotter import MovingAveragePlotter


class TractionCircleView:
    FINAL_COLOUR_DATA_POINTS =    (0.25, 0.50, 0.10, 1.00)
    START_COLOUR_DATA_POINTS =    (0.00, 0.75, 0.00, 0.00)
    FINAL_COLOUR_MOVING_AVERAGE = (1.00, 1.00, 1.00, 1.00)
    START_COLOUR_MOVING_AVERAGE = (0.75, 0.75, 0.75, 0.25)

    def __init__(self, window, tractionCircleModel, gPlotter, movingAvgPlotter):
        self.scatterSize = 0.04
        self.currentSize = 0.10
        self.gPlotter = gPlotter
        self.tractionCircleModel = tractionCircleModel
        self.dataPointsColourFader = ColourFader(self.START_COLOUR_DATA_POINTS, self.FINAL_COLOUR_DATA_POINTS)
        self.movingAverageColourFader = ColourFader(self.START_COLOUR_MOVING_AVERAGE, self.FINAL_COLOUR_MOVING_AVERAGE)
        self.movingAvgPlotter = movingAvgPlotter

    def drawCross(self, radius):
        ac.glBegin(1)
        ac.glVertex2f(*self.gPlotter.plotG(-radius, 0))
        ac.glVertex2f(*self.gPlotter.plotG(+radius, 0))
        ac.glEnd()
        ac.glBegin(1)
        ac.glVertex2f(*self.gPlotter.plotG(0, -radius))
        ac.glVertex2f(*self.gPlotter.plotG(0, +radius))
        ac.glEnd()

    def drawCircumference(self, radius, center):
        ac.glBegin(1)
        nlines = max(4, int(100.*radius))
        for i in range(nlines+1):
            x, y = self.gPlotter.plotG(center['x'] + (sin(2*pi*i/nlines)*radius), center['z'] + (cos(2*pi*i/nlines)*radius))
            ac.glVertex2f(x, y)
        ac.glEnd()

    def drawCircle(self, radius, center):
        ac.glBegin(acsys.GL.Triangles)
        prevx, prevy = self.gPlotter.plotG(center['x'], center['z'])
        ntriangles = max(4, int(100.*radius))
        for i in range(ntriangles+1):
            ac.glVertex2f(*self.gPlotter.plotG(center['x'], center['z']))
            ac.glVertex2f(prevx, prevy)
            x, y = self.gPlotter.plotG(center['x'] + (sin(2*pi*i/ntriangles)*radius), center['z'] + (cos(2*pi*i/ntriangles)*radius))
            ac.glVertex2f(x, y)
            prevx, prevy = x, y
        ac.glEnd()

    def drawGrid(self, radius):
        ac.glColor4f(0.8, 0.8, 0.8, 0.7)
        self.drawCross(radius)
        ac.glColor4f(1.0, 1.0, 1.0, 0.9)
        self.drawCircumference(radius, {'x':0, 'z':0})
        self.drawCircumference(radius/2, {'x':0, 'z':0})

    def drawScatterPlot(self, colourFades, dataPoints):
        for dataPoint, colour in zip(dataPoints, colourFades):
            ac.glColor4f(*colour)
            self.drawCircle(self.scatterSize, dataPoint)
        ac.glColor3f(1.0, 1.0, 1.0)

    def drawLinePlot(self, colourFades, dataPoints):
        ac.glBegin(1)
        for dataPoint, colour in zip(dataPoints, colourFades):
            ac.glColor4f(*colour)
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

            self.drawGrid(self.gPlotter.maxXRange)
            self.drawScatterPlot(dataPointsColourFades, dataPoints)
            self.drawLinePlot(movingAverageColourFades, moving_average)
            if len(moving_average) > 0:
                self.drawPoint(self.currentSize, moving_average[-1])

        except Exception as e:
            ac.log(str(traceback.format_exc()))



