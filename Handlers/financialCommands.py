import Handlers.camperHandler
from Handlers.camperHandler import summerCamp

from Objects.values import STATUS_CODES

from GUI.guiHandler import camperSubMenu, clearScreen, showPrompt, showMessage
from GUI.camperCommandsGUI import printCamperGUI


# TODO - REFORMATTED
def viewCamperBalance():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    clearScreen()
    printCamperGUI(camper, attribute="balance", topBracket=True, bottomBracket=True)
    showPrompt("Press 'Enter' to Return!", bottomBracket=True)
    camperSubMenu()


# TODO - REFORMATTED
def raiseCamperBalance():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    while True:
        clearScreen()

        printCamperGUI(camper, attribute="balance", topBracket=True, bottomBracket=True)

        try:
            amount = float(showPrompt("How much to raise balance?", prompt="($1000 is maximum balance!)", bottomBracket=True))
        except ValueError:
            showMessage("Invalid input!", bottomBracket=True, wait=2)
            continue

        clearScreen()
        showMessage("Old balance:", topBracket=True, bottomBracket=True)
        printCamperGUI(camper, attribute="balance")

        amount = camper.getBalance() + amount

        if amount > 1000:
            camper.setBalance(1000.00)
        else:
            camper.setBalance(amount)
        break


    showMessage("New balance:",topBracket=True, bottomBracket=True)
    printCamperGUI(camper, attribute="balance")

    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    camperSubMenu()


# TODO - REFORMATTED
def reduceCamperBalance():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    while True:
        clearScreen()

        printCamperGUI(camper, attribute="balance", topBracket=True, bottomBracket=True)

        try:
            amount = float(showPrompt("How much to reduce balance?", prompt="($0 is minimum balance!)", bottomBracket=True))
        except ValueError:
            showMessage("Invalid input!", bottomBracket=True, wait=2)
            continue

        clearScreen()
        showMessage("Old balance:", topBracket=True, bottomBracket=True)
        printCamperGUI(camper, attribute="balance")

        amount = camper.getBalance() - amount

        if amount < 0:
            camper.setBalance(0)
        else:
            camper.setBalance(amount)
        break


    showMessage("New balance:",topBracket=True, bottomBracket=True)
    printCamperGUI(camper, attribute="balance")

    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    camperSubMenu()


# TODO - REFORMATTED
def clearCamperBalance():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    while True:
        clearScreen()

        printCamperGUI(camper, attribute="balance", topBracket=True, bottomBracket=True)
        confirmation = showPrompt("Are you sure you want to clear balance?", prompt= '"Y" for Yes, "N" for No', bottomBracket=True)

        if confirmation == 'Y':
            break
        elif confirmation == 'N':
            camperSubMenu()
            showMessage("Balance clear aborted", bottomBracket=True)
            return
        else:
            showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    clearScreen()
    showMessage("Old balance:", topBracket=True, bottomBracket=True)
    printCamperGUI(camper, attribute="balance")

    camper.setBalance(0)

    showMessage("New balance:",topBracket=True, bottomBracket=True)
    printCamperGUI(camper, attribute="balance")

    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    camperSubMenu()
