import os, time

import Objects.values
from Objects.camper import *


versionNumber = "Build May082022"

def mainMenu():
    print('|---------------Gila Breath Camp---------------|')
    print('| Today\'s Date: ' + datetime.strftime(Objects.values.TODAYS_DATE, "%m/%d/%Y") + '                     |')
    print('|------------------Main Menu-------------------|')
    print('| Main Menu                                    |')
    print('| (0)  Shutdown                                |')
    print('| (1)  Credits                                 |')
    print('| (2)  Version                                 |')
    print('|----------------------------------------------|')
    print('| Campers                                      |')
    print('| (3)  Camper Actions                          |')
    print('| (4)  Sign Up Camper                          |')
    print('| (5)  Withdraw Camper                         |')
    print('| (6)  View Camper                             |')
    print('| (7)  View All Campers                        |')
    print('|----------------------------------------------|')
    print('| Finances                                     |')
    print('| (8)  View Balance                            |')
    print('| (9)  Process Payment                         |')
    print('| (10) Process Refund                          |')
    print('|----------------------------------------------|')
    print('| Sessions                                     |')
    print('| (11) View Sessions                           |')
    print('| (12) View Bunkhouse                          |')
    print('| (13) View Tribes                             |')
    print('|----------------------------------------------|')
    print('| Debug                                        |')
    print('| (14) Debug Menu                              |')
    print('|----------------------------------------------|')


def camperSubMenu():
    print('|---------------Gila Breath Camp---------------|')
    print('| Today\'s Date: ' + datetime.strftime(Objects.values.TODAYS_DATE, "%m/%d/%Y") + '                     |')
    print('|-----------------Camper Menu------------------|')
    print('| Application                                  |')
    print('| (0)  View Application Status                 |')
    print('| (1)  Accept Application                      |')
    print('| (2)  Reject Application                      |')
    print('| (3)  Reset Application                       |')
    print('|----------------------------------------------|')
    print('| First-Day Requirements                       |')
    print('| (4)  View Acceptance Notice Status           |')
    print('| (5)  Fill Out Forms                          |')
    print('| (6)  Check In Camper                         |')
    print('|----------------------------------------------|')
    print('| Assignment                                   |')
    print('| (7)  Assign Session                          |')
    print('| (8)  Assign Bunkhouse                        |')
    print('| (9)  Assign Tribe                            |')
    print('| (10) Process Pair Request                    |')
    print('|----------------------------------------------|')
    print('| (11) Return to Main Menu                     |')
    print('|----------------------------------------------|')


def debugSubMenu():
    print('|---------------Gila Breath Camp---------------|')
    print('| Today\'s Date: ' + datetime.strftime(Objects.values.TODAYS_DATE, "%m/%d/%Y") + '                     |')
    print('|------------------Debug Menu------------------|')
    print('| Time                                         |')
    print('| (0) Change Today\'s Date                      |')
    print('| (1) Reset Today\'s Date                       |')
    print('|----------------------------------------------|')
    print('| Population                                   |')
    print('| (2) Populate Maximum Campers                 |')
    print('| (3) Reset All Campers                        |')
    print('| (4) Reset All Sessions                       |')
    print('| (5) Reset All Bunkhouses                     |')
    print('| (6) Reset All Tribes                         |')
    print('|----------------------------------------------|')
    print('| Automation                                   |')
    print('| (7) Set Every Balance                        |')
    print('| (8) Set Every Applications                   |')
    #print('| (9) Auto-Assign All Sessions                |')
    #print('| (10) Auto-Assign All Bunkhouses              |')
    #print('| (11) Auto-Assign All Tribes                  |')
    print('|----------------------------------------------|')
    print('| Debugging                                    |')
    print('| (9) Toggle Database View in Menu             |')
    print('|----------------------------------------------|')
    print('| (10) Return to Main Menu                     |')
    print('|----------------------------------------------|')
def showCredits():
    clearScreen()
    mainMenu()
    print('| COMP-350 Team One                            |')
    print('| Created by:                                  |')
    print('|  Zachary Drake                               |')
    print('|  Paul Kime                                   |')
    print('|  Connor Moore                                |')
    print('|  Jon Roeske                                  |')
    print('|  Aaron Urrea                                 |')
    print('|----------------------------------------------|')


def showVersion():
    clearScreen()
    mainMenu()
    print('| VERSION NUMBER: ' + versionNumber + '              |')
    print('|----------------------------------------------|')


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def showMessage(message, **kwargs):
    if "topBracket" in kwargs and kwargs["topBracket"] is True:
        print('|----------------------------------------------|')

    if isinstance(message, list):
        for line in message:
            if isinstance(line, str):
                print("  INFO: " + line)

    elif isinstance(message, str):
        print("  INFO: " + message)

    if "bottomBracket" in kwargs and kwargs["bottomBracket"] is True:
        print('|----------------------------------------------|')

    if "wait" in kwargs and isinstance(kwargs["wait"], int):
        time.sleep(kwargs["wait"])


