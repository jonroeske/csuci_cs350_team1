# CLI System
import sys

from docHandler.docHandler import submitApplication
from guiHandler.guiHandler import *


def statushandler(status, index, argv):
    argsarr = str(argv)
    if status == 1:
        try:  # Calls findCamper()
            fullname = argsarr[index+1]
            camper = findCamper(fullname)
            camper.printApplication()
        except:
            print('Cannot find camper')
    if status == 2:
        try:  # Calls submitApplication()
            fullname = argsarr[index + 1]
            age = argsarr[index + 2]
            gender = argsarr[index + 3]
            address = argsarr[index + 4]
            session = argsarr[index + 5].lower()
            submitApplication(fullname, age, gender, address, session)
        except:
            print('Not all required fields present')
    if status == 3:
        try:  # Calls removeCamper()
            fullname = argsarr[index + 1]
            removeCamper(fullname)
        except:
            print('Cannot find camper')
    if status == 4:
        try:  # Calls findCamper() & printBalance()
            fullname = argsarr[index + 1]
            camper = findCamper(fullname)
            camper.printBalance()
        except:
            print('Cannot find camper')
    if status == 5:
        try:  # Calls balance functions
            fullname = argsarr[index + 1]
            amount = argsarr[index + 2]
            if amount > 0:
                raiseBalance(fullname, amount)
            elif amount < 0:
                reduceBalance(fullname, amount)
            elif amount == 0:
                resetBalance(fullname)
        except:
            print('Cannot find camper')
    if status == 6:
        try:  # Calls resetBalance()
            fullname = argsarr[index + 1]
            resetBalance(fullname)
        except:
            print('Cannot find camper')
    if status == 7:
        try:  # Calls printAcceptance()
            fullname = argsarr[index + 1]
            camper = findCamper(fullname)
            camper.printAcceptance()
        except:
            print('Cannot find camper')
    if status == 8:
        try:  # Calls camperAcceptedNotice()
            fullname = argsarr[index + 1]
            date = argsarr[index + 2]
            camperAcceptedNotice(fullname, date)
        except:
            print('Cannot find camper')
    if status == 9:
        try:  # Calls camperDeclinedNotice()
            fullname = argsarr[index + 1]
            date = argsarr[index + 2]
            camperDeclinedNotice(fullname, date)
        except:
            print('Cannot find camper')
    if status == 10:
        try:  # Calls printPacket()
            fullname = argsarr[index + 1]
            camper = findCamper(fullname)
            camper.printPacket()
        except:
            print('Cannot find camper')
    if status == 11:
        try:  # Calls instructionPacketSent()
            fullname = argsarr[index + 1]
            instructionPacketSent(fullname)
        except:
            print('Invalid arg field')


def main(argv):
    status = 0
    index = 0

    refreshScreen()
    while(1):
        varInput = int(input(">> "))
        match varInput:
            case 1:
                index += 1
                refreshScreen()
            case 2:
                index += 1
                refreshScreen()
                print('| VERSION NUMBER: ' + versionNumber + '      |')
                print('|--------------------------------------|')
            case 3:
                index += 1
            case 4:
                index += 1
            case 5:
                index += 1
            case 6:
                index += 1
            case 7:
                index += 1
            case 8:
                index += 1
            case 9:
                index += 1
            case 10:
                index += 1
            case 11:
                index += 1
            case 12:
                index += 1
            case 13:
                index += 1
            case _:
                index += 1
                mainMenu()


main(sys.argv[1:])

"""
    #ORIGINAL CODE

    status = 0
    index = 0
    argsarr = str(argv)
    for arg in argsarr:
        if arg == 'h':
            index += 1
            helpprompt()
            sys.exit(2)
        if arg == 'v':
            index += 1
            print('Build Feb192022')
            sys.exit(2)
        if arg == 'a':  # Grabs camper obj and prints app status
            index += 1
            statushandler(1, index, argsarr)
            sys.exit(2)
        if arg == 'an':  # Creates new camper obj
            index += 1
            statushandler(2, index, argsarr)
            sys.exit(2)
        if arg == 'aw':  # Removes camper obj
            index += 1
            statushandler(3, index, argsarr)
            sys.exit(2)
        if arg == 'b':  # Grabs camper obj and prints balance
            index += 1
            statushandler(4, index, argsarr)
            sys.exit(2)
        if arg == 'br':  # Modifies balance field in camper obj
            index += 1
            statushandler(5, index, argsarr)
            sys.exit(2)
        if arg == 'bc':  # Sets balance field to 0 in camper obj
            index += 1
            statushandler(6, index, argsarr)
            sys.exit(2)
        if arg == 'n':  # Grabs camper obj and prints acceptance status
            index += 1
            statushandler(7, index, argsarr)
            sys.exit(2)
        if arg == 'na':  # Modifies acceptance status field in camper obj to accepted
            index += 1
            statushandler(8, index, argsarr)
            sys.exit(2)
        if arg == 'nd':  # Modifies acceptance status field in camper obj to declined
            index += 1
            statushandler(9, index, argsarr)
            sys.exit(2)
        if arg == 'i':  # Grabs camper obj and prints packet status
            index += 1
            statushandler(10, index, argsarr)
            sys.exit(2)
        if arg == 'is':  # Modifies packet status field to sent & date
            index += 1
            statushandler(11, index, argsarr)
            sys.exit(2)
        else:
            index += 1
"""