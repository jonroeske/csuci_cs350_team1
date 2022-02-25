# CLI System
import sys

from Handlers.docHandler import *
from Handlers.guiHandler import *
from Handlers.camperHandler import *
from Handlers.statusHandler import *
from Objects.camper import *

global camperArray
global bunkhouseArray
global tribeArray

def main():
    index = 0

    refreshScreen()

    camperArray = list()

    while(1):
        try:
            varInput = int(input(">> "))

            match varInput:
                case 1:                                 # Credits
                    refreshScreen()
                    showCredits()
                case 2:                                 # Version
                    refreshScreen()
                    showVersion()
                case 3:                                 # Create New Camper
                    newCamper = createCamper()
                    refreshScreen()
                    try:
                        if(newCamper != None):
                            if(newCamper.getGender() == "FEMALE"):
                                camperArray.insert(index + 36, newCamper)  # If we want to create a female camper, put them further down the array.
                            else:                                          #  Indexes 0 - 35 are reserved for males, 36 - 72 are reserved for females
                                camperArray.insert(index, newCamper)

                            index += 1
                            camperCreateSuccess()
                    except:
                        camperCreateFailure()

                case 4:
                    # View all campers
                    viewCampers(camperArray)
                    refreshScreen()
                case 5:
                    notYetImplemented()
                case 6:
                    notYetImplemented()
                case 7:
                    notYetImplemented()
                case 8:
                    notYetImplemented()
                case 9:
                    notYetImplemented()
                case 10:
                    notYetImplemented()
                case 11:
                    notYetImplemented()
                case 12:
                    notYetImplemented()
                case 13:
                    notYetImplemented()
                case 14:
                    notYetImplemented()
                case _:
                    nonFatalError()
                    refreshScreen()
        except:
            nonFatalError()
            refreshScreen()

#main(sys.argv[1:])
main()