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
                case '1':
                    # Shows app credits
                    refreshScreen()
                    showCredits()
                case '2':
                    # Shows app version
                    refreshScreen()
                    showVersion()
                case '3':
                    # Creates a new camper
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
                case '5':
                    # Accept camper application
                case '6':
                    # Withdraw camper application
                case '7':
                    # View camper balance
                case '8':
                    # Reduce camper balance
                case '9':
                    # Clear camper balance
                case '10':
                    # View camper application status
                case '11':
                    # Show camper packet status
                case _:
                    refreshScreen()
        except:
            exit("Somehow, we messed this up in main()")


main()
