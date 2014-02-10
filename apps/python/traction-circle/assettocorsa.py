import ac
import acsys


class AssettoCorsa():
    def getAccelerations(self):
        return ac.getCarState(0, acsys.CS.AccG)