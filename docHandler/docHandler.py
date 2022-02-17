# Clerk logic for handling camp documents
import datetime
from objects.camper import Camper

juneCampers = []
julyCampers = []
augustCampers = []

def submitApplication(fullname, age, gender, address, session): # create camper obj using fields
    newCamper = Camper(fullname, age, gender, address, session)

    if newCamper.session == "june" and checkApplicationDate(newCamper):
        juneCampers.append(newCamper)
    elif newCamper.session == "july" and checkApplicationDate(newCamper):
        julyCampers.append(newCamper)
    elif newCamper.session == "august" and checkApplicationDate(newCamper):
        augustCampers.append(newCamper)
    else:
        print("Error assigning Camper to camp session.")

def checkApplicationDate(Camper):# checks application date to session start date
    current_time = datetime.datetime.now()

    if Camper.session == "june":
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

    if Camper.session == "july":
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

    if Camper.session == "august":
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



def withdrawApplication(fullname): # remove camper obj


def reduceBalance(fullname, amount): # reduce balance in camper obj by amount


def raiseBalance(fullname, amount): # raise balance in camper obj by amount


def resetBalance(fullname): # zero balance in camper obj


def sentAcceptanceNotice(fullname, date): # sent acceptance notice to camper on date


def camperAcceptedNotice(fullname, date): # camper accepted notice on date


def camperDeclinedNotice(fullname, date): # camper declined notice on date


def instructionPacketSent(fullname): # first day instruction packet sent to camper


