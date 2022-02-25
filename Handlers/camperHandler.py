from Handlers.guiHandler import *
from Objects.camper import Camper

import time

def createCamper():

    clearScreen()

    newCamper = Camper()

    print('|----------------------------------------------|')
    print('| Type "EXIT" at any time to exit creation.    |')

    try:
        newCamper.fullName = namePrompt()
        if(newCamper.fullName == 'EXIT'):
            return None

        newCamper.age = agePrompt()
        if(newCamper.age == 'EXIT'):
            return None

        newCamper.gender = genderPrompt()
        if(newCamper.gender == 'EXIT'):
            return None

        newCamper.address = addressPrompt()
        if(newCamper.address == 'EXIT'):
            return None

        #newCamper.session = "unassigned"
        #newCamper.appstatus = "pending"
        #newCamper.balance = "pending"
        #newCamper.tribe = "unassigned"
        #newCamper.bunkhouse = "unassigned"
        #newCamper.acceptstatus = "pending"
        #newCamper.arrivalreqcert = "unassigned"
        #newCamper.checkedin = "false"
        #newcamper.assignmentrequest = "unassigned"
        #newcamper.datesentnotice = "pending"
        #newcamper.packetstatus = "pending"

    except:
        exit("CODE 2: Exception during camper creation")

    while(1):
        clearScreen()
        confirmation = camperConfirmation(newCamper)

        if(confirmation == 'Y'):
            return newCamper

        elif(confirmation == 'N'):
            return None

        else:
            nonFatalError()

def viewCampers(camperArray):

    if(len(camperArray) <= 0 ):
        refreshScreen()

        print('| There are currently no campers!              |')
        print('|----------------------------------------------|')
        return

    clearScreen()

    for Camper in camperArray:
        print('|----------------------------------------------|')
        print('  Name:    ' + Camper.getName())
        print('  Age:     ' + Camper.getAge())
        print('  Gender:  ' + Camper.getGender())
        print('  Address: ' + Camper.getAddress())

    print('|----------------------------------------------|')
    print('| Press enter to return!                       |')
    print('|----------------------------------------------|')

    input()
    return

