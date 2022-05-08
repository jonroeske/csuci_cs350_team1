import Handlers.camperHandler
from Handlers.camperHandler import summerCamp

from Objects.camper import Camper
from Objects.values import *

from GUI.guiHandler import clearScreen, mainMenu, showPrompt, showMessage
from GUI.camperCommandsGUI import printCamperGUI

def createCamper():
    if not any(elem == "" for elem in summerCamp.getAllCampers()):
        mainMenu()
        print('| No more slots available!                     |')
        print('|----------------------------------------------|')
        return

    newCamper = Camper()

    clearScreen()
    name = showPrompt("Please insert camper name:", prompt= "(First + Last)", topBracket=True, bottomBracket=True)

    if summerCamp.searchCamper(name) != STATUS_CODES["NO_CAMPER"]:
        mainMenu()
        showMessage("That camper already exists!", bottomBracket=True)
        return

    newCamper.name = name

    while True:
        clearScreen()
        try:
            newCamper.age = int(showPrompt("Please insert camper age:", prompt="(9 - 18)", topBracket=True, bottomBracket=True))
        except ValueError:
            showMessage("Invalid input!", bottomBracket=True, wait=2)
            continue

        if 9 <= int(newCamper.age) <= 18:
            break
        else:
            showMessage("Applicant must be between 9 and 18 years old.", bottomBracket=True, wait=2)

    while True:
        clearScreen()
        newCamper.gender = showPrompt('Please insert camper gender:', prompt='"M" or "F"', bottomBracket=True, topBracket=True).upper()
        if newCamper.gender == 'F' or newCamper.gender == 'M':
            break
        else:
            showMessage('Applicant must be between "M" or "F"', bottomBracket=True, wait=2)

    clearScreen()
    newCamper.address = showPrompt("Please insert camper home address:", topBracket=True, bottomBracket=True)

    while True:
        clearScreen()

        printCamperGUI(newCamper, camperCreation= True, topBracket=True, bottomBracket=True)
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

    while True:
        confirmation = showPrompt("Would you like to try again?", prompt='"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)
        if confirmation == 'Y':
            break
        elif confirmation == 'N':
            mainMenu()
            return
        else:
            showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    createCamper()


# TODO - REFORMATTED
def deleteCamper():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt= "(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        mainMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    while True:
        clearScreen()
        printCamperGUI(camper, detailed=True, topBracket=True, bottomBracket=True)

        confirmation = showPrompt("Are you sure you want to delete this camper?",
                                      prompt='"Y" for Yes, "N" for No', bottomBracket=True)
        if confirmation == 'Y':
            # TODO - ADD PARTNER LOGIC

            camper.setSession(False)
            camper.setBunkhouse(False)
            camper.setTribe(False)

            summerCamp.updateCamper(camper, remove=True)
            mainMenu()
            showMessage("Camper deletion successful", bottomBracket=True)
            return
        elif confirmation == 'N':
            mainMenu()
            showMessage("Camper deletion aborted", bottomBracket=True)
            return
        else:
            showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)


# TODO - REFORMATTED
def printCamper():
    if not any(elem != "" for elem in summerCamp.getAllCampers()):
        mainMenu()
        showMessage("There are currently no campers!", bottomBracket=True)
        return

    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)
    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        mainMenu()
        showMessage("That camper doesn't exist!", bottomBracket=True)

    else:
        printCamperGUI(camper, detailed=True, topBracket=True, bottomBracket=True)
        showPrompt("Press 'Enter' to Return!", bottomBracket=True)
        mainMenu()


# TODO - REFORMATTED
def printAllCampers():
    if not any(elem != "" for elem in summerCamp.getAllCampers()):
       mainMenu()
       showMessage("There are currently no campers!", bottomBracket=True)
       return

    summerCamp.sortList(parameter="name")

    clearScreen()
    print('|----------------------------------------------|')
    print(f'   Amount: {sum(elem != "" for elem in summerCamp.getAllCampers()):}')

    genders = summerCamp.countGender()
    print(f'   Composition: {genders[0]} Male(s), {genders[1]} Female(s) ')

    for camper in summerCamp.getAllCampers():
        if isinstance(camper, Camper):
            printCamperGUI(camper, simple=True)

    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    mainMenu()
