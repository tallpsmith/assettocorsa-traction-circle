
class ColourFader:

    def __init__(self, startColour, endColour):
        self.endColour = endColour
        self.startColour = startColour

    def fade(self, numberOfSlots):
        startColourRed = self.startColour['red']
        endColourRed = self.endColour['red']
        startColourGreen = self.startColour['green']
        endColourGreen = self.endColour['green']
        startColourBlue = self.startColour['blue']
        endColourBlue = self.endColour['blue']
        colourFadeRed = list(
            (x for x in range(startColourRed, endColourRed, -round((startColourRed - endColourRed) / numberOfSlots))))
        colourFadeGreen = list((x for x in range(startColourGreen, endColourGreen,
                                                 -round((startColourGreen - endColourGreen) / numberOfSlots))))
        colourFadeBlue = list((x for x in range(startColourBlue, endColourBlue,
                                                -round((startColourBlue - endColourBlue) / numberOfSlots))))
        colours = list()
        for x in range(numberOfSlots):
            colours.append(
                {'red': (colourFadeRed[x] / 255), 'green': (colourFadeGreen[x] / 255), 'blue': (colourFadeBlue[x] / 255)})

        return colours

