from unittest import TestCase
from colourfader import ColourFader


class TestColourFader(TestCase):
    def test_emptyRange(self):
        fader = ColourFader((0, ), (10, ))
        # all these cases (<2 slots) are corrected to the same case (=2 slots):
        self.assertEqual(2, len(fader.fade(nSlots=-2)))
        self.assertEqual(2, len(fader.fade(nSlots=-1)))
        self.assertEqual(2, len(fader.fade(nSlots= 0)))
        self.assertEqual(2, len(fader.fade(nSlots= 1)))
        self.assertEqual(2, len(fader.fade(nSlots= 2)))

        self.assertEqual(fader.fade(0), fader.fade(-1), fader.fade(-2))
        self.assertEqual(fader.fade(0), fader.fade( 1), fader.fade( 2))

    def test_normalRange(self):
        fader = ColourFader((0, ), (10, ))
        self.assertEqual(   2, len(fader.fade(   2))) # min. normal range
        self.assertEqual( 100, len(fader.fade( 100)))
        self.assertEqual(1000, len(fader.fade(1000)))

    def test_signedValues(self):
        self.assertEqual(ColourFader((  0,), ( 10,)).fade(3), [(  0,), ( 5,), ( 10,)]) # increasing
        self.assertEqual(ColourFader((  0,), (-10,)).fade(3), [(  0,), (-5,), (-10,)]) # decreasing

        self.assertEqual(ColourFader((-10,), ( 10,)).fade(3), [(-10,), ( 0,), ( 10,)]) # increasing across zero
        self.assertEqual(ColourFader(( 10,), (-10,)).fade(3), [( 10,), ( 0,), (-10,)]) # decreasing across zero

    def test_manyComponents(self):
        # 1 colour components (e.g. greyscale)
        self.assertEqual(
            ColourFader((0,),       (2,)).fade(3),
            [           (0,), (1,), (2,)])

        # 2 colour components (e.g. sepia toning)
        self.assertEqual(
            ColourFader((0, 10),          (2, 20)).fade(3),
            [           (0, 10), (1, 15), (2, 20)])

        # 3 colour components (e.g. RGB)
        self.assertEqual(
            ColourFader((0, 10, 100),               (2, 20, 200)).fade(3),
            [           (0, 10, 100), (1, 15, 150), (2, 20, 200)])

        # 4 colour components (e.g. RGBA)
        self.assertEqual(
            ColourFader((0, 10, 100, 1000),                     (2, 20, 200, 2000)).fade(3),
            [           (0, 10, 100, 1000), (1, 15, 150, 1500), (2, 20, 200, 2000)])

