import unittest

from traction_circle_model import TractionCircleModel


class MyTest(unittest.TestCase):
    def test_firstTest(self):
        tc1 = TractionCircleModel()

        tc1.addDataPoint(1.0, 0.8, 0.1)

        self.assertEquals(1.0, tc1.dataPoints()[0]["x"])

