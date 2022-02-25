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
    print('| (6)  Withdraw Camper Application             |')
    print('|----------------------------------------------|')
    print('| (7)  View Current Camper Balance             |')
    print('| (8)  Reduce Camper Balance                   |')
    print('| (9)  Clear Camper Balance                    |')
    print('|----------------------------------------------|')
    print('| (10) View Camper Application Status          |')
    print('| (11) Accept Camper Application               |')
    print('| (12) Decline Camper Application              |')
    print('|----------------------------------------------|')
    print('| (13) Show Camper Packet Status               |')
    print('| (14) Send Camper Packet                      |')
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
    print('|----------------------------------------------|')
    print('| Please insert camper name: (First + Last)    |')
    print('|  EXAMPLE: "John Doe"                         |')
    print('|----------------------------------------------|')
    fullname: str = input(">> ")

    return fullname

def agePrompt():
    print('|----------------------------------------------|')
    print('| Please insert camper age:                    |')
    print('|----------------------------------------------|')
    age: str = input(">> ")

    return age

def genderPrompt():
    print('|----------------------------------------------|')
    print('| Please insert camper gender:                 |')
    print('|  NOTE: "Male" or "Female" only, sue us later |')
    print('|----------------------------------------------|')
    gender: str = input(">> ")

    return gender

def addressPrompt():
    print('|----------------------------------------------|')
    print('| Please insert camper home address:           |')
    print('|----------------------------------------------|')
    address: str = input(">> ")

    return address

def camperConfirmation(newCamper):
    print('|----------------------------------------------|')
    print('| Is this information correct?                 |')
    print('|  "Y" for Yes, "N" for No                     |')
    print('|----------------------------------------------|')
    print('  Name:    ' + newCamper.getName())
    print('  Age:     ' + newCamper.getAge())
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

def nonFatalError():
    print("| ERROR: Invalid character inputted.           | ")
    print("|  Retrying...                                 | ")
    print('|----------------------------------------------|')
    time.sleep(2)

def notYetImplemented():
    print("| ERROR: Not yet implemented.                  | ")
    print('|----------------------------------------------|')
    time.sleep(2)
    refreshScreen()