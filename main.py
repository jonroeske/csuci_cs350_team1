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
                    case '9': # TODO - DONE
                        viewBunkhouses()
                    case '10': # TODO - DONE
                        viewTribes()
                    case '11': # TODO - DONE
                        setEveryBalance()
                    case '12': # TODO - DONE
                        setEveryApplication()
                    case '13': # TODO - DONE
                        assignCampersToSessions()
                    case '14': # TODO - DONE
                        assignCampersToBunkhouses()
                    case '15': # TODO
                        notYetImplemented()
                        #assignCampersToTribes()
                    case '16': # TODO - DONE
                        populateMaxCampers()
                    case '17': # TODO - DONE
                        clearAllCampers()
                    #case '18':
                    #    clearAllSessions()
                    #case '19':
                    #    clearAllBunkHouses()
                    #case '20':
                    #    clearAllTribes()
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
            except Exception as e:
                print(e)

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
                    case '10': # TODO - DONE
                        assignPairRequest()
                    case '11': # TODO - DONE
                        viewCamperPacketStatus()
                    case '12': # TODO - DONE
                        updateCamperPacketStatus()
                    case '13': # TODO - IN PROGRESS
                        certifyCamperReqs()
                    case '14': # TODO - DONE
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
            except Exception as e:
                print(e)

main()
