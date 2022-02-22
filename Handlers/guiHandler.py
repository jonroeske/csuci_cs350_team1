import os

versionNumber = "Build Feb192022"

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def refreshScreen():
    clearScreen()
    print('|----------------Camp Clerk CLI----------------| ')
    print('| (1)  Help Prompt (TO DELETE LATER)           |')
    print('| (2)  Show Version                            |')
    print('|----------------------------------------------|')
    print('| (3)  Create New Camper                       |')
    print('| (4)  Show Camper Application Status          |')
    print('| (5)  Accept Camper Application               |')
    print('| (6)  Withdraw Camper Application             |')
    print('|----------------------------------------------|')
    print('| (7)  Show Current Camper Balance             |')
    print('| (8)  Reduce Camper Balance                   |')
    print('| (9)  Clear Camper Balance                    |')
    print('|----------------------------------------------|')
    print('| (10)  Show Camper Acceptance Status          |')
    print('| (11) Accept Camper Application               |')
    print('| (12) Decline Camper Application              |')
    print('|----------------------------------------------|')
    print('| (13) Show Camper Packet Status               |')
    print('| (14) Send Camper Packet                      |')
    print('|----------------------------------------------|')

def showVersion():
    refreshScreen()
    print('| VERSION NUMBER: ' + versionNumber + '              |')
    print('|----------------------------------------------|')

def namePrompt():
    refreshScreen()
    print('| Please insert camper name: (First + Last)    |')
    print('|  EXAMPLE: "John Doe"                         |')
    print('|----------------------------------------------|')

def agePrompt():
    refreshScreen()
    print('| Please insert camper age:                    |')
    print('|----------------------------------------------|')

def genderPrompt():
    refreshScreen()
    print('| Please insert camper gender:                 |')
    print('|  NOTE: "Male" or "Female" only, sue us later |')
    print('|----------------------------------------------|')