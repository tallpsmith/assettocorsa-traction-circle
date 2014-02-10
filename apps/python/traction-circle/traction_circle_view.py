import ac


class TractionCircleView:
    def __init__(self, window, tractionCircleModel):
        self.label = ac.addLabel(window, '')
        ac.setPosition(self.label, 100, 100)

        self.tractionCircleModel = tractionCircleModel

    def render(self):
        try:
            ac.setText(self.label, "{0}".format(len(self.tractionCircleModel.dataPoints())))
        except Exception as e:
            ac.log(str(e))
