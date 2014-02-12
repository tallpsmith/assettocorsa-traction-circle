import ac
from traction_circle_g_plotter import GPlotter
from traction_circle_model import TractionCircleModel
from traction_circle_view import TractionCircleView
from traction_circle_updater import TractionCircleUpdater
from assettocorsa import AssettoCorsa

appHeight = 200
appWidth = 320
updater = 0
maxG = 2


def acMain(ac_version):
    global updater
    appWindow = ac.newApp("Traction Circle")
    ac.setSize(appWindow, appWidth, appHeight)
    ac.drawBorder(appWindow, 0)

    try:
        model = TractionCircleModel()
        assetto_corsa = AssettoCorsa()
        gPlotter = GPlotter(appWidth, appHeight, maxG, maxG)
        view = TractionCircleView(appWindow, model, gPlotter)
        updater = TractionCircleUpdater(assetto_corsa, view, model)

        ac.addRenderCallback(appWindow, doUpdate)
    except Exception as e:
        ac.log(str(e))
    return "Traction Circle"

def doUpdate(deltaT):
    global updater

    updater.doUpdate(deltaT)

