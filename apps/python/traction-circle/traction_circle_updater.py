class TractionCircleUpdater:
    def __init__(self, AC, view, model):
        self.AC = AC
        self.view = view
        self.model = model

    def doUpdate(self, deltaT):
        #x, y, z = self.AC.getAccelerations()

        #self.model.addDataPoint(x, y, z)
        self.view.render()
        #pass
