from Handlers.guiHandler import *
from Objects.camper import Camper
from firstDay.firstDay import assignTribes
from firstDay.firstDay import assignBunkhouses
from firstDay.firstDay import checkInCert
from postAcceptance.postAcceptance import withdrawCamper

import itertools
import operator
import pickle
import os

def initializeData():
    global allCampers
    global juneCampers
    global julyCampers
    global augustCampers

    global locations
    locations = ['allCampers', 'juneCampers', 'julyCampers', 'augustCampers']

    global maxCampersTotal
    global maxBunkhouses
    global maxCampersInBunkhouses

    global maxTribes
    global maxCampersInTribes


    maxCampersTotal = 72
    maxBunkhouses = 6
    maxCampersInBunkhouse = 12
    maxTribes = 6
    maxCampersInTribe = 12

    for location in locations:
        path = './database/'+location+'.pkl'

        if os.path.exists(path):
            with (open(path, 'rb')) as openfile:
                while True:
                    try:
                        globals()[location] = list(pickle.load(openfile))
                    except EOFError:
                        print(location + ' loaded successfully!')
                        break

        elif not os.path.exists(path):
            fp = open(path, 'x')
            fp.close()
            print(location + ' not found! Creating...')

            if location == 'allCampers':
                allCampers = []
                for i in range(maxCampersTotal * 3):
                    allCampers.append(None)

            else:
                campers = list(itertools.repeat(None, maxCampersTotal))
                bunkhouses = list(itertools.repeat(list(itertools.repeat(None, maxCampersInBunkhouse)), maxBunkhouses))
                tribes = list(itertools.repeat(list(itertools.repeat(None, maxCampersInTribe)), maxTribes))

                # This is how we're defining our seasonal campers
                #  The first list consists of every single camper
                #  The second list consists of the six bunkhouses, which consists of a list of campers
                #  The third list consists of the six tribes, which consists of a list of campers
                globals()[location] = [campers, bunkhouses, tribes]

    print(allCampers)
    print(juneCampers)
    print(julyCampers)
    print(augustCampers)


def shutdown():
    print('| Shutting Down...                             |')
    print('|----------------------------------------------|')
    for location in locations:
        path = './database/'+location+'.pkl'
        try:
            pickle.dump(globals()[location], open(path, 'wb'))
        except EOFError:
            break


def searchCamperArr(camperArr, fullname):
    for currCamper in camperArr:
        if currCamper.getName() == fullname:
            return currCamper
    return None


#def loadFromPickle():
#   mainMenu()
#   try:
#       loadedCampers = pickle.load(open('./allCampers.pkl', 'rb'))
#       for camper in loadedCampers:
#           if not (camper.__eq__(searchCamperArr(allCampers, camper))):
#               allCampers.append(camper)

#       print('| Successfully loaded campers from file!       |')
#       print('|----------------------------------------------|')
#   except EOFError:
#       print('| File is empty!                               |')
#       print('|----------------------------------------------|')
#   except:
#       nonFatalError('ERROR: Loading campers from persistent file')


#def resetPickle():
#   mainMenu()
#   try:
#       if os.path.exists('./campers.pkl'):
#           os.remove('./campers.pkl')
#           fp = open('./campers.pkl', 'x')
#           fp.close()
#           print('| Successfully cleared file!                   |')
#           print('|----------------------------------------------|')
#       else:
#           nonFatalError('Error: Finding persistent file')
#   except:
#       nonFatalError('ERROR: Clearing persistent file')


#ef dumpToPickle():
#   mainMenu()
#   try:
#       pickle.dump(allCampers, open('./campers.pkl', 'wb'))
#       print('| Successfully dumped campers to file!         |')
#       print('|----------------------------------------------|')
#   except:
#       nonFatalError('ERROR: Dumping campers to persistent file')

def searchEmptySlot(array):
    return any(elem is None for elem in array)


def searchFilledSlot(array):
    return any(elem is not None for elem in array)


