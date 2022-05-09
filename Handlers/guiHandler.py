import os, time

import Objects.values
from Objects.camper import *


versionNumber = "Build May082022"

def mainMenu():
    clearScreen()
    print('|---------------Gila Breath Camp---------------|')
    print('| Today\'s Date: ' + Objects.values.TODAYS_DATE + '                     |')
    print('|----------------------------------------------|')
    print('| Main Menu                                    |')
    print('| (0)  Shutdown                                |')
    print('| (1)  Credits                                 |')
    print('| (2)  Show Version                            |')
    print('|----------------------------------------------|')
    print('| Campers                                      |')
    print('| (3)  Camper Actions                          |')
    print('| (4)  Create New Camper                       |')
    print('| (5)  Delete Camper                           |')
    print('| (6)  View Camper                             |')
    print('| (7)  View All Campers                        |')
    print('|----------------------------------------------|')
    print('| Finances                                     |')
    print('| (8)  Process Refund                          |')
    print('|----------------------------------------------|')
    print('| Sessions                                     |')
    print('| (9)  View Sessions                           |')
    print('| (10) View Bunkhouse                          |')
    print('| (11) View Tribes                             |')
    print('|----------------------------------------------|')
    print('| Automation                                   |')
    print('| (12) Set Every Balance                       |')
    print('| (13) Set All Applications                    |')
    #print('| (13) Auto-Assign All Sessions                |')
    #print('| (14) Auto-Assign All Bunkhouses              |')
    #print('| (15) Auto-Assign All Tribes                  |')


    print('|----------------------------------------------|')
    print('| DEBUG                                        |')
    print('| (14) Change Today\'s Date                     |')
    print('| (15) Reset Today\'s Date                      |')
    print('| (16) Populate Maximum Campers                |')
    print('| (17) Reset All Campers                       |')
    print('| (18) Reset All Sessions                      |')
    print('| (19) Reset All Bunkhouses                    |')
    print('| (20) Reset All Tribes                        |')
    print('|----------------------------------------------|')


def camperSubMenu():
    clearScreen()
    print('|----------------Camp Clerk CLI----------------|')
    print('| Balance                                      |')
    print('| (0)  View Camper Balance                     |')
    print('| (1)  Raise Camper Balance                    |')
    print('| (2)  Reduce Camper Balance                   |')
    print('| (3)  Clear Camper Balance                    |')
    print('|----------------------------------------------|')
    print('| Application                                  |')
    print('| (4)  View Application Status                 |')
    print('| (5)  Accept Application                      |')
    print('| (6)  Decline Application                     |')
    print('| (7)  Reset Application                       |')
    print('|----------------------------------------------|')
    print('| First-Day Requirements                       |')
    print('| (8) Show Packet Status                       |')
    print('| (9) Send Packet                              |')
    print('| (10) Certify First-Day Requirements          |')
    print('|----------------------------------------------|')
    print('| Assignment                                   |')
    print('| (11)  Assign Session                         |')
    print('| (12)  Assign Bunkhouse                       |')
    print('| (13)  Assign Tribe                           |')
    print('| (14) Process Pair Request                    |')
    print('|----------------------------------------------|')
    print('| (15) Return to Main Menu                     |')
    print('|----------------------------------------------|')


def showCredits():
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
            case "assignmentRequest":
                print('  Partner:  ' + camper.getAssignment().getName())
            case "balance":
                print('  Balance:   $' + str(camper.getBalance()))
            case "bunkhouse":
                print('  Bunkhouse:  ' + str(camper.getBunkhouse()+1))
            case "packetStatus":
                pass # TODO - SIMPLIFY CAMPER VARIABLES
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
        if camper.getAssignmentRequest():
            print('     Partner:  ' + camper.getAssignment().getName())

    elif "detailed" in kwargs and kwargs["detailed"] is True:
        print('  Name:     ' + camper.getName())
        if camper.getAssignmentRequest():
            print('   Partner:  ' + camper.getAssignment().getName())
        print('  Age:      ' + str(camper.getAge()))
        print('  Gender:   ' + camper.getGender())
        print('  Address:  ' + camper.getAddress())
        print('  Balance:  $' + str(camper.getBalance()))

        status = camper.getAppStatus()
        if status == 0:
            print('  Application Status: Pending')
        elif status == 1:
            print('  Application Status: Accepted')
            print('|----------------------------------------------|')

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

            print('  Checked In: ' + str(camper.getCheckedIn()))
            print('  Packet Status: : ' + str(camper.getPacket()))

            packetDate = camper.getPacketSendDate()

            if packetDate:
                print('  Packet Sent Date: ' + str(packetDate))

        elif status == 2:
            print('  Application Status: Rejected')


    if "bottomBracket" in kwargs and kwargs["bottomBracket"] is True:
        print('|----------------------------------------------|')

