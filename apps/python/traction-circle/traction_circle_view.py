import ac


class TractionCircleView:
    def __init__(self, window, tractionCircleModel):
        self.label = ac.addLabel(window, '')
        self.tractionCircleModel = tractionCircleModel

    def render(self):
        try:
            self.label.setText("{0}".format(len(self.tractionCircleModel.dataPoints())))
        except Exception as e:
            ac.log(str(e))
