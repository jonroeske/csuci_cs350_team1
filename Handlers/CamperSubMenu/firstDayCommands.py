from Handlers.camperHandler import summerCamp
from Handlers.guiHandler import *

def viewAcceptanceNoticeStatus():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    printCamperGUI(camper, attribute="appNotice", bottomBracket=True)
    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    camperSubMenu()

