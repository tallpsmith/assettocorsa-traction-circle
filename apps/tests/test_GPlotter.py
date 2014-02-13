from unittest import TestCase

from traction_circle_g_plotter import GPlotter


class TestGPlotter(TestCase):
    def test_plotAll(self):
        plotter = GPlotter(320, 200, 2, 2)
        dataPoints = [{"x": 1, "z": 1}, {"x": 1, "z": 1}]

        allPlots = plotter.plotAll(dataPoints)

        self.assertEquals(2, len(allPlots))
        self.assertTrue(allPlots[0][0] < 320 and allPlots[0][0] > 0,
                        "Plotted x values must be between the range -160:160 " + str(allPlots))


    def test_halfBreakingNoCornering(self):
        plotter = GPlotter(320, 200, 2, 2)

        x, y = plotter.plotG(0, 1)

        self.assertEquals(160, x)
        self.assertEquals(150, y)

    def test_centerPoint(self):
        plotter = GPlotter(320, 200, 2, 2)

        x, y = plotter.plotG(0, 0)
        self.assertEquals(160, x)
        self.assertEquals(100, y)



