from Handlers.guiHandler import *
from Objects.camper import Camper

def initializeData():
    global juneCampers
    global julyCampers
    global augustCampers
    global newCampers
    global bunkhouses
    global tribes

    juneCampers = []
    julyCampers = []
    augustCampers = []
    newCampers = []
    bunkhouses = []
    tribes = []

def createCamper():
    newCamper = Camper()

    try:
        newCamper.fullName = namePrompt()
        if(newCamper.fullName == 'EXIT' or newCamper.fullName == ''):
            return None

        check = 0

        while(check == 0):
            newCamper.age = agePrompt()
            if(newCamper.age == 'EXIT' or newCamper.age == ''):
                return None

            elif(newCamper.age >= 9 and newCamper.age <= 18):
                check = 1
            else:
                nonFatalError("Applicant must be between 9 and 18 years old.")

        check = 0

        while(check == 0):
            newCamper.gender = genderPrompt()
            if (newCamper.gender == 'EXIT' or newCamper.gender == ''):
                return None

            elif(newCamper.gender == 'F' or newCamper.gender == 'M'):
                check = 1
            else:
                nonFatalError('Applicant must be "M" or "F".')

        newCamper.address = addressPrompt()
        if(newCamper.address == 'EXIT' or newCamper.address == ''):
            return None

        newCamper.appStatus = 0

        while (1):
            clearScreen()
            confirmation = camperConfirmation(newCamper)

            if (confirmation == 'Y'):
                newCampers.append(newCamper)
                return True
            elif (confirmation == 'N'):
                return False

            else:
                nonFatalError('Must be "Y" or "N"')

    except:
        exit("CODE 2: Exception during camper creation")

def printNewCampers():
    if len(newCampers) <= 0:
        refreshScreen()
        print('| There are currently no campers!              |')
        print('|----------------------------------------------|')
        return
    clearScreen()
    for Camper in newCampers:
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

def viewCamperApplication():
    #try:
        fullname = namePrompt()
        camper = searchCamperArr(newCampers, fullname)

        status = camper.getAppStatus()

        refreshScreen()
        if(status == 0):
            print('  Camper Found: ' + camper.getName())
            print('  Application Status: Pending!')
            print('|----------------------------------------------|')
            return
        elif(status == 1):
            print('  Camper Found: ' + camper.getName())
            print('  Application Status: Accepted!')
            print('|----------------------------------------------|')
            return
        elif (status == 2):
            print('  Camper Found: ' + camper.getName())
            print('  Application Status: Rejected!')
            print('|----------------------------------------------|')
            return
    #except:
    #    refreshScreen()
    #    statusGetFailure()