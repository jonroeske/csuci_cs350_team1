from Handlers.guiHandler import *
from Objects.camper import Camper
from Objects.materials import Materials
from firstDay.firstDay import assignTribes
from firstDay.firstDay import assignBunkhouses
from firstDay.firstDay import checkInCert
from postAcceptance.postAcceptance import withdrawCamper

import itertools
import random

from faker import Faker

import pickle
import os

#====================================================================================================================================
# UTILITY FUNCTIONS
def initializeData():
    global allCampers
    global juneCampers
    global julyCampers
    global augustCampers


    global locations
    global maxCampersTotal
    global maxCampersInSession
    global maxBunkhouses
    global maxCampersInBunkhouses
    global maxTribes
    global maxCampersInTribes

    locations = ['allCampers', 'juneCampers', 'julyCampers', 'augustCampers']

    maxCampersTotal = 216
    maxCampersInSession = 72
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
                for i in range(maxCampersTotal):
                    allCampers.append(None)

            else:
                campers = list(itertools.repeat(None, maxCampersInSession))
                bunkhouses = list(itertools.repeat(list(itertools.repeat(None, maxCampersInBunkhouse)), maxBunkhouses))
                tribes = list(itertools.repeat(list(itertools.repeat(None, maxCampersInTribe)), maxTribes))

                # This is how we're defining our seasonal campers
                #  The first list consists of every single camper
                #  The second list consists of the six bunkhouses, which consists of a list of campers
                #  The third list consists of the six tribes, which consists of a list of campers
                globals()[location] = [campers, bunkhouses, tribes]

        #try:
        if location == 'allCampers':
            globals()[location].sort(key=lambda x: (x is None, x))
        else:
            for i in range(3):
                globals()[location][i].sort(key=lambda x: (x is None, x))
        #except TypeError:
        #    pass

    print(allCampers)
    #print(juneCampers)
    #print(julyCampers)
    #print(augustCampers)


def shutdown():
    print('| Shutting Down...                             |')
    print('|----------------------------------------------|')
    for location in locations:
        path = './database/'+location+'.pkl'
        try:
            pickle.dump(globals()[location], open(path, 'wb'))
        except EOFError:
            break


def searchCamperFullName(camperArr, fullname):
    try:
        for currCamper in camperArr:
            if isinstance(currCamper, Camper) and currCamper.getName() == fullname:
                return currCamper
    except AttributeError:
        pass
    return None


def searchCamperLastName(camperArr, camper):
    campersWithLastName = []

    lastName = camper.getName()
    lastName = lastName.split()[1]
    try:
        for currCamper in camperArr:
            currCamperLastName = currCamper.getName()
            currCamperLastName = currCamperLastName.split()[1]
            if not camper.__eq__(currCamper) and lastName == currCamperLastName:
                campersWithLastName.append(currCamper)
    except AttributeError:
        pass
    return campersWithLastName

def searchCamperGender(camperArr, camper):
    campersWithGender = []

    gender = camper.getGender()
    try:
        for currCamper in camperArr:
            currCamperGender = currCamper.getGender()
            if not camper.__eq__(currCamper) and gender == currCamperGender:
                campersWithGender.append(currCamper)
    except AttributeError:
        pass
    return campersWithGender


def searchEmptySlot(array):
    return any(elem is None for elem in array)


def searchFilledSlot(array):
    return any(elem is not None for elem in array)


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


def numberOfGender(array):
    toReturn = [0, 0]

    try:
        for i in array:
            gender = i.getGender()
            if(gender == 'M'):
                toReturn[0] += 1
            elif(gender == 'F'):
                toReturn[1] += 1

        return toReturn
    except Exception as e:
        print(e)
#====================================================================================================================================


#====================================================================================================================================
# CAMPER OBJECT FUNCTIONS
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
        newCamper.balance = 1000.00
        newCamper.appStatus = 0

        newCamper.session = None
        newCamper.bunkhouse = None
        newCamper.tribe = None
        newCamper.arrivalReqCert = False
        newCamper.checkedIn = False

        newCamper.assignmentRequest = None
        newCamper.packetStatus = False
        newCamper.dateSentNotice = None
        newCamper.materials = Materials()

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


