# Clerk logic for handling summerCamp documents
import datetime
from Objects.camper import Camper


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
