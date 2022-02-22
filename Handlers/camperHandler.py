from Handlers.guiHandler import *
from objects.camper import Camper

def createCamper():
    refreshScreen()
    namePrompt()
    camperFullname: str = input(">> ")

    refreshScreen()
    agePrompt()
    camperAge: str = input(">> ")

    refreshScreen()
    genderPrompt()
    camperGender: str = input(">> ")

    newCamper = Camper(camperFullname, camperAge, camperGender)

    refreshScreen()

    input()
    return newCamper