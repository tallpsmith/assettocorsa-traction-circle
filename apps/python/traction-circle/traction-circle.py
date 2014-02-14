import ac
import traceback
from traction_circle_g_plotter import GPlotter
from traction_circle_model import TractionCircleModel
from traction_circle_view import TractionCircleView
from traction_circle_updater import TractionCircleUpdater
from assettocorsa import AssettoCorsa

appHeight = 200
appWidth = 320
maxG = 2

updater = 0
numSecondsSpinner = 0


def acMain(ac_version):
    global updater, appHeight, appWidth, appWindow, numSecondsSpinner
    appWindow = ac.newApp("Traction Circle")
    ac.setSize(appWindow, appWidth, appHeight)
    ac.drawBorder(appWindow, 0)

    try:
        model = TractionCircleModel()
        assetto_corsa = AssettoCorsa()

        ac.log("Beginning Spinner creation")
        maxTimeSpan = 5
        numSecondsSpinner = ac.addSpinner(appWindow, 'Time Span')
        ac.setPosition(numSecondsSpinner, 0, appHeight - 20)
        ac.setRange(numSecondsSpinner, 1, 10)
        ac.setValue(numSecondsSpinner, maxTimeSpan)
        ac.addOnValueChangeListener(numSecondsSpinner, updateMaxTimeRange)

        ac.log("Finished Spinner")
        gPlotter = GPlotter(appWidth, appHeight, maxG, maxG)
        view = TractionCircleView(appWindow, model, gPlotter)
        updater = TractionCircleUpdater(assetto_corsa, view, model, maxTimeRange=maxTimeSpan)

        ac.addRenderCallback(appWindow, doUpdate)
    except Exception as e:
        ac.log(str(traceback.format_exc()))

    return "Traction Circle"


def doUpdate(deltaT):
    global updater

    updater.doUpdate(deltaT)


def updateMaxTimeRange(value):
    global updater
    ac.log("Setting Num Seconds to {0}".format(str(value)))
    updater.setMaxTimeRange(value)

