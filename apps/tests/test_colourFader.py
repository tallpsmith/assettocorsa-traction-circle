from unittest import TestCase
from colourfader import ColourFader


class TestColourFader(TestCase):
    def test_fadeSimple(self):
        fader = ColourFader({"red": 255, "green": 255, "blue": 255}, {"red": 0, "green": 0, "blue": 0})

        fadedColours = fader.fade(255)

        self.assertEquals(255, len(fadedColours))

        self.assertEquals(1/255, fadedColours[254]['red'])

    def test_fadeComplex(self):
        fader = ColourFader({"red": 100, "green": 100, "blue": 100}, {"red": 0, "green": 0, "blue": 0})

        fadedColours = fader.fade(10)

        self.assertEquals(10, len(fadedColours))

    def test_emptyDataPoints(self):
        fader = ColourFader({"red": 100, "green": 100, "blue": 100}, {"red": 0, "green": 0, "blue": 0})

        fadedColours = fader.fade(0)

        self.assertEquals(2, len(fadedColours))
        self.assertTrue(fadedColours[0]['red']<1.0)

        fadedColours = fader.fade(1)
        self.assertEquals(2, len(fadedColours))


        fadedColours = fader.fade(2)
        self.assertEquals(2, len(fadedColours))


