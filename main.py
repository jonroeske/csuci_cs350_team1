# CLI System
import sys

from Handlers.docHandler import *
from Handlers.guiHandler import *
from Handlers.camperHandler import *
from Objects.camper import *


def main():
    refreshScreen()

    initializeData()

    while 1:
        try:
            varInput = input(">> ")
            match varInput:
                case '0':
                    # Stops application
                    time.sleep(2)
                    break
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
                    if newCamper:
                        camperCreateSuccess()
                    else:
                        camperCreateFailure()
                case '4':
                    # View all campers
                    printNewCampers()
                case '5':
                    # View camper application status
                    viewCamperApplication()
                case '6':
                    # Accept camper application
                    acceptCamperApplication()
                case '7':
                    # Decline/withdraw camper application
                    rejectCamperApplication()
                case '8':
                    # View camper balance
                    viewCamperBalance()
                case '9':
                    # Reduce camper balance
                    reduceCamperBalance()
                case '10':
                    # Raise camper balance
                    raiseCamperBalance()
                case '11':
                    # Clear camper balance
                    clearCamperBalance()
                case '12':
                    # Show camper packet status
                    # try:
                    #    fullname = namePrompt()
                    #    camper = searchCamperArr(newCampers, fullname)
                    #    print(str(camper.getPacket()))
                    #    refreshScreen()
                    # except:
                    #    refreshScreen()
                    #    statusGetFailure()
                    notYetImplemented()
                case '13':
                    # Update camper packet status
                    # try:
                    #    fullname = namePrompt()
                    #    camper = searchCamperArr(newCampers, fullname)
                    #    camper.packetStatus = True
                    #    refreshScreen()
                    #    camperPacketSentSuccess()
                    # except:
                    #    refreshScreen()
                    #    camperPacketSentFailure()
                    notYetImplemented()
                case '14':
                    # Dumps campers to pickle file
                    dumpToPickle()
                case '15':
                    # Loads pickle file
                    loadFromPickle()
                case '16':
                    # Clears pickle file
                    resetPickle()
                case _:
                    refreshScreen()
        except:
            exit("main() has stopped")


main()
