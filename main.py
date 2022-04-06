# CLI System
import sys

from Handlers.camperHandler import *

def main():
    initializeData()
    currentRuntime = 'mainMenu'

    mainMenu()
    while 1:

        while currentRuntime == 'mainMenu':
            try:
                varInput = input(">> ")
                match varInput:
                    case '0': # TODO - DONE
                        exit()
                    case '1': # TODO - DONE
                        mainMenu()
                        showCredits()
                    case '2': # TODO - DONE
                        mainMenu()
                        showVersion()
                    case '3': # TODO - DONE
                        createCamper()
                    case '4': # TODO - DONE
                        deleteCamper()
                    case '5': # TODO - DONE
                        currentRuntime = 'camperSubMenu'
                        camperSubMenu()
                    case '6': # TODO - DONE
                        printCamper()
                    case '7': # TODO - DONE
                        printAllCampers()
                    case '8': # TODO - DONE
                        viewSessions()
                    case '9': # TODO
                        viewBunkhouses()
                    case '10': # TODO
                        viewTribes()
                    case '11': # TODO - DONE
                        setEveryBalance()
                    case '12': # TODO - DONE
                        setEveryApplication()
                    case '13': # TODO
                        assignCampersToSessions()
                    case '14': # TODO
                        notYetImplemented()
                    case '15': # TODO
                        notYetImplemented()
                    case '16': # TODO - DONE
                        populateMaxCampers()
                    case '17': # TODO - DONE
                        clearAllCampers()
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
            try:
                varInput = input(">> ")
                match varInput:
                    case '0': # TODO - DONE
                        viewCamperBalance()
                    case '1': # TODO - DONE
                        raiseCamperBalance()
                    case '2': # TODO - DONE
                        reduceCamperBalance()
                    case '3': # TODO - DONE
                        clearCamperBalance()
                    case '4': # TODO - DONE
                        viewCamperApplication()
                    case '5': # TODO - DONE
                        acceptCamperApplication()
                    case '6':# TODO - DONE
                        rejectCamperApplication()
                    case '7': # TODO - DONE
                        assignCamperToSession()
                    case '8': # TODO
                        assignCamperToBunkhouse() # CHECK
                    case '9': # TODO
                        assignCamperToTribe() # CHECK
                    case '10': # TODO
                        assignPairRequest()
                    case '11': # TODO
                        withdrawCamper()
                    case '12': # TODO - DONE
                        viewCamperPacketStatus()
                    case '13': # TODO - DONE
                        updateCamperPacketStatus()
                    case '14': # TODO - IN PROGRESS
                        certifyCamperReqs()
                    case '15': # TODO - DONE
                        currentRuntime = 'mainMenu'
                        mainMenu()
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
