from Handlers.guiHandler import *
from Objects.camper import Camper

def createCamper():

    clearScreen()

    newCamper = Camper()

    try:
        newCamper.fullName = namePrompt()
        newCamper.age = agePrompt()
        newCamper.gender = genderPrompt()
        newCamper.address = addressPrompt()

        #newCamper.session = "unassigned"
        #newCamper.appstatus = "pending"
        #newCamper.balance = "pending"
        #newCamper.tribe = "unassigned"
        #newCamper.bunkhouse = "unassigned"
        #newCamper.acceptstatus = "pending"
        #newCamper.arrivalreqcert = "unassigned"
        #newCamper.checkedin = "false"
        #newcamper.assignmentrequest = "unassigned"
        #newcamper.datesentnotice = "pending"
        #newcamper.packetstatus = "pending"

    except:
        exit("CODE 2: Exception during camper creation")

    maxErrorCounter = 0 #If they fuck up this many times, just leave lmao

    while(maxErrorCounter < 3):

        clearScreen()
        confirmation = camperConfirmation(newCamper)

        if(confirmation == 'Y'):
            return newCamper

        elif(confirmation == 'N'):
            return None

        else:
            nonFatalError()
            maxErrorCounter += 1

    return None