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
global index

def main():
    index = 0

    refreshScreen()
    camperArray = list()

    while(1):
        try:
            varInput = input(">> ")

            match varInput:
                case '1':                                 # Credits
                    refreshScreen()
                    showCredits()
                case '2':                                 # Version
                    refreshScreen()
                    showVersion()
                case '3':                                 # Create New Camper
                    newCamper = createCamper()
                    refreshScreen()
                    if(newCamper):
                        camperArray.append(newCamper)
                        camperCreateSuccess()
                    else:
                        camperCreateFailure()
                case '4':
                    # View all campers
                    viewAllCampers(camperArray)
                case _:
                    refreshScreen()
        except:
            exit("Somehow, we messed this up in main()")

#main(sys.argv[1:])
main()