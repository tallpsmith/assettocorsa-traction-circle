#import ac

class ColourFader:
    def __init__(self, startColour, endColour):
        self.endColour = endColour
        self.startColour = startColour

    def fade(self, numberOfSlots):
        if numberOfSlots <= 1:
            return [self.toFloat(self.startColour), self.toFloat(self.endColour)]

        startColourRed = self.startColour['red']
        endColourRed = self.endColour['red']
        startColourGreen = self.startColour['green']
        endColourGreen = self.endColour['green']
        startColourBlue = self.startColour['blue']
        endColourBlue = self.endColour['blue']

        colourFadeRed =   list(startColourRed-(startColourRed-endColourRed)/numberOfSlots*x for x in range(numberOfSlots))
        colourFadeGreen =   list(startColourGreen-(startColourGreen-endColourGreen)/numberOfSlots*x for x in range(numberOfSlots))
        colourFadeBlue =   list(startColourBlue-(startColourBlue-endColourBlue)/numberOfSlots*x for x in range(numberOfSlots))

        colours = list()
        for x in range(numberOfSlots):
            colours.append(
                {'red': (colourFadeRed[x] / 255), 'green': (colourFadeGreen[x] / 255),
                 'blue': (colourFadeBlue[x] / 255)})

        return colours

    def toFloat(self, colour):
        return {"red": colour['red'] / 255, "green": colour['green'] / 255, 'blue': colour['blue'] / 255}

