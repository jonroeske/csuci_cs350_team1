from Handlers.guiHandler import *
from Objects.camper import Camper

def createCamper():
    newCamper = Camper()

    try:
        newCamper.fullName = namePrompt()
        if(newCamper.fullName == 'EXIT' or newCamper.fullName == ''):
            return None

        check = 0

        while(check == 0):
            newCamper.age = agePrompt()
            if(newCamper.age == 'EXIT' or newCamper.age == ''):
                return None

            elif(newCamper.age >= 9 and newCamper.age <= 18):
                check = 1
            else:
                nonFatalError("Applicant must be between 9 and 18 years old.")

        check = 0

        while(check == 0):
            newCamper.gender = genderPrompt()
            if (newCamper.gender == 'EXIT' or newCamper.gender == ''):
                return None

            elif(newCamper.gender == 'F' or newCamper.gender == 'M'):
                check = 1
            else:
                nonFatalError('Applicant must be "M" or "F".')

        newCamper.address = addressPrompt()
        if(newCamper.address == 'EXIT' or newCamper.address == ''):
            return None

    except:
        exit("CODE 2: Exception during camper creation")

    while(1):
        clearScreen()
        confirmation = camperConfirmation(newCamper)

        if(confirmation == 'Y'):
            return newCamper

        elif(confirmation == 'N'):
            return None

        else:
            nonFatalError('Must be "Y" or "N"')


