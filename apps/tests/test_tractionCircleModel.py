from unittest import TestCase
import time
from unittest.mock import MagicMock

from traction_circle_model import TractionCircleModel


__author__ = 'psmith'


class TestTractionCircleModel(TestCase):
    def test_addDataPoint(self):
        mockedTime = time
        mockedTime.time = MagicMock(return_value=5)

        tcm = TractionCircleModel(mockedTime)

        tcm.addDataPoint(1, 2, 3)

        self.assertEquals(tcm.dataPoints()[0]["time"], 5)


