import ac
import traceback
from colourfader import ColourFader


class TractionCircleView:
    FINAL_COLOUR = {'red': 77, 'green': 184, 'blue': 77} # note that with some start/end values, one of the colour values stepping functions may abort earlier giving uneven array lengths
    START_COLOUR = {'red': 31, 'green': 77, 'blue': 31}

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
            colourFades = self.colourFader.fade(len(dataPoints))

            ac.glColor3f(1.0, 1.0, 1.0)

            i = 0
            for dataPoint in dataPoints:
                x, y = self.gPlotter.plotG(dataPoint['x'], dataPoint['z'])
                ac.glColor3f(colourFades[i]['red'], colourFades[i]['green'], colourFades[i]['blue'])
                i = i + 1
                ac.glQuad(x, y, self.WIDTH, self.HEIGHT)

            ac.glColor3f(1.0, 1.0, 1.0)
            ac.setText(self.label, "{0}".format(len(self.tractionCircleModel.dataPoints())))
        except Exception as e:
            ac.log(str(traceback.format_exc()))