def createCamper():
    if not searchEmptySlot(allCampers):
        mainMenu()
        print('| No more slots available!                     |')
        print('|----------------------------------------------|')
        return

    newCamper = Camper()

    try:
        newCamper.fullName = namePrompt()

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

            try:
                allCampers.index(newCamper)
                mainMenu()
                print('| This camper already exists!                  |')
                print('|----------------------------------------------|')
                return
            except ValueError:
                pass
                # if this camper isn't a duplicate, then we want to create it

            confirmation = camperConfirmation(newCamper)
            if confirmation == 'Y':
                index = searchEmptySlot(allCampers)
                allCampers.insert(index, newCamper)
                mainMenu()
                return True
            elif confirmation == 'N':
                mainMenu()
                return False
            else:
                nonFatalError('Must be "Y" or "N"')
    except:
        exit("CODE 2: Exception during camper creation")


def printAllCampers():
    try:
        if not searchFilledSlot(allCampers):
            mainMenu()
            print('| There are currently no campers!              |')
            print('|----------------------------------------------|')
            return

        clearScreen()
        for camper in allCampers:
            if camper:
                print('|----------------------------------------------|')
                print('  Name:    ' + camper.getName())
                print('  Age:     ' + str(camper.getAge()))
                print('  Gender:  ' + camper.getGender())
                print('  Address: ' + camper.getAddress())
                print('  Balance: $' + str(camper.getBalance()))

                status = camper.getAppStatus()

                if status == 0:
                    print('  Application Status: Pending')
                elif status == 1:
                    print('  Application Status: Accepted')
                elif status == 2:
                    print('  Application Status: Rejected')

                session = camper.getSession()

                if session:
                    print('  Session: ' + session)

        print('|----------------------------------------------|')
        print('| Press enter to return!                       |')
        print('|----------------------------------------------|')
        input()
        mainMenu()
    except AttributeError:
        pass
    except Exception as e:
        print(e)


def viewCamperApplication():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)

        status = camper.getAppStatus()

        mainMenu()
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
        mainMenu()
        statusGetFailure()


def acceptCamperApplication():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)

        balance = camper.getBalance()

        mainMenu()
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
            mainMenu()
            statusGetFailure()
            return

    except:
        mainMenu()
        statusGetFailure()


def rejectCamperApplication():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)

        mainMenu()

        if camper.setAppStatus(2):
            print('  Camper Found: ' + camper.getName())
            print('  Application Status: Rejected!')
            print('|----------------------------------------------|')
        else:
            mainMenu()
            statusGetFailure()

    except:
        mainMenu()
        statusGetFailure()


def viewCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)

        mainMenu()

        print('  Camper Found: ' + camper.getName())
        print('  Balance Due: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        mainMenu()
        statusGetFailure()


def viewCamperPacketStatus():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)

        mainMenu()

        print('  Camper Found: ' + camper.getName())
        print('  Packet Status: ' + str(camper.getPacket()))
        print('  Send Date: ' + str(camper.getPacketSendDate()))
        print('|----------------------------------------------|')

    except:
        mainMenu()
        statusGetFailure()


def updateCamperPacketStatus():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)

        mainMenu()

        camper.setPacketSend()
        print('  Camper Found: ' + camper.getName())
        print('  Packet Status: ' + str(camper.getPacket()))
        print('  Send Date: ' + str(camper.getPacketSendDate()))
        print('|----------------------------------------------|')
    except:
        mainMenu()
        statusGetFailure()


def reduceCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)

        amount = amountPrompt()

        mainMenu()

        print('  Camper Found: ' + camper.getName())
        print('  Old Balance: $' + str(camper.getBalance()))

        camper.setBalance(camper.getBalance() - float(amount))
        if camper.getBalance() < 0:
            camper.setBalance(0)

        print('  New Balance: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        mainMenu()
        statusGetFailure()


def raiseCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)

        amount = amountPrompt()

        mainMenu()

        print('  Camper Found: ' + camper.getName())
        print('  Old Balance: $' + str(camper.getBalance()))

        camper.setBalance(camper.getBalance() + float(amount))

        print('  New Balance: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        mainMenu()
        statusGetFailure()


def clearCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)

        mainMenu()

        print('  Camper Found: ' + camper.getName())
        print('  Old Balance: $' + str(camper.getBalance()))

        camper.setBalance(0)

        print('  New Balance: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        mainMenu()
        statusGetFailure()


def assignCamperToSession():
    try:
        maxCampers = 64

        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)

        availability = [searchEmptySlot(juneCampers[0]), searchEmptySlot(julyCampers[0]), searchEmptySlot(augustCampers[0])]

        if camper.getAppStatus() != 1:
            mainMenu()
            print('| Camper must be accepted!                     |')
            print('|----------------------------------------------|')
            return

        elif not any(availability):
            mainMenu()
            print('| Sorry, all sessions are full!                |')
            print('|----------------------------------------------|')
            return

        for location in locations:
            try:
                if location == "allCampers":
                    pass
                else:
                    globals()[location][0].index(camper)
                    mainMenu()
                    camperAlreadyEnrolled()
                    return
            except ValueError:
                pass
                # if this camper isn't a duplicate, then we want to create it



        while 1:
            clearScreen()

            print('|----------------------------------------------|')
            print('| What session would you like to assign?       |')
            print('| (0)  June                                    |')
            print(f'|  Availability: {maxCampers - juneCampers[0].index(None)}' + '                            |')
            print('| (1)  July                                    |')
            print(f'|  Availability: {maxCampers - julyCampers[0].index(None)}' + '                            |')
            print('| (2)  August                                  |')
            print(f'|  Availability: {maxCampers - augustCampers[0].index(None)}' + '                            |')
            print('|----------------------------------------------|')

            command = input(">> ")

            if command == '0' and availability[0]:
                juneCampers[0].insert(juneCampers[0].index(None), camper)
                camper.setSession("June")
                break
            elif command == '1' and availability[1]:
                julyCampers[0].insert(julyCampers[0].index(None), camper)
                camper.setSession("July")
                break
            elif command == '2' and availability[2]:
                augustCampers[0].insert(augustCampers[0].index(None), camper)
                camper.setSession("August")
                break
            else:
                nonFatalError('That session is full!')

        mainMenu()
        print('| Camper successfully added to session!        |')
        print('|----------------------------------------------|')


    except Exception as e:
        print(e)
        #mainMenu()
        #statusGetFailure()


def assignTribesToCampers():
    try:
        mainMenu()
        assignTribes(allCampers)
        print(' Tribes: ')
        for camper in allCampers:
            print(' ' + str(camper.getName()) + " Tribe: " + str(camper.getTribe()))
        print('|----------------------------------------------|')
    except:
        mainMenu()
        statusGetFailure()


def assignBunkhouseToCampers():
    try:
        mainMenu()
        assignBunkhouses(allCampers)
        print(' Bunkhouses: ')
        for camper in allCampers:
            print(' ' + str(camper.getName()) + " Bunkhouse: " + str(camper.getBunkhouse()))
        print('|----------------------------------------------|')
    except:
        mainMenu()
        statusGetFailure()


def certifyCamperReqs():
    try:
        fullname = namePrompt()
        camper = searchCamperArr(allCampers, fullname)
        mainMenu()
        checkInCert(camper)
        print('|----------------------------------------------|')
    except:
        mainMenu()
        statusGetFailure()


def assignPairRequest():
    try:
        subjectname = namePrompt()
        subjectcamper = searchCamperArr(allCampers, subjectname)

        requestname = namePrompt()
        requestcamper = searchCamperArr(allCampers, requestname)
        subjectcamper.setRequest(requestcamper)

        mainMenu()
        print(' Added pair request between ' + str(subjectcamper.getName()) + ' and ' + str(requestcamper.getName()))
        print('|----------------------------------------------|')
    except:
        mainMenu()
        statusGetFailure()


def withdrawRefundCamper():
    try:
        name = namePrompt()
        camper = searchCamperArr(allCampers, name)
        withdrawCamper(camper, allCampers, tribes, bunkhouses)
        mainMenu()
        print(' Withdrew ' + str(camper.getName()))
        print('|----------------------------------------------|')
    except:
        mainMenu()
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
