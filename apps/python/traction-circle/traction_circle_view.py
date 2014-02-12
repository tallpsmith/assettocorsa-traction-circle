import ac


class TractionCircleView:
    def __init__(self, window, tractionCircleModel, gPlotter):
        self.WIDTH = 2.0
        self.HEIGHT = 2.0

        self.gPlotter = gPlotter
        self.label = ac.addLabel(window, '')
        ac.setPosition(self.label, 100, 100)

        self.tractionCircleModel = tractionCircleModel

    def render(self):
        try:
            ac.glColor3f(77, 184, 73)
            for dataPoint in self.tractionCircleModel.dataPoints():
                x, y = self.gPlotter.plotG(dataPoint['x'], dataPoint['z'])
                ac.glQuad(x, y, self.WIDTH, self.HEIGHT)

            ac.setText(self.label, "{0}".format(len(self.tractionCircleModel.dataPoints())))
        except Exception as e:
            ac.log(str(e))
