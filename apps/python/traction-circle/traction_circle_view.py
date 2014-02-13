import ac
from colourfader import ColourFader


class TractionCircleView:
    START_COLOUR = {'red': 77.0, 'green': 184.0, 'blue': 73.0}
    FINAL_COLOUR = {'red': 31.0, 'green': 77.0, 'blue': 31.0}

    def __init__(self, window, tractionCircleModel, gPlotter):
        self.WIDTH = 2.0
        self.HEIGHT = 2.0

        self.gPlotter = gPlotter
        self.label = ac.addLabel(window, '')
        ac.setPosition(self.label, 160, 180)

        self.tractionCircleModel = tractionCircleModel
        self.colourFader = ColourFader(self.START_COLOUR, self.FINAL_COLOUR)

    def render(self):
        try:
            dataPoints = self.tractionCircleModel.dataPoints()
            colourFades = self.colourFader.fade(dataPoints.size())

            for dataPoint in dataPoints:
                x, y = self.gPlotter.plotG(dataPoint['x'], dataPoint['z'])
                ac.glColor3f(colourFades['red'], colourFades['green'], colourFades['blue'])
                ac.glQuad(x, y, self.WIDTH, self.HEIGHT)

            ac.setText(self.label, "{0}".format(len(self.tractionCircleModel.dataPoints())))
        except Exception as e:
            ac.log(str(e))