def showPrompt(message, **kwargs):
    if "topBracket" in kwargs and kwargs["topBracket"] is True:
        print('|----------------------------------------------|')

    if isinstance(message, list):
        for line in message:
            if isinstance(line, str):
                print("  CONFIRM: " + line)
    else:
        print("  CONFIRM: " + message)

    if "prompt" in kwargs:
        if isinstance(kwargs["prompt"], list):
            for line in kwargs["prompt"]:
                if isinstance(line, str):
                    print('   ' + line)
        elif isinstance(kwargs["prompt"], str):
            print('   ' + kwargs["prompt"])

    if "bottomBracket" in kwargs and kwargs["bottomBracket"] is True:
        print('|----------------------------------------------|')

    confirm = input(">> ")

    return confirm


def printCamperGUI(camper, **kwargs):
    if not isinstance(camper, Camper):
        return

    if "topBracket" in kwargs and kwargs["topBracket"] is True:
        print('|----------------------------------------------|')


    if "camperCreation" in kwargs and kwargs["camperCreation"] is True:
        print('  Name:    ' + camper.getName())
        print('  Age:     ' + str(camper.getAge()))
        print('  Gender:  ' + camper.getGender())
        print('  Address: ' + camper.getAddress())

    elif "attribute" in kwargs and isinstance(kwargs["attribute"], str):
        print('  Name:    ' + camper.getName())

        match kwargs["attribute"]:
            case "applicationStatus":
                match camper.getAppStatus():
                    case 0:
                        print('  Application Status: Pending')
                    case 1:
                        print('  Application Status: Accepted')
                    case 2:
                        print('  Application Status: Rejected')
            case "hasPartner":
                print('  Partner:  ' + camper.getPartner().getName())
            case "balance":
                print('  Balance: $' + str(camper.getBalance()))
            case "bunkhouse":
                print('  Bunkhouse:  ' + str(camper.getBunkhouse()+1))
            case "appNotice":
                if camper.getAppNoticeIsSent() is True:
                    print('  Date Sent:  ' + datetime.strftime(camper.getDateAppNoticeSent(), "%m/%d/%Y"))
                elif camper.getDateAppNoticeSent() is False:
                    print('  Date Sent:  N/A')
            case "session":
                match camper.getSession():
                    case 0:
                        print('  Session:     June')
                    case 1:
                        print('  Session:     July')
                    case 2:
                        print('  Session:     August')
                    case _:
                        print('  Session:     None')
            case "tribe":
                print('  Tribe:   ' + str(camper.getTribe()+1))

    elif "simple" in kwargs and kwargs["simple"] is True:
        print('    Name:     ' + camper.getName())
        if camper.getHasPartner():
            print('     Partner:  ' + camper.getPartner().getName())

    elif "detailed" in kwargs and kwargs["detailed"] is True:
        print('  Name:     ' + camper.getName())
        if camper.getHasPartner():
            print('   Partner:  ' + camper.getPartner().getName())
        print('  Age:      ' + str(camper.getAge()))
        print('  Gender:   ' + camper.getGender())
        print('  Address:  ' + camper.getAddress())
        print('  Balance:  $' + str(camper.getBalance()))

        status = camper.getAppStatus()
        if status == 0:
            print('  Application Status: Pending')
        elif status == 1:
            print('  Application Status: Accepted')
            if camper.getAppNoticeIsSent() is True:
                print('   Date Sent:  ' + datetime.strftime(camper.getDateAppNoticeSent(), "%m/%d/%Y"))
            print('|----------------------------------------------|')

            print('  Forms Filled: ' + str(camper.getMaterials() is not None))
            print('  Checked In:   ' + str(camper.getCheckedIn()))

            session = camper.getSession()
            bunkhouse = camper.getBunkhouse()
            tribe = camper.getTribe()

            if session is not False:
                match session:
                    case 0:
                        print('  Session: June')
                    case 1:
                        print('  Session: July')
                    case 2:
                        print('  Session: August')

            if bunkhouse is not False:
                print('  Bunkhouse: ' + str(bunkhouse))
            if tribe is not False:
                print('  Tribe: ' + str(tribe))


        elif status == 2:
            print('  Application Status: Rejected')


    if "bottomBracket" in kwargs and kwargs["bottomBracket"] is True:
        print('|----------------------------------------------|')

