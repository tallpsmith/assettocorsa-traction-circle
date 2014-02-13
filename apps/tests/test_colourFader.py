from unittest import TestCase
from colourfader import ColourFader


class TestColourFader(TestCase):
    def test_fadeSimple(self):
        fader = ColourFader({"red": 255, "green": 255, "blue": 255}, {"red": 0, "green": 0, "blue": 0})

        fadedColours = fader.fade(255)

        self.assertEquals(255, len(fadedColours))

        self.assertEquals(1/255, fadedColours[254]['red'])

    def test_fadeComplex(self):
        START_COLOUR = {'red': 77.0, 'green': 184.0, 'blue': 73.0}
        FINAL_COLOUR = {'red': 31.0, 'green': 77.0, 'blue': 31.0}

        fader = ColourFader({"red": 100, "green": 100, "blue": 100}, {"red": 0, "green": 0, "blue": 0})

        fadedColours = fader.fade(10)

        self.assertEquals(10, len(fadedColours))
