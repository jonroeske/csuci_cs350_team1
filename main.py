# CLI System
import sys

from Handlers.docHandler import *
from Handlers.guiHandler import *
from Handlers.camperHandler import *
from Objects.camper import *

def main():
    initializeData()

    # Original
    #while 1:
    #    try:
    #        varInput = input(">> ")
    #        match varInput:
    #            case '0':
    #                # Stops application
    #                shutdown()
    #                time.sleep(2)
    #                exit()
    #            case '1':
    #                # Shows app credits
    #                mainMenu()
    #                showCredits()
    #            case '2':
    #                # Shows app version
    #                mainMenu()
    #                showVersion()
    #            case '3':
    #                # Creates a new camper
    #                newCamper = createCamper()
    #                if newCamper:
    #                    camperCreateSuccess()
    #                else:
    #                    camperCreateFailure()
    #            case '4':
    #                # View all campers
    #                printAllCampers()
    #            case '5':
    #                # View camper application status
    #                viewCamperApplication()
    #            case '6':
    #                # Accept camper application
    #                acceptCamperApplication()
    #            case '7':
    #                # Decline/withdraw camper application
    #                rejectCamperApplication()
    #            case '8':
    #                # View camper balance
    #                viewCamperBalance()
    #            case '9':
    #                # Reduce camper balance
    #                reduceCamperBalance()
    #            case '10':
    #                # Raise camper balance
    #                raiseCamperBalance()
    #            case '11':
    #                # Clear camper balance
    #                clearCamperBalance()
    #            case '12':
    #                # Show camper packet status
    #                viewCamperPacketStatus()
    #            case '13':
    #                # Update camper packet status
    #                updateCamperPacketStatus()
    #            case '14':
    #                assignCamperToSession()
    #            case '15':
    #                # Assign tribes
    #                assignTribesToCampers()
    #            case '16':
    #                # Assign bunkhouses
    #                assignBunkhouseToCampers()
    #            case '17':
    #                # Certify camper
    #                certifyCamperReqs()
    #            case '18':
    #                # Pair request
    #                assignPairRequest()
    #            case '19':
    #                # Withdraw & refund camper
    #                withdrawRefundCamper()
    #            case '20':
    #                # Launch Django
    #                notYetImplemented()
    #            case _:
    #                mainMenu()
    #    except KeyboardInterrupt:
    #        shutdown()
    #        time.sleep(2)
    #        exit()
    #    except SystemExit:
    #        time.sleep(2)
    #        exit()
    #    except:
    #        exit("main() has stopped")

    currentRuntime = 'mainMenu'

    while 1:

        while currentRuntime == 'mainMenu':
            mainMenu()
            try:
                varInput = input(">> ")
                match varInput:
                    case '0':
                        shutdown()
                        time.sleep(2)
                        exit()
                    case '1':
                        mainMenu()
                        showCredits()
                    case '2':
                        mainMenu()
                        showVersion()
                    case '3':
                        createCamper()
                    case '4':
                        deleteCamper()
                    case '5':
                        currentRuntime = 'camperSubMenu'
                    case '6':
                        printCamper()
                    case '7':
                        printAllCampers()
                    case '8':
                        viewSessions()
                    case '9':
                        viewBunkhouses()
                    case '10':
                        viewTribes()
                    case '11':
                        notYetImplemented()
                    case '12':
                        notYetImplemented()
                    case '13':
                        notYetImplemented()
                    case '14':
                        notYetImplemented()
                    case '15':
                        notYetImplemented()
                    case _:
                        mainMenu()
            except KeyboardInterrupt:
                shutdown()
                time.sleep(2)
                exit()
            except SystemExit:
                shutdown()
                time.sleep(2)
                exit()
            except:
                exit("main() has stopped")

        while currentRuntime == 'camperSubMenu':
            camperSubMenu()
            try:
                varInput = input(">> ")
                match varInput:
                    case '0':
                        viewCamperBalance()
                    case '1':
                        raiseCamperBalance()
                    case '2':
                        reduceCamperBalance()
                    case '3':
                        clearCamperBalance()
                    case '4':
                        viewCamperApplication()
                    case '5':
                        acceptCamperApplication()
                    case '6':
                        rejectCamperApplication()
                    case '7':
                        assignCamperToSession()
                    case '8':
                        assignBunkhouseToCampers() # CHECK
                    case '9':
                        assignTribesToCampers() # CHECK
                    case '10':
                        assignPairRequest()
                    case '11':
                        withdrawCamper()
                    case '12':
                        viewCamperPacketStatus()
                    case '13':
                        updateCamperPacketStatus()
                    case '14':
                        certifyCamperReqs()
                    case '15':
                        currentRuntime = 'mainMenu'
                        break
                    case _:
                        camperSubMenu()
            except KeyboardInterrupt:
                shutdown()
                time.sleep(2)
                exit()
            except SystemExit:
                shutdown()
                time.sleep(2)
                exit()
            except:
                exit("main() has stopped")

main()
