from unittest import TestCase
from traction_circle_g_plotter import GPlotter

class TestGPlotter(TestCase):
    def test_halfBreakingNoCornering(self):
        plotter =  GPlotter(320,200, 2, 2)

        x,y = plotter.plotG(0, 1)

        self.assertEquals(160, x)
        self.assertEquals(150, y)

    def test_centerPoint(self):

        plotter =  GPlotter(320,200, 2, 2)

        x,y = plotter.plotG(0, 0)
        self.assertEquals(160, x)
        self.assertEquals(100, y)



