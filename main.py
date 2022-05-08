# CLI System
# TODO - DELETE THIS WHEN POSSIBLE
from Handlers.camperHandler import *


from Handlers.MainMenu.camperCommands import *
from Handlers.MainMenu.sessionsCommands import *
from Handlers.MainMenu.automationCommands import *
from Handlers.MainMenu.debugCommands import *


from Handlers.CamperSubMenu.financialCommands import *
from Handlers.CamperSubMenu.applicationCommands import *
from Handlers.CamperSubMenu.assignmentCommands import *


from Handlers.guiHandler import mainMenu, camperSubMenu


def main():
    initializeData()
    currentRuntime = 'mainMenu'

    mainMenu()
    while True:
        while currentRuntime == 'mainMenu':
            try:
                varInput = input(">> ")
                match varInput:
                    case '0':
                        exit()
                    case '1':
                        mainMenu()
                        showCredits()
                    case '2':
                        mainMenu()
                        showVersion()
                    case '3':
                        currentRuntime = 'camperSubMenu'
                        camperSubMenu()
                    case '4':
                        createCamper()
                    case '5':
                        deleteCamper()
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
                        setEveryBalance()
                    case '12':
                        setEveryApplication()
                    case '13':
                        #assignCampersToSessions()
                        pass
                    case '14':
                        #assignCampersToBunkhouses()
                        pass
                    case '15':
                        #assignCampersToTribes()
                        pass
                    case '16':
                        populateMaxCampers()
                    case '17':
                        clearAllCampers()
                    #case '18':
                    #    clearAllSessions()
                    #case '19':
                    #    clearAllBunkHouses()
                    #case '20':
                    #    clearAllTribes()
                    case _:
                        print(summerCamp.getAllCampers())
                        print(summerCamp.getJune())
                        print(summerCamp.getJuly())
                        print(summerCamp.getAugust())
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
                print("How about here? " + e)

        while currentRuntime == 'camperSubMenu':
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
                        assignCamperToBunkhouse() # CHECK
                    case '9':
                        assignCamperToTribe() # CHECK
                    case '10':
                        assignPairRequest()
                    case '11':
                        viewCamperPacketStatus()
                    case '12':
                        updateCamperPacketStatus()
                    case '13':
                        certifyCamperReqs()
                    case '14':
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
