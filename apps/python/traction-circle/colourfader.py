#import ac

class ColourFader:
    def __init__(self, startColour, endColour):
        self.startColour = startColour
        self.colourRange = list([s-e for s,e in zip(startColour, endColour)]) # that is: startColour - endColour

    def fade(self, nSlots):
        def fadeSlot(progress):
            return tuple( (component-self.colourRange[nComponent]*progress for nComponent,component in enumerate(self.startColour)) )

        nSlots = max(nSlots, 2)
        return [fadeSlot(nSlot/nSlots) for nSlot in range(nSlots)]
