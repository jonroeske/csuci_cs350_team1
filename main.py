# CLI System
from Handlers.MainMenu.camperCommands import *
from Handlers.MainMenu.sessionsCommands import *
from Handlers.MainMenu.financialCommands import *

from Handlers.CamperSubMenu.applicationCommands import *
from Handlers.CamperSubMenu.assignmentCommands import *
from Handlers.CamperSubMenu.firstDayCommands import *

from Handlers.DebugSubMenu.automationCommands import *
from Handlers.DebugSubMenu.debugCommands import *

from Handlers.guiHandler import mainMenu, camperSubMenu, debugSubMenu
from Handlers.camperHandler import *

# TODO LIST, MAIN MENU:
# MAIN MENU
#  SHUTDOWN         - FULLY WORKING
#  CREDITS          - FULLY WORKING
#  VERSION          - FULLY WORKING
# CAMPERS
#  CAMPER ACTIONS   - FULLY WORKING
#  SIGN UP CAMPER   - FULLY WORKING
#  WITHDRAW CAMPER  - TODO NEEDS TESTING
#  VIEW CAMPER      - FULLY WORKING
#  VIEW ALL CAMPERS - FULLY WORKING
# FINANCES
#  VIEW BALANCE     - FULLY WORKING
#  PROCESS PAYMENT  - FULLY WORKING
#  PROCESS REFUND   - TODO NEEDS TESTING
# SESSIONS
#  VIEW SESSIONS    - FULLY WORKING
#  VIEW BUNKHOUSES  - FULLY WORKING
#  VIEW TRIBES      - FULLY WORKING

# TODO LIST, CAMPER SUB MENU:
# APPLICATION
#  VIEW APP STATUS  - FULLY WORKING
#  ACCEPT APP       - FULLY WORKING
#  REJECT APP       - FULLY WORKING
#  RESET APP        - FULLY WORKING
# FIRST DAY
#  VIEW NOTICE      - FULLY WORKING
#  FILL OUT FORMS   - TODO CREATE
#  CHECK IN CAMPER  - TODO CREATE
# ASSIGNMENT
#  ASSIGN SESSIONS  - FULLY WORKING
#  ASSIGN BUNKS     - FULLY WORKING
#  ASSIGN TRIBES    - FULLY WORKING
#  PROCESS PAIR     - FULLY WORKING

# TODO LIST, DEBUG SUB MENU:
# TIME
#  CHANGE DATE      - FULLY WORKING
#  RESET DATE       - FULLY WORKING
# POPULATION
#  POPULATE CAMP    - FULLY WORKING
#  RESET CAMP       - FULLY WORKING
#  RESET SESSIONS   - TODO CREATE
#  RESET BUNKS      - TODO CREATE
#  RESET TRIBES     - TODO CREATE
# AUTOMATION
#  SET ALL BALANCE  - FULLY WORKING
#  SET ALL APP      - FULLY WORKING
#  AUTO SESSIONS    - FULLY WORKING
#  AUTO BUNKS       - FULLY WORKING
#  AUTO TRIBES      - FULLY WORKING



def main():
    initializeData()
    resetDate()

    currentRuntime = 'mainMenu'
    debugDatabase = False

    mainMenu()

    while True:
        while currentRuntime == 'mainMenu':
            if debugDatabase is True:
                databaseView()

            try:
                varInput = input(">> ")
                match varInput:
                    case '0':
                        exit()
                    case '1':
                        showCredits()
                    case '2':
                        showVersion()
                    case '3':
                        currentRuntime = 'camperSubMenu'
                        camperSubMenu()
                    case '4':
                        signUpCamper()
                    case '5':
                        withdrawCamper()
                    case '6':
                        printCamper()
                    case '7':
                        printAllCampers()
                    case '8':
                        viewBalance()
                    case '9':
                        processPayment()
                    case '10':
                        processRefund()
                    case '11':
                        viewSessions()
                    case '12':
                        viewBunkhouses()
                    case '13':
                        viewTribes()
                    case '14':
                        currentRuntime = "debugSubMenu"
                        debugSubMenu()
                    case _:
                        mainMenu()

            except (KeyboardInterrupt, SystemExit):
                shutdown()
                time.sleep(2)
                exit()


        while currentRuntime == 'camperSubMenu':
            if debugDatabase is True:
                databaseView()

            try:
                varInput = input(">> ")
                match varInput:
                    case '0':
                        viewCamperApplication()
                    case '1':
                        acceptCamperApplication()
                    case '2':
                        rejectCamperApplication()
                    case '3':
                        resetCamperApplication()
                    case '4':
                        viewAcceptanceNoticeStatus()
                    case '5':
                        #fillOutForms()
                        pass
                    case '6':
                        #checkInCamper()
                        pass
                    case '7':
                        assignCamperToSession()
                    case '8':
                        assignCamperToBunkhouse() # CHECK
                    case '9':
                        assignCamperToTribe() # CHECK
                    case '10':
                        assignPairRequest()
                    case '11':
                        currentRuntime = 'mainMenu'
                        clearScreen()
                        mainMenu()
                    case _:
                        clearScreen()
                        camperSubMenu()

            except (KeyboardInterrupt, SystemExit):
                shutdown()
                time.sleep(2)
                exit()


        while currentRuntime == 'debugSubMenu':
            if debugDatabase is True:
                databaseView()

            try:
                varInput = input(">> ")
                match varInput:
                    case '0':
                        changeTodaysDate()
                    case '1':
                        resetTodaysDate()
                    case '2':
                        populateMaxCampers()
                    case '3':
                        resetAllCampers()
                    case '4':
                        #resetAllSessions()
                        pass
                    case '5':
                        #resetAllBunkhouses()
                        pass
                    case '6':
                        #resetAllTribes()
                        pass
                    case '7':
                        setEveryBalance()
                    case '8':
                        setEveryApplication() # CHECK
                    case '9':
                        if debugDatabase is False:
                            debugDatabase = True

                            debugSubMenu()
                            showMessage("Database view toggled: True", bottomBracket=True)

                        elif debugDatabase is True:
                            debugDatabase = False

                            debugSubMenu()

                            showMessage("Database view toggled: False", bottomBracket=True)
                    case '10':
                        currentRuntime = 'mainMenu'
                        mainMenu()
                    #case '9':
                    #    #autoAssignSessions()
                    #    pass
                    #case '10':
                    #    #autoAssignBunkhouses()
                    #    pass
                    #case '11':
                    #    #autoAssignTribes()
                    #    pass
                    #case '12':
                    #    currentRuntime = 'mainMenu'
                    #    mainMenu()
                    case _:
                        debugSubMenu()
            except (KeyboardInterrupt, SystemExit):
                shutdown()
                time.sleep(2)
                exit()

main()
