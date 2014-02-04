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

appHeight = 200
appWidth = 320

gFormatter = "{} {:.2f}"

def doRender(deltaT):
    global x,y,z, xG, yG, zG, gFormatter
    try:
        x, y, z=ac.getCarState(0,acsys.CS.AccG)

        ac.setText(xG, "{:.2f}".format(x))
        ac.setText(yG,"{:.2f}".format(y))
        ac.setText(zG, gFormatter.format("z", z))

    except Exception as e:
        ac.log(str(e))

def acMain(ac_version):
    global xG, yG, zG, versionLabel

    appWindow=ac.newApp("Traction Circle")
    ac.setSize(appWindow, appWidth, appHeight)
    ac.drawBorder(appWindow,0)

    versionLabel=ac.addLabel(appWindow, "Hello World!")

    xG=ac.addLabel(appWindow, "0.0")
    yG=ac.addLabel(appWindow, "0.0")
    zG=ac.addLabel(appWindow, "0.0")

    ac.setPosition(xG, 10, appHeight-20)
    ac.setPosition(yG, 50, appHeight-20)
    ac.setPosition(zG, 100, appHeight-20)
    ac.setPosition(versionLabel, 50, appHeight - 50)


    ac.addRenderCallback(appWindow, doRender)
    return "Traction Circle"
