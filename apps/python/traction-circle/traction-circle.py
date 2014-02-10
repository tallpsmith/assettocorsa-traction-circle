import ac
from traction_circle_model import TractionCircleModel
from traction_circle_view import TractionCircleView
from traction_circle_updater import TractionCircleUpdater
from assettocorsa import AssettoCorsa

appHeight = 200
appWidth = 320


def acMain(ac_version):
    appWindow = ac.newApp("Traction Circle")
    ac.setSize(appWindow, appWidth, appHeight)
    ac.drawBorder(appWindow, 0)

    model = TractionCircleModel()

    assetto_corsa = AssettoCorsa()
    view = TractionCircleView(appWindow, model)
    updater = TractionCircleUpdater(assetto_corsa, view, model)

    ac.addRenderCallback(appWindow, updater.doUpdate)
    return "Traction Circle"
