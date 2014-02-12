import ac


class TractionCircleView:
    RED = 77.0/255
    GREEN = 184.0/255
    BLUE = 73.0 / 255

    FINAL_COLOUR = {31,77,31}

    def __init__(self, window, tractionCircleModel, gPlotter):
        self.WIDTH = 2.0
        self.HEIGHT = 2.0

        self.gPlotter = gPlotter
        self.label = ac.addLabel(window, '')
        ac.setPosition(self.label, 100, 100)

        self.tractionCircleModel = tractionCircleModel

    def render(self):
        try:
            ac.glColor3f(self.RED, self.GREEN, self.BLUE)
            for dataPoint in self.tractionCircleModel.dataPoints():
                x, y = self.gPlotter.plotG(dataPoint['x'], dataPoint['z'])
                ac.glQuad(x, y, self.WIDTH, self.HEIGHT)

            ac.setText(self.label, "{0}".format(len(self.tractionCircleModel.dataPoints())))
        except Exception as e:
            ac.log(str(e))
