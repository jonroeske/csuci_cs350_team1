from Handlers.camperHandler import summerCamp
from Handlers.CamperSubMenu.assignmentCommands import assignCamperToSession

from Handlers.guiHandler import *

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


def acceptCamperApplication():
    locations = [JUNE_SESSION_DATE, JULY_SESSION_DATE, AUGUST_SESSION_DATE]

    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    monthDifference = abs((((Objects.values.TODAYS_DATE - locations[camper.getSession()]).days)/7)/4)

    if monthDifference < 2:
        showMessage("Applications are due two months in advance of session!", bottomBracket=True)
        printCamperGUI(camper, attribute="sessionDate", bottomBracket=True)
        showPrompt("Press 'Enter' to Return!", bottomBracket=True)
        camperSubMenu()
        return

    elif monthDifference > 8:
        showMessage("Applications are within eight months in advance of session!", bottomBracket=True)
        printCamperGUI(camper, attribute="sessionDate", bottomBracket=True)
        showPrompt("Press 'Enter' to Return!", bottomBracket=True)
        camperSubMenu()
        return

    elif camper.getSession() is False:
        showMessage("Camper must be assigned to a session before application review!", bottomBracket=True)
        printCamperGUI(camper, attribute="session", bottomBracket=True)
        showPrompt("Press 'Enter' to Return!", bottomBracket=True)
        camperSubMenu()
        return
    elif camper.getBalance() > 0:
        showMessage("Camper must not have any outstanding balance!", bottomBracket=True)
        printCamperGUI(camper, attribute="session", bottomBracket=True)
        showPrompt("Press 'Enter' to Return!", bottomBracket=True)
        camperSubMenu()
        return


    while True:
        clearScreen()

        printCamperGUI(camper, attribute="applicationStatus", topBracket=True, bottomBracket=True)

        confirmation = showPrompt(["Are you sure you would like to accept this camper?",
                                  "This will automatically send an acceptance notice to the camper today!"], prompt= '"Y" for Yes, "N" for No', bottomBracket=True)

        if confirmation == 'Y':
            break
        elif confirmation == 'N':
            camperSubMenu()
            showMessage("Action aborted.", bottomBracket=True)
            return
        else:
            showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    clearScreen()
    camper.setAppStatus(1)
    camper.setAppNoticeIsSent(True)
    camper.setDateAppNoticeSent(Objects.values.TODAYS_DATE)

    summerCamp.updateCamper(camper)

    showMessage("Camper has been accepted!",topBracket=True, bottomBracket=True)
    printCamperGUI(camper, attribute="applicationStatus")

    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    camperSubMenu()


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

        confirmation = showPrompt(["Are you sure you would like to reject this camper?"
                                    "If assigned, this will clear Camper's session, bunkhouse, and Tribe!"],
                                  prompt= '"Y" for Yes, "N" for No', bottomBracket=True)

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
    camper.setAppNoticeIsSent(False)
    camper.setDateAppNoticeSent(None)

    camper.setSession(False)
    camper.setBunkhouse(False)
    camper.setTribe(False)

    summerCamp.updateCamper(camper)

    showMessage("Camper has been rejected!",topBracket=True, bottomBracket=True)
    printCamperGUI(camper, attribute="applicationStatus")

    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    camperSubMenu()
