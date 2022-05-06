# Clerk logic for handling summerCamp documents
import datetime
from Objects.camper import Camper

def submitApplication(fullname, age, gender, address, session):  # create camper obj using fields
    newCamper = Camper(fullname, age, gender, address, session)

    if newCamper.session == 1 and checkApplicationDate(newCamper):
        juneCampers.append(newCamper)
        return True
    elif newCamper.session == 2 and checkApplicationDate(newCamper):
        julyCampers.append(newCamper)
        return True
    elif newCamper.session == 3 and checkApplicationDate(newCamper):
        augustCampers.append(newCamper)
        return True
    else:
        print("Error assigning Camper to summerCamp session.")
        return False


def checkApplicationDate(Camper):  # checks application date to session start date
    current_time = datetime.datetime.now()

    if Camper.session == 1:
        difference = current_time.month - 6
        if 5 > difference:
            print("Application DENIED:")
            print("Please reapply with five months of camps start date.")
            return False
        elif difference < 2:
            print("Application DENIED:")
            print("Cannot apply within two month of start date.")
            print("Please apply to another session.")
            return False
        else:
            return True

    if Camper.session == 2:
        difference = current_time.month - 7
        if 5 > difference:
            print("Application DENIED:")
            print("Please reapply with five months of camps start date.")
            return False
        elif difference < 2:
            print("Application DENIED:")
            print("Cannot apply within two month of start date.")
            print("Please apply to another session.")
            return False
        else:
            return True

    if Camper.session == 3:
        difference = current_time.month - 8
        if 5 > difference:
            print("Application DENIED:")
            print("Please reapply with five months of camps start date.")
            return False
        elif difference < 2:
            print("Application DENIED:")
            print("Cannot apply within two month of start date.")
            print("Please apply to another session.")
            return False
        else:
            return True


def withdrawApplication(fullname):  # remove camper obj
    for juneCamper in juneCampers:
        if juneCamper.fullname == fullname:
            juneCampers.remove(juneCamper)
            return True
    for julyCamper in julyCampers:
        if julyCamper.fullname == fullname:
            julyCampers.remove(julyCamper)
            return True
    for augustCamper in augustCampers:
        if augustCamper.fullname == fullname:
            augustCampers.remove(augustCamper)
            return True
    return False


def reduceBalance(fullname, amount):  # reduce balance in camper obj by amount
    for juneCamper in juneCampers:
        if juneCamper.fullname == fullname:
            juneCamper.balance -= amount
            return True
    for julyCamper in julyCampers:
        if julyCamper.fullname == fullname:
            julyCamper.balance -= amount
            return True
    for augustCamper in augustCampers:
        if augustCamper.fullname == fullname:
            augustCamper.balance -= amount
            return True
    return False


def raiseBalance(fullname, amount):  # raise balance in camper obj by amount
    for juneCamper in juneCampers:
        if juneCamper.fullname == fullname:
            juneCamper.balance += amount
            return True
    for julyCamper in julyCampers:
        if julyCamper.fullname == fullname:
            julyCamper.balance += amount
            return True
    for augustCamper in augustCampers:
        if augustCamper.fullname == fullname:
            augustCamper.balance += amount
            return True
    return False


def resetBalance(fullname):  # zero balance in camper obj
    for juneCamper in juneCampers:
        if juneCamper.fullname == fullname:
            juneCamper.balance = 0
            return True
    for julyCamper in julyCampers:
        if julyCamper.fullname == fullname:
            julyCamper.balance = 0
            return True
    for augustCamper in augustCampers:
        if augustCamper.fullname == fullname:
            augustCamper.balance = 0
            return True
    return False


def sentAcceptanceNotice(fullname, date):  # sent acceptance notice to camper on date
    if date == null:
        for juneCamper in juneCampers:
            if juneCamper.fullname == fullname:
                juneCamper.datesentnotice = datetime.datetime.now()
                return True
        for julyCamper in julyCampers:
            if julyCamper.fullname == fullname:
                julyCamper.datesentnotice = datetime.datetime.now()
                return True
        for augustCamper in augustCampers:
            if augustCamper.fullname == fullname:
                augustCamper.datesentnotice = datetime.datetime.now()
                return True
        return False
    else:
        for juneCamper in juneCampers:
            if juneCamper.fullname == fullname:
                juneCamper.datesentnotice = date
                return True
        for julyCamper in julyCampers:
            if julyCamper.fullname == fullname:
                julyCamper.datesentnotice = date
                return True
        for augustCamper in augustCampers:
            if augustCamper.fullname == fullname:
                augustCamper.datesentnotice = date
                return True
        return False


def camperAcceptedNotice(fullname, date):  # camper accepted notice on date
    for juneCamper in juneCampers:
        if juneCamper.fullname == fullname:
            if juneCamper.datesentnotice.date[2] - date.date[2] <= 2:
                juneCamper.acceptstatus = True
            return True
    for julyCamper in julyCampers:
        if julyCamper.fullname == fullname:
            if julyCamper.datesentnotice.date[2] - date.date[2] <= 2:
                julyCamper.acceptstatus = True
            return True
    for augustCamper in augustCampers:
        if augustCamper.fullname == fullname:
            if augustCamper.datesentnotice.date[2] - date.date[2] <= 2:
                augustCamper.acceptstatus = True
            return True
    return False


def camperDeclinedNotice(fullname, date):  # camper declined notice on date
    for juneCamper in juneCampers:
        if juneCamper.fullname == fullname:
            if juneCamper.datesentnotice < date:
                juneCamper.acceptstatus = False
            return True
    for julyCamper in julyCampers:
        if julyCamper.fullname == fullname:
            if julyCamper.datesentnotice < date:
                julyCamper.acceptstatus = False
            return True
    for augustCamper in augustCampers:
        if augustCamper.fullname == fullname:
            if augustCamper.datesentnotice < date:
                augustCamper.acceptstatus = False
            return True
    return False


def instructionPacketSent(fullname):  # first day instruction packet sent to camper
    for juneCamper in juneCampers:
        if juneCamper.fullname == fullname:
            if juneCamper.acceptstatus:
                juneCamper.packetstatus = True
            else:
                print("Camper has not accepted")
                return False
            return True
    for julyCamper in julyCampers:
        if julyCamper.fullname == fullname:
            if julyCamper.acceptstatus:
                julyCamper.packetstatus = True
            else:
                print("Camper has not accepted")
                return False
            return True
    for augustCamper in augustCampers:
        if augustCamper.fullname == fullname:
            if augustCamper.acceptstatus:
                augustCamper.packetstatus = True
            else:
                print("Camper has not accepted")
                return False
            return True
    return False
