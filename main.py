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
                    fullname = namePrompt()
                    index = searchCamperArr(camperArray, fullname)
                    camperArray[index].printApplication()
                    refreshScreen()
                case '6':
                    # Accept camper application
                    try:
                        fullname = namePrompt()
                        index = searchCamperArr(camperArray, fullname)
                        camperArray[index].appstatus = True
                        camperApplicationUpdateSuccess()
                        refreshScreen()
                    except:
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
                        camperApplicationUpdateFailure()
                case '8':
                    # View camper balance
                    fullname = namePrompt()
                    index = searchCamperArr(camperArray, fullname)
                    camperArray[index].printBalance()
                    refreshScreen()
                case '9':
                    # Reduce camper balance
                    try:
                        fullname = namePrompt()
                        index = searchCamperArr(camperArray, fullname)
                        camperArray[index].balance -= amount
                        camperBalanceUpdateSuccess()
                        refreshScreen()
                    except:
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
                        camperBalanceUpdateFailure()
                case '12':
                    # Show camper packet status
                    fullname = namePrompt()
                    index = searchCamperArr(camperArray, fullname)
                    camperArray[index].printPacket()
                    refreshScreen()
                case '13':
                    # Update camper packet status
                    fullname = namePrompt()
                    index = searchCamperArr(camperArray, fullname)
                    camperArray[index].packetStatus = True
                    print("Camper packet sent")
                    refreshScreen()
                case _:
                    refreshScreen()
        except:
            exit("Somehow, we messed this up in main()")



def searchCamperArr(camperArr, fullname):
    try:
        found = camperArr.index(fullname)
        return found
    except:
        nonFatalError("Cannot find camper")


main()
