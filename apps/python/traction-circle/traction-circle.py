import ac
import acsys

appWindow=0
versionLabel=0
xG=0
yG=0
zG=0
x=0
y=0
z=0

def doRender(deltaT):
    global x,y,z, xG, yG, zG
    try:
        x, y, z=ac.getCarState(0,acsys.CS.AccG)

        ac.setText(xG,"{0}g".format(x))
        ac.setText(yG,"{0}g".format(y))
        ac.setText(zG,"{0}g".format(z))

    except Exception as e:
        ac.log(str(e))

def acMain(ac_version):
    global xG, yG, zG, versionLabel

    appWindow=ac.newApp("Traction Circle")
    ac.setSize(appWindow, 320,160)
    ac.drawBorder(appWindow,0)

    versionLabel=ac.addLabel(appWindow, "Hello World!")

    xG=ac.addLabel(appWindow, "0.0")
    yG=ac.addLabel(appWindow, "0.0")
    zG=ac.addLabel(appWindow, "0.0")

    ac.setPosition(xG, 50, 20)
    ac.setPosition(yG, 50, 50)
    ac.setPosition(zG, 50, 70)
    ac.setPosition(versionLabel, 50, 100)


    ac.addRenderCallback(appWindow, doRender)
    return "Traction Circle"
