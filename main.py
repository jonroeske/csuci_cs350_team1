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