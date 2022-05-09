# CLI System
from Handlers.MainMenu.camperCommands import *
from Handlers.MainMenu.sessionsCommands import *
from Handlers.MainMenu.financialCommands import *

from Handlers.CamperSubMenu.applicationCommands import *
from Handlers.CamperSubMenu.assignmentCommands import *
from Handlers.CamperSubMenu.firstDayCommands import *

from Handlers.DebugSubMenu.automationCommands import *
from Handlers.DebugSubMenu.debugCommands import *
from Handlers.DebugSubMenu.populationCommands import *
from Handlers.DebugSubMenu.timeCommands import *

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
#  RESET SESSIONS   - TODO NEEDS TESTING
#  RESET BUNKS      - TODO NEEDS TESTING
#  RESET TRIBES     - TODO NEEDS TESTING
# AUTOMATION
#  AUTO SESSIONS    - NOT WORKING IN THE SLIGHTEST :(
#  AUTO BUNKS       - NOT WORKING IN THE SLIGHTEST :(
#  AUTO TRIBES      - NOT WORKING IN THE SLIGHTEST :(

def main():
    initializeData()
    resetDate()

    currentRuntime = 'mainMenu'
    debugDatabase = False

    mainMenu()

    while True:
        while currentRuntime == 'mainMenu':
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
                        if debugDatabase is True:
                            databaseView(currentRuntime)
                        else:
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
                        if debugDatabase is True:
                            databaseView(currentRuntime)
                        else:
                            debugSubMenu()
                    case _:
                        if debugDatabase is True:
                            databaseView(currentRuntime)
                        else:
                            mainMenu()

            except (KeyboardInterrupt, SystemExit):
                shutdown()
                time.sleep(2)
                exit()


        while currentRuntime == 'camperSubMenu':
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
                        viewAcceptanceNoticeStatus()
                    case '4':
                        fillOutForms()
                    case '5':
                        #checkInCamper()
                        pass
                    case '6':
                        assignCamperToSession()
                    case '7':
                        assignCamperToBunkhouse() # CHECK
                    case '8':
                        assignCamperToTribe() # CHECK
                    case '9':
                        assignPairRequest()
                    case '10':
                        currentRuntime = 'mainMenu'
                        if debugDatabase is True:
                            databaseView(currentRuntime)
                        else:
                            mainMenu()
                    case _:
                        if debugDatabase is True:
                            databaseView(currentRuntime)
                        else:
                            camperSubMenu()

            except (KeyboardInterrupt, SystemExit):
                shutdown()
                time.sleep(2)
                exit()


        while currentRuntime == 'debugSubMenu':
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
                        resetSessions()
                    case '5':
                        resetBunkhouses()
                    case '6':
                        resetTribes()
                    case '7':
                        if debugDatabase is False:
                            debugDatabase = True
                            showMessage("Database view toggled: True", bottomBracket=True)

                        elif debugDatabase is True:
                            debugDatabase = False
                            showMessage("Database view toggled: False", bottomBracket=True)
                    case '8':
                        currentRuntime = 'mainMenu'
                        if debugDatabase is True:
                            databaseView(currentRuntime)
                        else:
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
                        if debugDatabase is True:
                            databaseView(currentRuntime)
                        else:
                            debugSubMenu()
            except (KeyboardInterrupt, SystemExit):
                shutdown()
                time.sleep(2)
                exit()

main()