def deleteCamper():
    try:
        mainMenu()
        if not searchFilledSlot(allCampers):
            print('| There are currently no campers!              |')
            print('|----------------------------------------------|')
            return

        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        for location in locations:
            try:
                if location == 'allCampers':
                    globals()[location].remove(camper)
                    #globals()[location].sort(key=attrgetter('fullName'))
                else:
                    for i in range(3):
                        globals()[location][i].remove(camper)
                        #globals()[location][i].sort(key=attrgetter('fullName'))

            except ValueError:
                pass

        mainMenu()
        print('| Camper has been deleted!                     |')
        print('|----------------------------------------------|')

    except:
        mainMenu()
        statusGetFailure()


def printCamper():
    try:
        if not searchFilledSlot(allCampers):
            mainMenu()
            print('| There are currently no campers!              |')
            print('|----------------------------------------------|')
            return

        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

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
            print('|----------------------------------------------|')

            session = camper.getSession()
            bunkhouse = camper.getBunkhouse()
            tribe = camper.getTribe()

            if session:
                print('  Session: ' + session)
            if bunkhouse:
                print('  Bunkhouse: ' + bunkhouse)
            if tribe:
                print('  Tribe: ' + tribe)

            print('  Checked In: ' + str(camper.getCheckedIn()))
            print('  Packet Status: : ' + str(camper.getPacket()))

            packetDate = camper.getPacketSendDate()

            if packetDate:
                print('  Packet Sent Date: ' + str(packetDate))

        elif status == 2:
            print('  Application Status: Rejected')


        print('|----------------------------------------------|')
        print('| Press enter to return!                       |')
        print('|----------------------------------------------|')
        input()
        mainMenu()


    except Exception as e:
        print(e)
        mainMenu()
        statusGetFailure()


def printAllCampers():
    try:
        if not searchFilledSlot(allCampers):
            mainMenu()
            print('| There are currently no campers!              |')
            print('|----------------------------------------------|')
            return

        clearScreen()
        print('|----------------------------------------------|')
        print(f'|  Amount: {len(allCampers)}                                 |')

        genders = numberOfGender(allCampers)
        print(f'|  Composition: {genders[0]} Male(s), {genders[1]} Female(s)      |')
        print('|  Name(s):                                    |')

        for camper in allCampers:
            if camper:
                print('    ' + camper.getName())

                if camper.getAssignmentRequest() is not None:
                    print('     Partner: ' + camper.getAssignmentRequest().getName())



        print('|----------------------------------------------|')
        print('| Press enter to return!                       |')
        print('|----------------------------------------------|')
        input()
        mainMenu()
    except AttributeError:
        pass
    except Exception as e:
        print(e)
#====================================================================================================================================


#====================================================================================================================================
# SESSIONS

def viewSessions():
    try:
        clearScreen()
        print('|----------------------------------------------|')
        print('| Sessions:                                    |')
        for location in locations[1:]:
            if location == 'allCampers':
                pass
            else:
                month = location.split("Camper", maxsplit=1)[0].capitalize()

                print(f'    {month}:')
                try:
                    for i in range(maxCampersInSession):
                        camper = globals()[location][0][i]
                        print('     ' +camper.getName())
                except ValueError:
                    pass
                except AttributeError:
                    pass

        print('|----------------------------------------------|')
        print('| Press enter to return!                       |')
        print('|----------------------------------------------|')
        input()
        mainMenu()

    except Exception as e:
        mainMenu()
        statusGetFailure()


def viewBunkhouses():
    print("Cry me a river")


def viewTribes():
    print("Cry me a river")
#====================================================================================================================================


