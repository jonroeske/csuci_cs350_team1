from GUI.guiHandler import *
from Objects.camper import Camper
from Objects.materials import Materials
from Objects.camp import Camp
from Documents.firstDay import checkInCert

from Objects.values import *

from faker import Faker
import random, pickle, sys, os

summerCamp = Camp()
locations = ["allCampers", "juneCampers", "julyCampers", "augustCampers"]

#====================================================================================================================================
# UTILITY FUNCTIONS
def initializeData():

    global summerCamp

    for location in locations:
        path = './Database/'+location+'.pkl'
        if os.path.exists(path):
            with (open(path, 'rb')) as openfile:
                while True:
                    try:
                        match location:
                            case "allCampers":
                                importedList = list(pickle.load(openfile))
                                summerCamp.setAllCampers(importedList)
                                break
                            case "juneCampers":
                                importedList = list(pickle.load(openfile))
                                summerCamp.setJune(importedList)
                                break
                            case "julyCampers":
                                importedList = list(pickle.load(openfile))
                                summerCamp.setJuly(importedList)
                                break
                            case "augustCampers":
                                importedList = list(pickle.load(openfile))
                                summerCamp.setAugust(importedList)
                                break

                    except EOFError:
                        print(location + ' loaded successfully!')
                        break
        elif not os.path.exists(path):
            fp = open(path, 'x')
            fp.close()
            print(location + ' not found! Creating...')


    print(summerCamp.getAllCampers())
    print(summerCamp.getJune())
    print(summerCamp.getJuly())
    print(summerCamp.getAugust())



def shutdown():
    print('| Shutting Down...                             |')
    print('|----------------------------------------------|')

    global summerCamp

    for location in locations:
        path = './Database/'+location+'.pkl'
        with (open(path, 'wb')) as openfile:
            while True:
                match location:
                    case "allCampers":
                        pickle.dump(summerCamp.getAllCampers(), openfile)
                        break
                    case "juneCampers":
                        pickle.dump(summerCamp.getJune(), openfile)

                        break
                    case "julyCampers":
                        pickle.dump(summerCamp.getJuly(), openfile)

                        break
                    case "augustCampers":
                        pickle.dump(summerCamp.getAugust(), openfile)
                        break





# TODO - DEPRECIATED
def searchCamperFullName(camperArr, fullname):
    try:
        for currCamper in camperArr:
            if isinstance(currCamper, Camper) and currCamper.getName() == fullname:
                return currCamper
    except AttributeError:
        pass
    return None


# TODO - DEPRECIATED
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


# TODO - DEPRECIATED
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
    except TypeError:
        pass
    return campersWithGender


def searchEmptySlot(array):
    return any(elem is None for elem in array)


def searchFilledSlot(array):
    return any(elem is not None for elem in array)


# TODO - DEPRECIATED
def searchAllGender(array, singleGender):
    toReturn = []

    try:
        for camper in array:
            try:
                gender = camper.getGender()
                if(gender == singleGender):
                    toReturn.append(camper)
            except AttributeError:
                pass
            except TypeError:
                pass
    except Exception is e:
        print(e)

    return toReturn

#====================================================================================================================================


#====================================================================================================================================

