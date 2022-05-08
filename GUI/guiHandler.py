import os, time

from Objects.camper import *

versionNumber = "Build May052022"


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def mainMenu():
    clearScreen()
    print('|----------------Camp Clerk CLI----------------|')
    print('| Main Menu                                    |')
    print('| (0)  Shutdown                                |')
    print('| (1)  Credits                                 |')
    print('| (2)  Show Version                            |')
    print('|----------------------------------------------|')
    print('| Campers                                      |')
    print('| (3)  Create New Camper                       |')
    print('| (4)  Delete Camper                           |')
    print('| (5)  Camper Actions                          |')
    print('| (6)  View Camper                             |')
    print('| (7)  View All Campers                        |')
    print('|----------------------------------------------|')
    print('| Sessions                                     |')
    print('| (8)  View Sessions                           |')
    print('| (9)  View Bunkhouse                          |')
    print('| (10) View Tribes                             |')
    print('|----------------------------------------------|')
    print('| Automation                                   |')
    print('| (11) Set Every Balance                       |')
    print('| (12) Set All Applications                    |')
    print('| (13) Auto-Assign All Sessions                |')
    print('| (14) Auto-Assign All Bunkhouses              |')
    print('| (15) Auto-Assign All Tribes                  |')
    print('|----------------------------------------------|')
    print('| DEBUG                                        |')
    print('| (16) Reset and Create All Campers            |')
    print('| (17) Reset All Campers                       |')
    #print('| (18) Clear All Sessions                      |')
    #print('| (19) Clear All Bunkhouses                    |')
    #print('| (20) Clear All Tribes                        |')
    print('|----------------------------------------------|')


def camperSubMenu():
    clearScreen()
    print('|----------------Camp Clerk CLI----------------|')
    print('| Financial                                    |')
    print('| (0)  View Camper Balance                     |')
    print('| (1)  Raise Camper Balance                    |')
    print('| (2)  Reduce Camper Balance                   |')
    print('| (3)  Clear Camper Balance                    |')
    print('|----------------------------------------------|')
    print('| Application                                  |')
    print('| (4)  View Application Status                 |')
    print('| (5)  Accept Application                      |')
    print('| (6)  Decline Application                     |')
    print('|----------------------------------------------|')
    print('| Assignment                                   |')
    print('| (7)  Assign Session                          |')
    print('| (8)  Assign Bunkhouse                        |')
    print('| (9)  Assign Tribe                            |')
    print('| (10) Process Pair Request                    |')
    print('|----------------------------------------------|')
    print('| First-Day Materials                          |')
    print('| (11) Show Packet Status                      |')
    print('| (12) Send Packet                             |')
    print('| (13) Certify First-Day Requirements          |')
    print('|----------------------------------------------|')
    print('| (14) Return to Main Menu                     |')
    print('|----------------------------------------------|')


def showCredits():
    print('| COMP-350 Team One                            |')
    print('| Created by:                                  |')
    print('|  Zachary Drake                               |')
    print('|  Paul Kime                                   |')
    print('|  Connor Moore                                |')
    print('|  Jon Roeske                                  |')
    print('|  Aaron Urrea                                 |')
    print('|----------------------------------------------|')


def showVersion():
    print('| VERSION NUMBER: ' + versionNumber + '              |')
    print('|----------------------------------------------|')


def showMessage(message, **kwargs):
    if "topBracket" in kwargs and kwargs["topBracket"] is True:
        print('|----------------------------------------------|')

    if isinstance(message, list):
        for line in message:
            if isinstance(line, str):
                print("  INFO: " + line)

    else:
        print("  INFO: " + message)

    if "bottomBracket" in kwargs and kwargs["bottomBracket"] is True:
        print('|----------------------------------------------|')

    if "wait" in kwargs and isinstance(kwargs["wait"], int):
        time.sleep(kwargs["wait"])


def showPrompt(message, **kwargs):
    if "topBracket" in kwargs and kwargs["topBracket"] is True:
        print('|----------------------------------------------|')

    if isinstance(message, list):
        for line in message:
            if isinstance(line, str):
                print("  CONFIRM: " + line)
    else:
        print("  CONFIRM: " + message)

    if "prompt" in kwargs and isinstance(kwargs["prompt"], str):
        print('   ' + kwargs["prompt"])

    if "bottomBracket" in kwargs and kwargs["bottomBracket"] is True:
        print('|----------------------------------------------|')

    confirm = input(">> ")

    return confirm


def partnerPrompt(partner):
    print('| Camper has a partner request:                |')
    print('|  Partner: ' + partner.getName())
    print('| Would you like to assign the partner?        |')
    print('|  "Y" for Yes, "N" for No                     |')
    print('|----------------------------------------------|')

    confirmation = input(">> ")

    return confirmation

def viewCamperBalance(camperArray, name):
    if len(camperArray) <= 0:
        mainMenu()
        print('| There are currently no campers!              |')
        print('|----------------------------------------------|')
        return
    clearScreen()
    for Camper in camperArray:
        if Camper.getName() == name:
            print('  Balance: ' + str(Camper.getBalance()))
    print('|----------------------------------------------|')
    print('| Press "Enter" to return!                     |')
    print('|----------------------------------------------|')
    input()
    mainMenu()
    return
