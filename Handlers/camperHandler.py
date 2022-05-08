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