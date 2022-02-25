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
                    index += 1
                    refreshScreen()
                case 5:
                    break
                case 6:
                   break
                case 7:
                    break
                case 8:
                    break
                case 9:
                    break
                case 10:
                    break
                case 11:
                    break
                case 12:
                    break
                case 13:
                    break
                case 14:
                    break
                case _:
                    nonFatalError()
                    refreshScreen()
        except:
            nonFatalError()
            refreshScreen()

#main(sys.argv[1:])
main()