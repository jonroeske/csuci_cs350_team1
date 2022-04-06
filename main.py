# CLI System
import sys

from Handlers.docHandler import *
from Handlers.guiHandler import *
from Handlers.camperHandler import *
from Objects.camper import *

def main():
    mainMenu()

    initializeData()

    # Original
    while 1:
        try:
            varInput = input(">> ")
            match varInput:
                case '0':
                    # Stops application
                    shutdown()
                    time.sleep(2)
                    exit()
                case '1':
                    # Shows app credits
                    mainMenu()
                    showCredits()
                case '2':
                    # Shows app version
                    mainMenu()
                    showVersion()
                case '3':
                    # Creates a new camper
                    newCamper = createCamper()
                    if newCamper:
                        camperCreateSuccess()
                    else:
                        camperCreateFailure()
                case '4':
                    # View all campers
                    printAllCampers()
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
                    viewCamperPacketStatus()
                case '13':
                    # Update camper packet status
                    updateCamperPacketStatus()
                case '14':
                    assignCamperToSession()
                case '15':
                    # Assign tribes
                    assignTribesToCampers()
                case '16':
                    # Assign bunkhouses
                    assignBunkhouseToCampers()
                case '17':
                    # Certify camper
                    certifyCamperReqs()
                case '18':
                    # Pair request
                    assignPairRequest()
                case '19':
                    # Withdraw & refund camper
                    withdrawRefundCamper()
                case '20':
                    # Launch Django
                    notYetImplemented()
                case _:
                    mainMenu()
        except KeyboardInterrupt:
            shutdown()
            time.sleep(2)
            exit()
        except SystemExit:
            time.sleep(2)
            exit()
        except:
            exit("main() has stopped")

    currentRuntime = 'mainMenu'


    #while currentRuntime == 'mainMenu':
    #    try:
    #        varInput = input(">> ")
    #        match varInput:
    #            case '0':
    #                shutdown()
    #                time.sleep(2)
    #                exit()
    #            case '1':
    #                mainMenu()
    #                showCredits()
    #            case '2':
#
    #            case _:
    #                mainMenu()
    #    except KeyboardInterrupt:
    #        shutdown()
    #        time.sleep(2)
    #        exit()
    #    except SystemExit:
    #        shutdown()
    #        time.sleep(2)
    #        exit()
    #    except:
    #        exit("main() has stopped")
#

main()
