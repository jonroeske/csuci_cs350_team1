from Handlers.camperHandler import summerCamp

from Handlers.guiHandler import *

# TODO - REFORMATTED
def viewCamperApplication():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    clearScreen()
    printCamperGUI(camper, attribute="applicationStatus", topBracket=True, bottomBracket=True)
    showPrompt("Press 'Enter' to Return!", bottomBracket=True)
    camperSubMenu()


# TODO - REFORMATTED
def acceptCamperApplication():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    while True:
        clearScreen()

        printCamperGUI(camper, attribute="applicationStatus", topBracket=True, bottomBracket=True)

        confirmation = showPrompt("Are you sure you would like to accept this camper?", prompt= '"Y" for Yes, "N" for No', bottomBracket=True)

        if confirmation == 'Y':
            break
        elif confirmation == 'N':
            camperSubMenu()
            showMessage("Action aborted.", bottomBracket=True)
            return
        else:
            showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    clearScreen()

    if camper.getBalance() > 0:
        printCamperGUI(camper, attribute="balance", topBracket=True, bottomBracket=True)
        showMessage('Camper balance must be 0!')


    else:
        camper.setAppStatus(1)

        showMessage("Camper has been accepted!",topBracket=True, bottomBracket=True)
        printCamperGUI(camper, attribute="applicationStatus")

    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    camperSubMenu()


# TODO - REFORMATTED
def rejectCamperApplication():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    while True:
        clearScreen()

        printCamperGUI(camper, attribute="applicationStatus", topBracket=True, bottomBracket=True)

        confirmation = showPrompt("Are you sure you would like to reject this camper?", prompt= '"Y" for Yes, "N" for No', bottomBracket=True)

        if confirmation == 'Y':
            break
        elif confirmation == 'N':
            camperSubMenu()
            showMessage("Action aborted.", bottomBracket=True)
            return
        else:
            showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    clearScreen()

    camper.setAppStatus(2)

    showMessage("Camper has been rejected!",topBracket=True, bottomBracket=True)
    printCamperGUI(camper, attribute="applicationStatus")

    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    camperSubMenu()