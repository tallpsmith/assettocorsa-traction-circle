import ac


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

    def render(self):
        try:
            dataPoints = self.tractionCircleModel.dataPoints()
            colourFades = self.colourFader(dataPoints.size(), self.START_COLOUR, self.FINAL_COLOUR)

            for dataPoint in dataPoints:
                x, y = self.gPlotter.plotG(dataPoint['x'], dataPoint['z'])
                ac.glColor3f(colourFades['red'], colourFades['green'], colourFades['blue'])
                ac.glQuad(x, y, self.WIDTH, self.HEIGHT)

            ac.setText(self.label, "{0}".format(len(self.tractionCircleModel.dataPoints())))
        except Exception as e:
            ac.log(str(e))


    def colourFader(self, numberOfSlots, startColour, endColour):
        startColourRed = startColour['red']
        endColourRed = endColour['red']
        startColourGreen = startColour['green']
        endColourGreen = endColour['green']
        startColourBlue = startColour['blue']
        endColourBlue = endColour['blue']
        colourFadeRed = list(
            (x for x in range(startColourRed, startColourRed, -round((startColourRed - endColourRed) / numberOfSlots))))
        colourFadeGreen = list((x for x in range(startColourGreen, startColourGreen,
                                                 -round((startColourGreen - endColourGreen) / numberOfSlots))))
        colourFadeBlue = list((x for x in range(startColourBlue, startColourBlue,
                                                -round((startColourBlue - endColourBlue) / numberOfSlots))))
        colours = list()
        for x in range(numberOfSlots):
            colours.append(
                {'red': colourFadeRed[x] / 255, 'green': colourFadeGreen[x] / 255, 'blue': colourFadeBlue[x]} / 255)

        return colours

