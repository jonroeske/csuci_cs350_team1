from Handlers.guiHandler import *
from Objects.camper import Camper
from Objects.camp import Camp

import pickle, os

summerCamp = Camp()
locations = ["allCampers", "juneCampers", "julyCampers", "augustCampers"]

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


def shutdown():
    showMessage("Shutting down...", bottomBracket=True, wait=1)

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
