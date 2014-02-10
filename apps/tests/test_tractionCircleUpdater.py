from unittest import TestCase
from unittest.mock import Mock

from traction_circle_updater import TractionCircleUpdater


class TestTractionCircleUpdater(TestCase):
    def test_doUpdate(self):
        view = Mock()
        model = Mock()
        AC = Mock()

        AC.getAccelerations = Mock(return_value=[1, 2, 3])

        updater = TractionCircleUpdater(AC, view, model)
        updater.doUpdate(1)

        model.addDataPoint.assert_called_with(1, 2, 3)

        AC.getAccelerations.assert_called_with()
        view.render.assert_called_with()




