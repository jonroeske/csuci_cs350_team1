import sys

from Handlers.camperHandler import *

def statusHandler(status, index, argv):
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