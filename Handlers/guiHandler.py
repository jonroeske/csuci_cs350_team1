import os
import time

from Objects.camper import *

versionNumber = "Build Apr052022"


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


def namePrompt():
    clearScreen()
    print('|----------------------------------------------|')
    print('| Press "Enter" to return at any time          |')
    print('|----------------------------------------------|')
    print('| Please insert camper name: (First + Last)    |')
    print('|  EXAMPLE: "John Doe"                         |')
    print('|----------------------------------------------|')
    fullname = str(input(">> "))

    return fullname


def agePrompt():
    clearScreen()
    print('|----------------------------------------------|')
    print('| Press "Enter" to return at any time          |')
    print('|----------------------------------------------|')
    print('| Please insert camper age:                    |')
    print('|----------------------------------------------|')
    age = input(">> ")

    return age


def genderPrompt():
    clearScreen()
    print('|----------------------------------------------|')
    print('| Press "Enter" to return at any time          |')
    print('|----------------------------------------------|')
    print('| Please insert camper gender:                 |')
    print('|  NOTE: "M" or "F" only, sue us later         |')
    print('|----------------------------------------------|')
    gender = str(input(">> "))

    return gender


def addressPrompt():
    clearScreen()
    print('|----------------------------------------------|')
    print('| Press "Enter" to return at any time          |')
    print('|----------------------------------------------|')
    print('| Please insert camper home address:           |')
    print('|----------------------------------------------|')
    address = str(input(">> "))

    return address


def amountPrompt():
    clearScreen()
    print('|----------------------------------------------|')
    print('| Press "Enter" to return at any time          |')
    print('|----------------------------------------------|')
    print('| Please enter amount:                         |')
    print('|----------------------------------------------|')
    amount = str(input(">> "))

    return amount


def applicationStatusPrompt():
    clearScreen()
    print('|----------------------------------------------|')
    print('| Press "Enter" to return at any time          |')
    print('|----------------------------------------------|')
    print('| Which status would you like to set to?       |')
    print('| (0)  Pending                                 |')
    print('| (1)  Accepted                                |')
    print('| (2)  Rejected                                |')
    print('|----------------------------------------------|')
    status = str(input(">> "))

    return status


def camperConfirmation(newCamper):
    print('|----------------------------------------------|')
    print('| Is this information correct?                 |')
    print('|  "Y" for Yes, "N" for No                     |')
    print('|----------------------------------------------|')
    print('  Name:    ' + newCamper.getName())
    print('  Age:     ' + str(newCamper.getAge()))
    print('  Gender:  ' + newCamper.getGender())
    print('  Address: ' + newCamper.getAddress())
    print('|----------------------------------------------|')
    confirm = input(">> ")

    return confirm


def camperCreateSuccess():
    print('| Camper successfully created!                 |')
    print('|----------------------------------------------|')


def camperCreateFailure():
    print('| ERROR: Camper creation aborted               |')
    print('|----------------------------------------------|')


def camperAlreadyEnrolled():
    print('| This camper is enrolled in a session!        |')
    print('|----------------------------------------------|')


def camperApplicationUpdateSuccess():
    print('| Camper app status successfully updated!      |')
    print('|----------------------------------------------|')


def camperApplicationUpdateFailure():
    print('| ERROR: Camper app update failed!             |')
    print('|----------------------------------------------|')


def camperBalanceUpdateSuccess():
    print('| Camper balance successfully updated!         |')
    print('|----------------------------------------------|')


def camperBalanceUpdateFailure():
    print('| ERROR: Camper balance update failed!         |')
    print('|----------------------------------------------|')


def camperPacketSentSuccess():
    print('| Camper packet has been sent!                 |')
    print('|----------------------------------------------|')


def camperPacketSentFailure():
    print('| ERROR: Camper packet failed to send!         |')
    print('|----------------------------------------------|')


def statusGetFailure():
    print('| ERROR: Failed to get status!                 |')
    print('|----------------------------------------------|')


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


def nonFatalError(message):
    print("  ERROR: " + message)
    print('|----------------------------------------------|')
    print("| Retrying...                                  | ")
    print('|----------------------------------------------|')
    time.sleep(2)


def notYetImplemented():
    print("| ERROR: Not yet implemented.                  | ")
    print('|----------------------------------------------|')
    time.sleep(2)
    mainMenu()