#  ASSIGNMENT
def assignCamperToSession():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        availability = [searchEmptySlot(juneCampers[0]), searchEmptySlot(julyCampers[0]), searchEmptySlot(augustCampers[0])]

        sessions = ["June", "July", "August"]

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
                    camperAlreadyEnrolled("session")
                    return
            except ValueError:
                pass
                # if this camper isn't a duplicate, then we want to create it
            
        while 1:

            clearScreen()

            print('|----------------------------------------------|')
            print('| What session would you like to assign?       |')
            print('| (0)  June                                    |')
            print(f'|  Availability: {maxCampersInSession - juneCampers[0].index(None)}' + '                            |')
            print('| (1)  July                                    |')
            print(f'|  Availability: {maxCampersInSession - julyCampers[0].index(None)}' + '                            |')
            print('| (2)  August                                  |')
            print(f'|  Availability: {maxCampersInSession - augustCampers[0].index(None)}' + '                            |')
            print('|----------------------------------------------|')

            command = int(input(">> "))
            session = None

            match command:
                case 0:
                    session = globals()["juneCampers"][0]
                case 1:
                    session = globals()["julyCampers"][0]
                case 2:
                    session = globals()["augustCampers"][0]
                case _:
                    nonFatalError("Incorrect input!")

            if camper.getAssignmentRequest() is False and availability[session]:
                session[session.index(None)] = camper
                camper.setSession(sessions[command])
                break

            elif camper.getAssignmentRequest():
                slotsRemaining = maxCampersInSession - session.index(None)
                partner = camper.getAssignmentRequest()

                if partner.getSession() is not None:
                    session[session.index(None)] = camper
                    camper.setSession(sessions[command])
                    break

                while 1:
                    confirmation = partnerPrompt(partner)

                    if confirmation == "Y" or confirmation == "N":
                        break
                    else:
                        nonFatalError("Incorrect Input!")


                if slotsRemaining > 1 and confirmation == "Y":
                    session[session.index(None)] = camper
                    camper.setSession(sessions[command])

                    session[session.index(None)] = partner
                    partner.setSession(sessions[command])
                    break

                elif slotsRemaining <= 1 and confirmation == "Y":
                    nonFatalError("There is not enough capacity for both campers!")

                elif confirmation == "N":
                    session[session.index(None)] = camper
                    camper.setSession(sessions[command])
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
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        if(camper is None):
            pass # TODO - WE NEED TO SET CONDITIONS FOR MISSPELLED NAMES

        session = camper.getSession()

        if(session == "June"):
            session = globals()["juneCampers"][1]
        elif(session == "July"):
            session = globals()["julyCampers"][1]
        elif(session == "August"):
            session = globals()["augustCampers"][1]
        elif session is None:
            camperSubMenu()
            print('| Camper must be assigned to a session!        |')
            print('|----------------------------------------------|')
            return

        maleOrFemaleBunkhouse = []

        if(camper.getGender() == 'M'):
            maleOrFemaleBunkhouse = [0, 1, 2]
        elif(camper.getGender() == 'F'):
            maleOrFemaleBunkhouse = [3, 4, 5]

        availability = [searchEmptySlot(session[maleOrFemaleBunkhouse[0]]),
                                        searchEmptySlot(session[maleOrFemaleBunkhouse[1]]),
                                        searchEmptySlot(session[maleOrFemaleBunkhouse[2]])]

        if camper.getAppStatus() != 1:
            camperSubMenu()
            print('| Camper must be accepted!                     |')
            print('|----------------------------------------------|')
            return

        elif not any(availability):
            camperSubMenu()
            print('| Sorry, all bunkhouses are full!              |')
            print('|----------------------------------------------|')
            return

        for bunkhouse in session:
            try:
                bunkhouse.index(camper)
                camperSubMenu()
                camperAlreadyEnrolled("bunkhouse")
                return
            except ValueError:
                pass
            # if this camper isn't a duplicate, then we want to create it

        while 1:

            clearScreen()

            print('|----------------------------------------------|')
            print('| What bunkhouse would you like to assign?     |')
            print('| (0)  Bunkhouse ' + str(maleOrFemaleBunkhouse[0] + 1) + '                             |')
            print(
                 f'|  Availability: {maxCampersInBunkhouse - session[maleOrFemaleBunkhouse[0]].index(None)}' + '                            |')
            print('| (1)  Bunkhouse ' + str(maleOrFemaleBunkhouse[1] + 1) + '                             |')
            print(
                 f'|  Availability: {maxCampersInBunkhouse - session[maleOrFemaleBunkhouse[1]].index(None)}' + '                            |')
            print('| (2)  Bunkhouse ' + str(maleOrFemaleBunkhouse[2] + 1) + '                             |')
            print(
                 f'|  Availability: {maxCampersInBunkhouse - session[maleOrFemaleBunkhouse[2]].index(None)}' + '                            |')

            command = int(input(">> "))

            bunkhouse = session[maleOrFemaleBunkhouse[command]]

            if camper.getAssignmentRequest() is None and availability[bunkhouse]:
                bunkhouse[bunkhouse.index(None)] = camper
                camper.setBunkhouse(maleOrFemaleBunkhouse[command])
                break

            elif camper.getAssignmentRequest():
                slotsRemaining = maxCampersInBunkhouse - bunkhouse.index(None)
                partner = camper.getAssignmentRequest()

                if partner.getBunkhouse() is not None or partner.getSession() != camper.getSession():
                    bunkhouse[bunkhouse.index(None)] = camper
                    camper.setBunkhouse(maleOrFemaleBunkhouse[command])
                    break


                while 1:
                    confirmation = partnerPrompt(partner)

                    if confirmation == "Y" or confirmation == "N":
                        break
                    else:
                        nonFatalError("Incorrect Input!")


                if slotsRemaining > 1 and confirmation == "Y":
                    bunkhouse[bunkhouse.index(None)] = camper
                    camper.setBunkhouse(maleOrFemaleBunkhouse[command])

                    bunkhouse[bunkhouse.index(None)] = partner
                    partner.setBunkhouse(maleOrFemaleBunkhouse[command])
                    break

                elif slotsRemaining <= 1 and confirmation == "Y":
                    nonFatalError("There is not enough capacity for both campers!")

                elif confirmation == "N":
                    bunkhouse[bunkhouse.index(None)] = camper
                    camper.setBunkhouse(maleOrFemaleBunkhouse[command])
                    break

            else:
                nonFatalError('That bunkhouse is full!')

        camperSubMenu()
        print('| Camper successfully added to bunkhouse!      |')
        print('|----------------------------------------------|')


    except Exception as e:
        print(e)
        # mainMenu()
        # statusGetFailure()


