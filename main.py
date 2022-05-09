# CLI System
# TODO - DELETE THIS WHEN POSSIBLE
from Handlers.camperHandler import *


from Handlers.MainMenu.camperCommands import *
from Handlers.MainMenu.sessionsCommands import *
from Handlers.MainMenu.automationCommands import *
from Handlers.MainMenu.debugCommands import *


from Handlers.CamperSubMenu.balanceCommands import *
from Handlers.CamperSubMenu.applicationCommands import *
from Handlers.CamperSubMenu.assignmentCommands import *


from Handlers.guiHandler import mainMenu, camperSubMenu


def main():
    initializeData()
    resetDate()
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
                        #processRefunds()
                        pass
                    case '9':
                        viewSessions()
                    case '10':
                        viewBunkhouses()
                    case '11':
                        viewTribes()
                    case '12':
                        setEveryBalance()
                    case '13':
                        setEveryApplication()
                    case '14':
                        changeTodaysDate()
                    case '15':
                        resetTodaysDate()
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
                        resetCamperApplication()
                    case '8':
                        pass
                    case '9':
                        pass
                    case '10':
                        pass
                    case '11':
                        assignCamperToSession()
                    case '12':
                        assignCamperToBunkhouse() # CHECK
                    case '13':
                        assignCamperToTribe() # CHECK
                    case '14':
                        assignPairRequest()
                    case '15':
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
