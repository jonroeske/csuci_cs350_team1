import os
import time

from Objects.camper import *

versionNumber = "Build Feb192022"

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def refreshScreen():
    clearScreen()
    print('|----------------Camp Clerk CLI----------------| ')
    print('| (1)  Credits                                 |')
    print('| (2)  Show Version                            |')
    print('|----------------------------------------------|')
    print('| (3)  Create New Camper                       |')
    print('| (4)  View All Campers                        |')
    print('| (5)  Accept Camper Application               |')
    print('| (6)  Decline/Withdraw Camper Application     |')
    print('|----------------------------------------------|')
    print('| (7)  View Current Camper Balance             |')
    print('| (8)  Reduce Camper Balance                   |')
    print('| (9)  Clear Camper Balance                    |')
    print('|----------------------------------------------|')
    print('| (10) View Camper Application Status          |')
    print('| (11) Show Camper Packet Status               |')
    print('| (12) Send Camper Packet                      |')
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
    print('| Type "EXIT" at any time to exit.             |')
    print('|----------------------------------------------|')
    print('| Please insert camper name: (First + Last)    |')
    print('|  EXAMPLE: "John Doe"                         |')
    print('|----------------------------------------------|')
    fullname = str(input(">> "))

    return fullname

def agePrompt():
    clearScreen()
    print('|----------------------------------------------|')
    print('| Type "EXIT" at any time to exit.             |')
    print('|----------------------------------------------|')
    print('| Please insert camper age:                    |')
    print('|----------------------------------------------|')
    age = int(input(">> "))

    return age

def genderPrompt():
    clearScreen()
    print('|----------------------------------------------|')
    print('| Type "EXIT" at any time to exit.             |')
    print('|----------------------------------------------|')
    print('| Please insert camper gender:                 |')
    print('|  NOTE: "M" or "F" only, sue us later         |')
    print('|----------------------------------------------|')
    gender = str(input(">> "))

    return gender

def addressPrompt():
    clearScreen()
    print('|----------------------------------------------|')
    print('| Type "EXIT" at any time to exit.             |')
    print('|----------------------------------------------|')
    print('| Please insert camper home address:           |')
    print('|----------------------------------------------|')
    address = str(input(">> "))

    return address

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

def viewAllCampers(camperArray):
    if (len(camperArray) <= 0):
        refreshScreen()
        print('| There are currently no campers!              |')
        print('|----------------------------------------------|')
        return
    clearScreen()
    for Camper in camperArray:
        print('|----------------------------------------------|')
        print('  Name:    ' + Camper.getName())
        print('  Age:     ' + str(Camper.getAge()))
        print('  Gender:  ' + Camper.getGender())
        print('  Address: ' + Camper.getAddress())
    print('|----------------------------------------------|')
    print('| Press enter to return!                       |')
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