def assignCamperToTribe():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        if(camper is None):
            pass # TODO - WE NEED TO SET CONDITIONS FOR MISSPELLED NAMES

        session = camper.getSession()

        if(session == "June"):
            session = globals()["juneCampers"][2]
        elif(session == "July"):
            session = globals()["julyCampers"][2]
        elif(session == "August"):
            session = globals()["augustCampers"][2]
        elif session is None:
            camperSubMenu()
            print('| Camper must be assigned to a session!        |')
            print('|----------------------------------------------|')
            return


        availability = [searchEmptySlot(session[0]),
                                        searchEmptySlot(session[1]),
                                        searchEmptySlot(session[2]),
                                        searchEmptySlot(session[3]),
                                        searchEmptySlot(session[4]),
                                        searchEmptySlot(session[5])]

        if camper.getAppStatus() != 1:
            camperSubMenu()
            print('| Camper must be accepted!                     |')
            print('|----------------------------------------------|')
            return

        elif not any(availability):
            camperSubMenu()
            print('| Sorry, all tribes are full!                  |')
            print('|----------------------------------------------|')
            return

        for tribe in session:
            try:
                tribe.index(camper)
                camperSubMenu()
                camperAlreadyEnrolled("tribe")
                return
            except ValueError:
                pass
            # if this camper isn't a duplicate, then we want to create it

        while 1:

            clearScreen()

            print('|----------------------------------------------|')
            print('| What tribe would you like to assign?     |')
            print('| (0)  Tribe 1                                 |')
            print(
                 f'|  Availability: {maxCampersInTribe - session[0].index(None)}' + '                            |')
            print('| (1)  Tribe 2                                 |')
            print(
                 f'|  Availability: {maxCampersInTribe - session[1].index(None)}' + '                            |')
            print('| (2)  Tribe 3                                 |')
            print(
                 f'|  Availability: {maxCampersInTribe - session[2].index(None)}' + '                            |')
            print('| (3)  Tribe 4                                 |')
            print(
                 f'|  Availability: {maxCampersInTribe - session[3].index(None)}' + '                            |')
            print('| (4)  Tribe 5                                 |')
            print(
                 f'|  Availability: {maxCampersInTribe - session[4].index(None)}' + '                            |')
            print('| (5)  Tribe 6                                 |')
            print(
                 f'|  Availability: {maxCampersInTribe - session[5].index(None)}' + '                            |')

            command = int(input(">> "))

            tribe = session[command]

            if camper.getAssignmentRequest() is None and availability[tribe]:
                tribe[tribe.index(None)] = camper
                camper.setTribe(command)
                break

            elif camper.getAssignmentRequest():
                slotsRemaining = maxCampersInTribe - tribe.index(None)
                partner = camper.getAssignmentRequest()

                if partner.getTribe() is not None or partner.getSession() != camper.getSession():
                    tribe[tribe.index(None)] = camper
                    camper.setTribe(command)
                    break

                while 1:
                    confirmation = partnerPrompt(partner)

                    if confirmation == "Y" or confirmation == "N":
                        break
                    else:
                        nonFatalError("Incorrect Input!")

                if slotsRemaining > 1 and confirmation == "Y":
                    tribe[tribe.index(None)] = camper
                    camper.setTribe(command)

                    tribe[tribe.index(None)] = partner
                    partner.setTribe(command)
                    break

                elif slotsRemaining <= 1 and confirmation == "Y":
                    nonFatalError("There is not enough capacity for both campers!")

                elif confirmation == "N":
                    tribe[tribe.index(None)] = camper
                    camper.setTribe(command)
                    break

            else:
                nonFatalError('That tribe is full!')
        camperSubMenu()
        print('| Camper successfully added to tribe!          |')
        print('|----------------------------------------------|')


    except Exception as e:
        print(e)
        # mainMenu()
        # statusGetFailure()


