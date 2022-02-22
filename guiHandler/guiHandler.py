import os

versionNumber = "Build Feb192022"

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def refreshScreen():
    clearScreen()
    print('|------------Camp Clerk CLI------------| ')
    print('| (1)  Help Prompt (TO DELETE LATER)   |')
    print('| (2)  Show Version                    |')
    print('|--------------------------------------|')
    print('| (3)  Show Camper Application Status  |')
    print('| (4)  Withdraw Camper Application     |')
    print('| (5)  Withdraw Camper Application     |')
    print('|--------------------------------------|')
    print('| (6)  Show Current Camper Balance     |')
    print('| (7)  Reduce Camper Balance           |')
    print('| (8)  Clear Camper Balance            |')
    print('|--------------------------------------|')
    print('| (9)  Show Camper Acceptance Status   |')
    print('| (10) Accept Camper Application       |')
    print('| (11) Decline Camper Application      |')
    print('|--------------------------------------|')
    print('| (12) Show Camper Packet Status       |')
    print('| (13) Send Camper Packet              |')
    print('|--------------------------------------|')
