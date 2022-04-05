import os
import time

from Objects.camper import *

versionNumber = "Build Mar292022"


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def refreshScreen():
    clearScreen()
    print('|----------------Camp Clerk CLI----------------| ')
    print('| (0)  Shutdown                                |')
    print('| (1)  Credits                                 |')
    print('| (2)  Show Version                            |')
    print('|----------------------------------------------|')
    print('| (3)  Create New Camper                       |')
    print('| (4)  View All Campers                        |')
    print('|----------------------------------------------|')
    print('| (5)  View Camper Application Status          |')
    print('| (6)  Accept Camper Application               |')
    print('| (7)  Decline/Withdraw Camper Application     |')
    print('|----------------------------------------------|')
    print('| (8)  View Current Camper Balance             |')
    print('| (9)  Reduce Camper Balance                   |')
    print('| (10) Raise Camper Balance                    |')
    print('| (11) Clear Camper Balance                    |')
    print('|----------------------------------------------|')
    print('| (12) Show Camper Packet Status               |')
    print('| (13) Send Camper Packet                      |')
    print('|----------------------------------------------|')
    print('| (14) Dump to file                            |')
    print('| (15) Load from file                          |')
    print('| (16) Reset file                              |')
    print('|----------------------------------------------|')
    print('| (17) Assign tribes                           |')
    print('| (18) Assign bunkhouses                       |')
    print('| (19) Certify camper first day reqs           |')
    print('| (20) Camper pair request                     |')
    print('| (21) Withdraw camper                         |')
    print('|----------------------------------------------|')
    print('| (22) Launch Django GUI                       |')
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
    print('| ERROR: Camper creation failed!               |')
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
        refreshScreen()
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
    refreshScreen()
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
    refreshScreen()
