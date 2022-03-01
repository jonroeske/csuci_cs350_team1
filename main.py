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
                    # View camper application status
                    try:
                        fullname = namePrompt()
                        index = searchCamperArr(camperArray, fullname)
                        camperArray[index].printApplication()
                        refreshScreen()
                    except:
                        refreshScreen()
                        statusGetFailure()
                case '6':
                    # Accept camper application
                    try:
                        fullname = namePrompt()
                        index = searchCamperArr(camperArray, fullname)
                        camperArray[index].appstatus = True
                        camperApplicationUpdateSuccess()
                        refreshScreen()
                    except:
                        refreshScreen()
                        camperApplicationUpdateFailure()
                case '7':
                    # Decline/withdraw camper application
                    try:
                        fullname = namePrompt()
                        index = searchCamperArr(camperArray, fullname)
                        camperArray[index].appstatus = False
                        camperApplicationUpdateSuccess()
                        refreshScreen()
                    except:
                        refreshScreen()
                        camperApplicationUpdateFailure()
                case '8':
                    # View camper balance
                    try:
                        fullname = namePrompt()
                        index = searchCamperArr(camperArray, fullname)
                        camperArray[index].printBalance()
                        refreshScreen()
                    except:
                        refreshScreen()
                        statusGetFailure()
                case '9':
                    # Reduce camper balance
                    try:
                        fullname = namePrompt()
                        index = searchCamperArr(camperArray, fullname)
                        camperArray[index].balance -= amount
                        camperBalanceUpdateSuccess()
                        refreshScreen()
                    except:
                        refreshScreen()
                        camperBalanceUpdateFailure()
                case '10':
                    # Raise camper balance
                    try:
                        fullname = namePrompt()
                        index =  searchCamperArr(camperArray, fullname)
                        camperArray[index].balance += amount
                        camperBalanceUpdateSuccess()
                        refreshScreen()
                    except:
                        refreshScreen()
                        camperBalanceUpdateFailure()
                case '11':
                    # Clear camper balance
                    try:
                        fullname = namePrompt()
                        index = searchCamperArr(camperArray, fullname)
                        camperArray[index].balance = 0
                        camperBalanceUpdateSuccess()
                        refreshScreen()
                    except:
                        refreshScreen()
                        camperBalanceUpdateFailure()
                case '12':
                    # Show camper packet status
                    try:
                        fullname = namePrompt()
                        index = searchCamperArr(camperArray, fullname)
                        camperArray[index].printPacket()
                        refreshScreen()
                    except:
                        refreshScreen()
                        statusGetFailure()
                case '13':
                    # Update camper packet status
                    try:
                        fullname = namePrompt()
                        index = searchCamperArr(camperArray, fullname)
                        camperArray[index].packetStatus = True
                        refreshScreen()
                        camperPacketSentSuccess()
                    except:
                        refreshScreen()
                        camperPacketSentFailure()
                case _:
                    refreshScreen()
        except:
            exit("main() has stopped")



def searchCamperArr(camperArr, fullname):
    try:
        for i in range(0, len(camperArr)):
            if camperArr[i].fullname == fullname:
                return i
        nonFatalError("Cannot find camper")
    except:
        nonFatalError("Cannot find camper")


main()