def assignPairRequest():
    try:
        subjectname = namePrompt()
        subjectcamper = searchCamperFullName(allCampers, subjectname)

        if subjectcamper.getAssignmentRequest() is not None:
                print('| Camper already has request:                  |')
                print(f'|  {subjectcamper.getAssignmentRequest().getName()}')
                print('|----------------------------------------------|')
                print('| Press "Enter" to return!                     |')
                print('|----------------------------------------------|')
                input(">> ")
                camperSubMenu()
                return

        requestname = namePrompt()
        requestcamper = searchCamperFullName(allCampers, requestname)

        if requestcamper.getAssignmentRequest() is not None:
                print('| Camper already has request:                  |')
                print(f'|  {requestcamper.getAssignmentRequest().getName()}')
                print('|----------------------------------------------|')
                print('| Press "Enter" to return!                     |')
                print('|----------------------------------------------|')
                input(">> ")
                camperSubMenu()
                return

        if(subjectcamper.getGender() != requestcamper.getGender()):
            print('| Campers must have the same gender!           |')
            print('|----------------------------------------------|')
            print('| Press "Enter" to return!                     |')
            print('|----------------------------------------------|')
            input(">> ")
            camperSubMenu()
            return
        
        subjectcamper.setAssignmentRequest(requestcamper)
        requestcamper.setAssignmentRequest(subjectcamper)

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
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)
        clearScreen()

        try:
            checkInCert(camper)
        except:
            pass #lol


##def clearAllSessions():
#    print('| Clearing all sessions...                      |')
#    print('|----------------------------------------------|')
#
#    try:
#        for location in locations:
#            if location == 'allCampers':
#                continue
#            else:
#                globals()[location][0] = []
#                globals()[location][0] = list(itertools.repeat(None, maxCampersInSession))
#
#    except Exception as e:
#        print(e)
#
#    time.sleep(2)
#
#    mainMenu()
#    print('| Cleared all sessions, do we need them?       |')
#    print('|----------------------------------------------|')


##def clearAllBunkHouses():
#    print('| Clearing all bunkhouses                      |')
#    print('|----------------------------------------------|')
#
#    try:
#        for location in locations:
#            if location == 'allCampers':
#                continue
#            else:
#                globals()[location][1] = []
#                globals()[location][1] = list(itertools.repeat(list(itertools.repeat(None, maxCampersInBunkhouse)), maxBunkhouses))
#    except Exception as e:
#        print(e)
#
#    time.sleep(2)
#
#    mainMenu()
#    print('| Cleared all bunkhouses, homelessness is in!  |')
#    print('|----------------------------------------------|')


#def clearAllTribes():
#   print('| Clearing all bunkhouses                      |')
#   print('|----------------------------------------------|')
#
#   try:
#       for location in locations:
#           if location == 'allCampers':
#               continue
#           else:
#               globals()[location][2] = []
#               globals()[location][2] = list(itertools.repeat(list(itertools.repeat(None, maxCampersInBunkhouse)), maxBunkhouses))
#   except Exception as e:
#       print(e)
#
#   time.sleep(2)
#
#   mainMenu()
#   print('| Cleared all tribes, we\'re civilized now!     |')
#   print('|----------------------------------------------|')


#==========================================================================================================================