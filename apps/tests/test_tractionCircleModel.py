from unittest import TestCase
import time
from unittest.mock import MagicMock

from traction_circle_model import TractionCircleModel


__author__ = 'psmith'


class TestTractionCircleModel(TestCase):
    def test_addDataPoint(self):

        mockedTime = time
        mockedTime.time = MagicMock(return_value=5)

        self.tcm = TractionCircleModel(mockedTime)

        self.tcm.addDataPoint(1, 2, 3)

        self.assertEqual(self.tcm.dataPoints()[0]["time"], 5)

    def test_filterDataPoints(self):
        mockedTime = time
        mockedTime.time = MagicMock(return_value=5)

        tcm = TractionCircleModel(mockedTime)

        tcm.addDataPoint(1,2,3)

        self.assertEqual(1, len(tcm.dataPoints()))
        tcm.filterPoints(10)

        self.assertEqual(0, len(tcm.dataPoints()))

        # check we can still add to the filtered structure!
        tcm.addDataPoint(9,9,9)


