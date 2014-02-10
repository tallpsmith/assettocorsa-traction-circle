import ac


class TractionCircleView:
    def __init__(self, window, tractionCircleModel):
        self.label = ac.addLabel(window, '')
        ac.setPosition(self.label, 100, 100)

        self.tractionCircleModel = tractionCircleModel

    def render(self):
        try:
            #self.label.setText("{0}".format(len(self.tractionCircleModel.dataPoints())))
            ac.setText(self.label, 'Rendering!')
        except Exception as e:
            ac.log(str(e))
