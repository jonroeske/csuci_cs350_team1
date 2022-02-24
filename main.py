# CLI System
import sys

from Handlers.docHandler import *
from Handlers.guiHandler import *
from Handlers.camperHandler import *

def main(argv):
    status = 0
    index = 0

    refreshScreen()

    while(1):

        varInput = int(input(">> "))

        match varInput:
            case 1:                                 # Main Menu
                index += 1
                refreshScreen()
            case 2:                                 # Version
                index += 1
                showVersion()
            case 3:                                 # Create New Camper
                index += 1
                refreshScreen()
            case 4:
                index += 1
                namePrompt()
                camperFullname = input(">> ")
                # TODO - Implement Camper Lookup
                #         Print results here
                refreshScreen()
            case 5:
                index += 1
            case 6:
                index += 1
            case 7:
                index += 1
            case 8:
                index += 1
            case 9:
                index += 1
            case 10:
                index += 1
            case 11:
                index += 1
            case 12:
                index += 1
            case 13:
                index += 1
            case 14:
                index += 1
            case _:
                index += 1
                exit("ERROR")


main(sys.argv[1:])