#====================================================================================================================================
# CAMPER ATTRIBUTE FUNCTIONS
#  BALANCE
def viewCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        camperSubMenu()

        print('  Camper Found: ' + camper.getName())
        print('  Balance Due: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        camperSubMenu()
        statusGetFailure()


def raiseCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        amount = amountPrompt()

        camperSubMenu()

        print('  Camper Found: ' + camper.getName())
        print('  Old Balance: $' + str(camper.getBalance()))

        camper.setBalance(camper.getBalance() + float(amount))

        print('  New Balance: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        camperSubMenu()
        statusGetFailure()


def reduceCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        amount = amountPrompt()

        camperSubMenu()

        print('  Camper Found: ' + camper.getName())
        print('  Old Balance: $' + str(camper.getBalance()))

        camper.setBalance(camper.getBalance() - float(amount))
        if camper.getBalance() < 0:
            camper.setBalance(0)

        print('  New Balance: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        camperSubMenu()
        statusGetFailure()


def clearCamperBalance():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        camperSubMenu()

        print('  Camper Found: ' + camper.getName())
        print('  Old Balance: $' + str(camper.getBalance()))

        camper.setBalance(0)

        print('  New Balance: $' + str(camper.getBalance()))
        print('|----------------------------------------------|')

    except:
        camperSubMenu()
        statusGetFailure()

#  APPLICATION
def viewCamperApplication():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        status = camper.getAppStatus()

        camperSubMenu()
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
        camperSubMenu()
        statusGetFailure()


def acceptCamperApplication():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        balance = camper.getBalance()

        camperSubMenu()
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
            camperSubMenu()
            statusGetFailure()
            return

    except:
        camperSubMenu()
        statusGetFailure()


def rejectCamperApplication():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        camperSubMenu()

        if camper.setAppStatus(2):
            print('  Camper Found: ' + camper.getName())
            print('  Application Status: Rejected!')
            print('|----------------------------------------------|')
        else:
            camperSubMenu()
            statusGetFailure()

    except:
        camperSubMenu()
        statusGetFailure()

#  ASSIGNMENT
def assignCamperToSession():
    try:
        maxCampers = 64

        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        availability = [searchEmptySlot(juneCampers[0]), searchEmptySlot(julyCampers[0]), searchEmptySlot(augustCampers[0])]

        if camper.getAppStatus() != 1:
            camperSubMenu()
            print('| Camper must be accepted!                     |')
            print('|----------------------------------------------|')
            return

        elif not any(availability):
            camperSubMenu()
            print('| Sorry, all sessions are full!                |')
            print('|----------------------------------------------|')
            return

        for location in locations:
            try:
                if location == "allCampers":
                    pass
                else:
                    globals()[location][0].index(camper)
                    camperSubMenu()
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

        camperSubMenu()
        print('| Camper successfully added to session!        |')
        print('|----------------------------------------------|')


    except Exception as e:
        print(e)
        #mainMenu()
        #statusGetFailure()


def assignCamperToBunkhouse():
    try:
        camperSubMenu()
        assignBunkhouses(allCampers)
        print(' Bunkhouses: ')
        for camper in allCampers:
            print(' ' + str(camper.getName()) + " Bunkhouse: " + str(camper.getBunkhouse()))
        print('|----------------------------------------------|')
    except:
        camperSubMenu()
        statusGetFailure()


def assignCamperToTribe():
    try:
        camperSubMenu()
        assignTribes(allCampers)
        print(' Tribes: ')
        for camper in allCampers:
            print(' ' + str(camper.getName()) + " Tribe: " + str(camper.getTribe()))
        print('|----------------------------------------------|')
    except:
        camperSubMenu()
        statusGetFailure()


def assignPairRequest():
    try:
        subjectname = namePrompt()
        subjectcamper = searchCamperFullName(allCampers, subjectname)

        requestname = namePrompt()
        requestcamper = searchCamperFullName(allCampers, requestname)
        subjectcamper.setRequest(requestcamper)

        camperSubMenu()
        print(' Added pair request between ' + str(subjectcamper.getName()) + ' and ' + str(requestcamper.getName()))
        print('|----------------------------------------------|')
    except:
        camperSubMenu()
        statusGetFailure()


def withdrawRefundCamper():
    try:
        name = namePrompt()
        camper = searchCamperFullName(allCampers, name)
        #withdrawCamper(camper, allCampers, tribes, bunkhouses)
        camperSubMenu()
        print(' Withdrew ' + str(camper.getName()))
        print('|----------------------------------------------|')
    except:
        camperSubMenu()
        statusGetFailure()

#  FIRST DAY MATERIALS
def viewCamperPacketStatus():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        camperSubMenu()

        print('  Camper Found: ' + camper.getName())
        print('  Packet Status: ' + str(camper.getPacket()))
        print('  Send Date: ' + str(camper.getPacketSendDate()))
        print('|----------------------------------------------|')

    except:
        camperSubMenu()
        statusGetFailure()


def updateCamperPacketStatus():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        camperSubMenu()

        camper.setPacketSend()
        print('  Camper Found: ' + camper.getName())
        print('  Packet Status: ' + str(camper.getPacket()))
        print('  Send Date: ' + str(camper.getPacketSendDate()))
        print('|----------------------------------------------|')
    except:
        camperSubMenu()
        statusGetFailure()


def certifyCamperReqs():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)
        clearScreen()
        checkInCert(camper)
    except:
        camperSubMenu()
        statusGetFailure()
#====================================================================================================================================


#====================================================================================================================================
# AUTOMATION
def setEveryBalance():
    try:
        amount = amountPrompt()
        mainMenu()
        if not searchFilledSlot(allCampers):
            print('| There are currently no campers!              |')
            print('|----------------------------------------------|')
            return

        for camper in allCampers:
            if camper:
                camper.setBalance(amount)

        print('| Every balance cleared!                       |')
        print('|  PS: HR would like a word with you!          |')
        print('|----------------------------------------------|')

    except AttributeError:
        pass
    except Exception as e:
        print(e)


def setEveryApplication():
    try:
        status = applicationStatusPrompt()
        mainMenu()
        if not searchFilledSlot(allCampers):
            print('| There are currently no campers!              |')
            print('|----------------------------------------------|')
            return

        for camper in allCampers:
            if camper:
                if camper.getBalance() == 0:
                    camper.setAppStatus(status)

        print('| Every application status changed!            |')
        print('|  PS: Some excellent quality control there...  |')
        print('|----------------------------------------------|')

    except AttributeError:
        pass
    except Exception as e:
        print(e)
#====================================================================================================================================


#====================================================================================================================================
# DEBUG
def populateMaxCampers():
    random.seed()
    fake = Faker()

    allCampers.sort(key=lambda x: (x is None, x))

    for i in range(maxCampersTotal):
        empty = searchEmptySlot(allCampers)
        if empty:
            newCamper = Camper()

            check = 0

            while check == 0:
                if i < maxCampersTotal/2:
                    newCamper.fullName = fake.first_name_male() + ' ' + fake.last_name_male()
                    newCamper.gender = 'M'
                elif i >= maxCampersTotal/2:
                    newCamper.fullName = fake.first_name_female() + ' ' + fake.last_name_female()
                    newCamper.gender = 'F'

                if searchCamperFullName(allCampers, newCamper.fullName) is None:
                    check = 1

            newCamper.age = random.randint(9, 18)

            newCamper.address = fake.street_address()

            newCamper.balance = 1000.00
            newCamper.appStatus = 0

            newCamper.session = None
            newCamper.bunkhouse = None
            newCamper.tribe = None
            newCamper.arrivalReqCert = False
            newCamper.checkedIn = False

            newCamper.assignmentRequest = None
            newCamper.packetStatus = False
            newCamper.dateSentNotice = None
            newCamper.materials = Materials()

            try:
                allCampers.remove(None)
                allCampers.append(newCamper)
            except ValueError:
                pass
                # we shouldn't be getting this error, as above the empty check confirms
                #  there is an empty slot to use

    allCampers.sort(key=lambda x: (x is None, x))

    for camper in allCampers:

        try:
            if camper.getAssignmentRequest() is None:
                # Here we find all campers with the same last name
                matchingCampers = searchCamperLastName(allCampers, camper)

                # Here we find all campers with the same last name
                #  We can't pair up two campers of different genders
                matchingCampers = searchCamperGender(matchingCampers, camper)

                if len(matchingCampers) > 0:

                    chanceRequest = random.randint(1, 4)
                    if chanceRequest == 4:
                        print("Pairing request started!")
                        try:
                            index = random.randint(0, len(matchingCampers) - 1)

                            camper.setRequest(matchingCampers[index])
                            matchingCampers[index].setRequest(camper)

                            print(f"Successful pair! {camper.getName()} {matchingCampers[index].getName()}")
                        except Exception as e:
                            print(e)

        except Exception as e:
            print(e)
    mainMenu()
    print('| Max campers created, calm down there God...  |')
    print('|----------------------------------------------|')


def clearAllCampers():
    allCampers.clear()
    for i in range(maxCampersInSession * 3):
        allCampers.append(None)

    mainMenu()
    print('| Cleared all campers, you monster!            |')
    print('|----------------------------------------------|')
#==========================================================================================================================