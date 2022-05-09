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


def fillOutForms():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return


    if camper.getMaterials() is None:
        camper.setMaterials(Materials())


    if camper.getMaterials().getMedical() is False:
        while True:
            clearScreen()

            confirmation = showPrompt("Is this information correct?", prompt= '"Y" for Yes, "N" for No', bottomBracket=True)

            if confirmation == 'Y':
                summerCamp.insertCamper(newCamper)
                summerCamp.sortList(parameter="name")

                mainMenu()
                showMessage("Camper successfully created!", bottomBracket=True)
                return
            elif confirmation == 'N':
                break
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)