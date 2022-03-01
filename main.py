# CLI System
import sys

from Handlers.docHandler import *
from Handlers.guiHandler import *
from Handlers.camperHandler import *
from Handlers.statusHandler import *
from Objects.camper import *

def main():
    refreshScreen()

    initializeData()
    
    while(1):
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
                    if(newCamper == True):
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
                    try:
                        fullname = namePrompt()
                        camper = searchCamperArr(newCampers, fullname)
                        camper.appstatus = True
                        camperApplicationUpdateSuccess()
                        refreshScreen()
                    except:
                        refreshScreen()
                        camperApplicationUpdateFailure()
                case '7':
                    # Decline/withdraw camper application
                    try:
                        fullname = namePrompt()
                        camper = searchCamperArr(newCampers, fullname)
                        camper.appstatus = False
                        camperApplicationUpdateSuccess()
                        refreshScreen()
                    except:
                        refreshScreen()
                        camperApplicationUpdateFailure()
                case '8':
                    # View camper balance
                    try:
                        fullname = namePrompt()
                        viewCamperBalance(newCampers, fullname)
                    except:
                        refreshScreen()
                        statusGetFailure()
                case '9':
                    # Reduce camper balance
                    try:
                        fullname = namePrompt()
                        camper = searchCamperArr(newCampers, fullname)
                        amount = amountPrompt()
                        camper.balance -= amount
                        camperBalanceUpdateSuccess()
                        refreshScreen()
                    except:
                        refreshScreen()
                        camperBalanceUpdateFailure()
                case '10':
                    # Raise camper balance
                    try:
                        fullname = namePrompt()
                        camper = searchCamperArr(newCampers, fullname)
                        amount = amountPrompt()
                        camper.balance += amount
                        camperBalanceUpdateSuccess()
                        refreshScreen()
                    except:
                        refreshScreen()
                        camperBalanceUpdateFailure()
                case '11':
                    # Clear camper balance
                    try:
                        fullname = namePrompt()
                        camper = searchCamperArr(newCampers, fullname)
                        camper.balance = 0
                        camperBalanceUpdateSuccess()
                        refreshScreen()
                    except:
                        refreshScreen()
                        camperBalanceUpdateFailure()
                case '12':
                    # Show camper packet status
                    try:
                        fullname = namePrompt()
                        camper = searchCamperArr(newCampers, fullname)
                        print(str(camper.getPacket()))
                        refreshScreen()
                    except:
                        refreshScreen()
                        statusGetFailure()
                case '13':
                    # Update camper packet status
                    try:
                        fullname = namePrompt()
                        camper = searchCamperArr(newCampers, fullname)
                        camper.packetStatus = True
                        refreshScreen()
                        camperPacketSentSuccess()
                    except:
                        refreshScreen()
                        camperPacketSentFailure()
                case _:
                    refreshScreen()
        except:
            exit("main() has stopped")


main()
