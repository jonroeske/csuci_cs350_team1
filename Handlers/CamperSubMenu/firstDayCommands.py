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

    elif camper.getAppStatus() != 1:
        printCamperGUI(camper, attribute="applicationStatus", topBracket=True, bottomBracket=True)
        showMessage('Camper must be accepted!')
        showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
        camperSubMenu()
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
    elif camper.getAppStatus() != 1:
        printCamperGUI(camper, attribute="applicationStatus", topBracket=True, bottomBracket=True)
        showMessage('Camper must be accepted!')
        showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
        camperSubMenu()
        return

    if camper.getMaterials() is None:
        camper.setMaterials(Materials())

    # FORMS

    if camper.getMaterials().getMedical() is False:
        while True:
            clearScreen()

            confirmation = showPrompt(["Verify camper's medical paperwork.",
                                      "Is the camper's medical paperwork verified and accurate?"], prompt= '"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)

            if confirmation == 'Y':
                camper.getMaterials().setMedical(True)
                break
            elif confirmation == 'N':
                showMessage("Medical paperwork must be completed before the camper can be checked in!", bottomBracket=True)
                showPrompt("Press 'Enter' to Continue!", bottomBracket=True)
                break
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    if camper.getMaterials().getLegal() is False:
        while True:
            clearScreen()

            confirmation = showPrompt(["Verify camper's legal release paperwork.",
                                      "Is the camper's legal release verified and accurate?"], prompt= '"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)

            if confirmation == 'Y':
                camper.getMaterials().setLegal(True)
                break
            elif confirmation == 'N':
                showMessage("Legal release paperwork must be completed before the camper can be checked in!", bottomBracket=True)
                showPrompt("Press 'Enter' to Continue!", bottomBracket=True)
                break
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    if camper.getMaterials().getEmergencyContacts() is False:
        while True:
            clearScreen()

            confirmation = showPrompt(["Verify camper's emergency contacts.",
                                      "Are the camper's emergency contacts verified and accurate?"], prompt= '"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)

            if confirmation == 'Y':
                camper.getMaterials().setEmergencyContacts(True)
                break
            elif confirmation == 'N':
                showMessage("Emergency contacts must be completed before the camper can be checked in!", bottomBracket=True)
                showPrompt("Press 'Enter' to Continue!", bottomBracket=True)
                break
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    # EQUIPMENT

    if camper.getMaterials().getHelmet() is False:
        while True:
            clearScreen()

            confirmation = showPrompt("Does the camper have an acceptable, fitting helmet?"
                                      , prompt='"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)

            if confirmation == 'Y':
                camper.getMaterials().setHelmet(True)
                break
            elif confirmation == 'N':
                showMessage(["The camper must have a helmet before they can be checked in!",
                             " Helmets can be bought from the Camp Store."], bottomBracket=True)
                showPrompt("Press 'Enter' to Continue!", bottomBracket=True)
                break
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    if camper.getMaterials().getBoots() is False:
        while True:
            clearScreen()

            confirmation = showPrompt("Does the camper have a pair of appropriate, fitting boots?"
                                      , prompt='"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)

            if confirmation == 'Y':
                camper.getMaterials().setBoots(True)
                break
            elif confirmation == 'N':
                showMessage(["The camper must have boots before they can be checked in!",
                             " Boots can be bought from the Camp Store."], bottomBracket=True)
                showPrompt("Press 'Enter' to Continue!", bottomBracket=True)
                break
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    if camper.getMaterials().getSleepingBag() is False:
        while True:
            clearScreen()

            confirmation = showPrompt("Does the camper have an appropriate sleeping bag?"
                                      , prompt='"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)

            if confirmation == 'Y':
                camper.getMaterials().setSleepingBag(True)
                break
            elif confirmation == 'N':
                showMessage(["The camper must have a sleeping bag before they can be checked in!",
                             " Sleeping bags can be bought from the Camp Store."], bottomBracket=True)
                showPrompt("Press 'Enter' to Continue!", bottomBracket=True)
                break
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)


    # SUPPLIES

    if camper.getMaterials().getWaterBottle() is False:
        while True:
            clearScreen()

            confirmation = showPrompt("Does the camper have at least one water bottle?"
                                      , prompt='"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)

            if confirmation == 'Y':
                camper.getMaterials().setWaterBottle(True)
                break
            elif confirmation == 'N':
                showMessage(["The camper must have at least one water bottle before they can be checked in!",
                             " Water bottles can be bought from the Camp Store."], bottomBracket=True)
                showPrompt("Press 'Enter' to Continue!", bottomBracket=True)
                break
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    if camper.getMaterials().getSunscreen() is False:
        while True:
            clearScreen()

            confirmation = showPrompt("Does the camper have a bottle of sunscreen?"
                                      , prompt='"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)

            if confirmation == 'Y':
                camper.getMaterials().setSunscreen(True)
                break
            elif confirmation == 'N':
                showMessage(["The camper must have sunscreen before they can be checked in!",
                             " Bottles of sunscreen can be bought from the Camp Store."], bottomBracket=True)
                showPrompt("Press 'Enter' to Continue!", bottomBracket=True)
                break
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    if camper.getMaterials().getBugSpray() is False:
        while True:
            clearScreen()

            confirmation = showPrompt("Does the camper have a bottle of bug spray?"
                                      , prompt='"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)

            if confirmation == 'Y':
                camper.getMaterials().setBugSpray(True)
                break
            elif confirmation == 'N':
                showMessage(["The camper must have bug spray before they can be checked in!",
                             " Bug spray can be bought from the Camp Store."], bottomBracket=True)
                showPrompt("Press 'Enter' to Continue!", bottomBracket=True)
                break
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    clearScreen()
    printCamperGUI(camper, attribute="materials", topBracket=True, bottomBracket=True)
    showPrompt("Press 'Enter' to Continue!", bottomBracket=True)
    camperSubMenu()


def checkInCamper():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return
    elif camper.getAppStatus() != 1:
        printCamperGUI(camper, attribute="applicationStatus", topBracket=True, bottomBracket=True)
        showMessage('Camper must be accepted!')
        showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
        camperSubMenu()
        return
    elif camper.getMaterials() is None or camper.getMaterials().getCompletedForms() is False:
        printCamperGUI(camper, attribute="materials", topBracket=True, bottomBracket=True)
        showMessage('Camper have completed their required forms!')
        showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
        camperSubMenu()
        return
    elif camper.getBalance() > 0:
        printCamperGUI(camper, attribute="balance", topBracket=True, bottomBracket=True)
        showMessage('Camper must have no outstanding balance!')
        showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
        camperSubMenu()
        return

    clearScreen()

    camper.setCheckedIn(True)

    showMessage(["Camper has been checked in!",
                 " You may now assign the camper to bunkhouses/tribes!"], topBracket=True, bottomBracket=True)
    printCamperGUI(camper, attribute="checkedIn")

    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    camperSubMenu()