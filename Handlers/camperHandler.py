from Handlers.guiHandler import *
from Objects.camper import Camper
import pickle
import os


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


def searchCamperArr(camperArr, name):
    try:
        for currCamper in camperArr:
            if str(currCamper.getName()) == name:
                return currCamper
    except:
        nonFatalError("Cannot find camper")
    return None


def loadFromPickle():
    refreshScreen()
    try:
        loadedCampers = pickle.load(open('./campers.pkl', 'rb'))
        for camper in loadedCampers:
            newCampers.append(camper)
        print('| Successfully loaded campers from file!       |')
        print('|----------------------------------------------|')
    except:
        nonFatalError('ERROR: Loading campers from persistent file')

def resetPickle():
    refreshScreen()
    try:
        if os.path.exists('./campers.pkl'):
            os.remove('./campers.pkl')
            fp = open('./campers.pkl', 'x')
            fp.close()
            print('| Successfully cleared file!                   |')
            print('|----------------------------------------------|')
        else:
            nonFatalError('Error: Finding persistent file')
    except:
        nonFatalError('ERROR: Clearing persistent file')


def dumpToPickle():
    refreshScreen()
    try:
        pickle.dump(newCampers, open('./campers.pkl', 'wb'))
        print('| Successfully dumped campers to file!         |')
        print('|----------------------------------------------|')
    except:
        nonFatalError('ERROR: Dumping campers to persistent file')


def createCamper():
    newCamper = Camper()

    try:
        newCamper.fullName = namePrompt()
        if newCamper.fullName == '':
            return False
        check = 0
        while check == 0:
            newCamper.age = agePrompt()
            if 9 <= int(newCamper.age) <= 18:
                check = 1
            else:
                nonFatalError("Applicant must be between 9 and 18 years old.")
        check = 0
        while check == 0:
            newCamper.gender = genderPrompt()
            if newCamper.gender == '':
                return False
            elif newCamper.gender == 'F' or newCamper.gender == 'M':
                check = 1
            else:
                nonFatalError('Applicant must be "M" or "F".')
        newCamper.address = addressPrompt()
        if newCamper.address == 'EXIT' or newCamper.address == '':
            return False
        newCamper.appStatus = 0
        newCamper.balance = 1000.00
        newCamper.packetStatus = False
        newCamper.checkedIn = False
        newCamper.acceptStatus = False
        newCamper.arrivalReqCert = False
        newCamper.session = None
        newCamper.tribe = None
        newCamper.bunkhouse = None
        newCamper.assignmentRequest = None
        newCamper.dateSentNotice = None
        newCamper.medical = None
        newCamper.legal = None
        newCamper.emergencyContacts = None
        newCamper.helmet = None
        newCamper.boots = None
        newCamper.sleepingBag = None
        newCamper.waterBottle = None
        newCamper.sunscreen = None
        newCamper.bugSpray = None
        while 1:
            clearScreen()
            confirmation = camperConfirmation(newCamper)
            if confirmation == 'Y':
                newCampers.append(newCamper)
                return True
            elif confirmation == 'N':
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

        status = Camper.getAppStatus()

        if status == 0:
            print('  Application Status: Pending')
            print('  Balance: $' + str(Camper.getBalance()))
        elif status == 1:
            print('  Application Status: Accepted')
            print('  Balance: $' + str(Camper.getBalance()))
        elif status == 2:
            print('  Application Status: Rejected')

    print('|----------------------------------------------|')
    print('| Press enter to return!                       |')
    print('|----------------------------------------------|')
    input()
    refreshScreen()


def viewCamperApplication():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(newCampers, fullname)

        status = camper.getAppStatus()

        refreshScreen()
        if status == 0:
            print('  Camper Found: ' + camper.getName())
            print('  Application Status: Pending!')
            print('|----------------------------------------------|')
            return
        elif status == 1:
            print('  Camper Found: ' + camper.getName())
            print('  Application Status: Accepted!')
            print('|----------------------------------------------|')
            return
        elif status == 2:
            print('  Camper Found: ' + camper.getName())
            print('  Application Status: Rejected!')
            print('|----------------------------------------------|')
            return
    except:
        refreshScreen()
        statusGetFailure()


def acceptCamperApplication():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(newCampers, fullname)

        balance = camper.getBalance()

        refreshScreen()
        if balance != 0:
            print('  Camper Found: ' + camper.getName())
            print('  Balance: $' + str(balance))
            print('   NOTE: Balance must be $0 to be accepted!')
            print('|----------------------------------------------|')
            return
        elif camper.setAppStatus(1):
            print('  Camper Found: ' + camper.getName())
            print('  Application Status: Accepted!')
            print('|----------------------------------------------|')
            return
        else:
            refreshScreen()
            statusGetFailure()
            return

    except:
        refreshScreen()
        statusGetFailure()


def rejectCamperApplication():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(newCampers, fullname)

        refreshScreen()

        if camper.setAppStatus(2):
            print('  Camper Found: ' + camper.getName())
            print('  Application Status: Rejected!')
            print('|----------------------------------------------|')
        else:
            refreshScreen()
            statusGetFailure()

    except:
        refreshScreen()
        statusGetFailure()


def viewCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(newCampers, fullname)

        refreshScreen()

        print('  Camper Found: ' + camper.getName())
        print('  Balance Due: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        refreshScreen()
        statusGetFailure()

def viewCamperPacketStatus():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(newCampers, fullname)

        refreshScreen()

        print('  Camper Found: ' + camper.getName())
        print('  Packet Status: ' + str(camper.getPacket()))
        print('  Send Date: ' + str(camper.getPacketSendDate()))
        print('|----------------------------------------------|')

    except:
        refreshScreen()
        statusGetFailure()

def updateCamperPacketStatus():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(newCampers, fullname)

        refreshScreen()

        camper.setPacketSend()
        print('  Camper Found: ' + camper.getName())
        print('  Packet Status: ' + str(camper.getPacket()))
        print('  Send Date: ' + str(camper.getPacketSendDate()))
        print('|----------------------------------------------|')
    except:
        refreshScreen()
        statusGetFailure()

def reduceCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(newCampers, fullname)

        amount = amountPrompt()

        refreshScreen()

        print('  Camper Found: ' + camper.getName())
        print('  Old Balance: $' + str(camper.getBalance()))

        camper.setBalance(camper.getBalance() - float(amount))
        if camper.getBalance() < 0:
            camper.setBalance(0)

        print('  New Balance: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        refreshScreen()
        statusGetFailure()


def raiseCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(newCampers, fullname)

        amount = amountPrompt()

        refreshScreen()

        print('  Camper Found: ' + camper.getName())
        print('  Old Balance: $' + str(camper.getBalance()))

        camper.setBalance(camper.getBalance() + float(amount))

        print('  New Balance: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        refreshScreen()
        statusGetFailure()


def clearCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(newCampers, fullname)

        refreshScreen()

        print('  Camper Found: ' + camper.getName())
        print('  Old Balance: $' + str(camper.getBalance()))

        camper.setBalance(0)

        print('  New Balance: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        refreshScreen()
        statusGetFailure()


def isCamperAccepted(camper):
    if camper.getAppStatus() == 0:
        print('| Camper has not been accepted!                |')
        print('|----------------------------------------------|')
        return False
    elif camper.getAppStatus() == 2:
        print('| Camper has been Rejected!                    |')
        print('|----------------------------------------------|')
        return False
    else:
        return True
