from Handlers.camperHandler import summerCamp

from Handlers.guiHandler import *

from Objects.camp import Camp
from Objects.camper import Camper
from Objects.values import STATUS_CODES, changeDate, resetDate

# When we get Docker working, remove this!
from Libraries.faker.proxy import Faker

import time, random

def changeTodaysDate():
    while True:
        clearScreen()
        date = showPrompt("What would you like to set today's date to?",
                          prompt=["(Month)/(Day)/(Year)", "Example: 12/25/1998", "Press 'Enter' to Return!"], topBracket=True, bottomBracket=True)

        if date == "":
            mainMenu()
            return


        result = changeDate(date)

        if result == STATUS_CODES["ARGUMENT_ERROR"]:
            showMessage("Invalid input!", bottomBracket=True, wait=2)
        elif result == STATUS_CODES["SUCCESS"]:
            break

    clearScreen()
    debugSubMenu()
    showMessage("Date change successful!", bottomBracket=True)


def resetTodaysDate():
    resetDate()

    debugSubMenu()
    showMessage("Date reset successful!", bottomBracket=True)


def populateMaxCampers():

    showMessage("Populating maximum amount of campers...", bottomBracket=True, wait=1)


    random.seed()
    fake = Faker()

    global summerCamp


    while True:
        if not any(elem == "" for elem in summerCamp.getAllCampers()):
            break

        for camper in summerCamp.getAllCampers():
            if isinstance(camper, str):
                newCamper = Camper()
                while True:
                    genders = summerCamp.countGender()
                    if genders[0] <= genders[1]:
                        newCamper.setName(fake.first_name_male() + ' ' + fake.last_name_male())
                        newCamper.setGender('M')

                    elif genders[0] > genders[1]:
                        newCamper.setName(fake.first_name_female() + ' ' + fake.last_name_female())
                        newCamper.setGender('F')

                    newCamper.setAge(random.randint(9, 18))
                    newCamper.setAddress(fake.street_address())

                    if newCamper.searchByFullName(summerCamp.getAllCampers()) == STATUS_CODES["NO_CAMPER"]:
                        break

                summerCamp.insertCamper(newCamper)



    for camper in summerCamp.getAllCampers():
        if camper.getHasPartner() is False:
            # Here we find all campers with the same last name
            matchingCampers = camper.searchByLastName(summerCamp.getAllCampers())

            if matchingCampers != STATUS_CODES["NO_CAMPER"]:

                # Here we find all campers with the same last name and gender
                #  We can't pair up two campers of different genders
                matchingCampers = camper.searchByGender(matchingCampers)

                if matchingCampers != STATUS_CODES["NO_CAMPER"]:

                    chanceRequest = random.randint(1, 4)
                    if chanceRequest == 4:
                        index = random.randint(0, len(matchingCampers) - 1)

                        partner = matchingCampers[index]

                        camper.setHasPartner(True)
                        partner.setHasPartner(True)

                        camper.setPartner(partner)
                        partner.setPartner(camper)

                        summerCamp.updateCamper(camper)
                        summerCamp.updateCamper(partner)

    clearScreen()
    debugSubMenu()

    showMessage("Maximum amount of campers populated!", bottomBracket=True)


def resetAllCampers():
    showMessage("Resetting all campers...", bottomBracket=True, wait=1)

    global summerCamp
    summerCamp.__init__()

    clearScreen()
    debugSubMenu()

    showMessage("All campers reset!", bottomBracket=True)


def resetSessions():
    showMessage("Resetting all sessions...", bottomBracket=True, wait=1)

    locations = [summerCamp.getJune(), summerCamp.getJuly(), summerCamp.getAugust()]

    for locations in locations:
        for camper in locations[0]:
            camper.setSession(False)
            camper.setBunkhouse(False)
            camper.setTribe(False)

    summerCamp.setJune([["" for _ in range(GLOBAL_VALUES["maxCampersInSession"])],
                            [["" for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"])] for _ in
                             range(GLOBAL_VALUES["maxBunkhouses"])],
                            [["" for _ in range(GLOBAL_VALUES["maxCampersInTribe"])] for _ in
                             range(GLOBAL_VALUES["maxTribes"])]])
    summerCamp.setJuly([["" for _ in range(GLOBAL_VALUES["maxCampersInSession"])],
                            [["" for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"])] for _ in
                             range(GLOBAL_VALUES["maxBunkhouses"])],
                            [["" for _ in range(GLOBAL_VALUES["maxCampersInTribe"])] for _ in
                             range(GLOBAL_VALUES["maxTribes"])]])
    summerCamp.setAugust([["" for _ in range(GLOBAL_VALUES["maxCampersInSession"])],
                            [["" for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"])] for _ in
                             range(GLOBAL_VALUES["maxBunkhouses"])],
                            [["" for _ in range(GLOBAL_VALUES["maxCampersInTribe"])] for _ in
                             range(GLOBAL_VALUES["maxTribes"])]])
    clearScreen()
    debugSubMenu()

    showMessage("All sessions reset!", bottomBracket=True)


def databaseView():
    global summerCamp

    print()
    print('|----------------------------------------------|')
    print("ALL CAMPERS LIST:")
    print(summerCamp.getAllCampers())
    print('|----------------------------------------------|')
    print("JUNE CAMPERS LIST:")
    print(" JUNE CAMPERS:")
    print(summerCamp.getJuneCampers())
    print(" JUNE BUNKHOUSES:")
    print(summerCamp.getJuneBunkhouses())
    print(" JUNE TRIBES:")
    print(summerCamp.getJuneTribes())
    print('|----------------------------------------------|')
    print("JULY CAMPERS LIST:")
    print(" JULY CAMPERS:")
    print(summerCamp.getJulyCampers())
    print(" JULY BUNKHOUSES:")
    print(summerCamp.getJulyBunkhouses())
    print(" JULY TRIBES:")
    print(summerCamp.getJulyTribes())
    print('|----------------------------------------------|')
    print("AUGUST CAMPERS LIST:")
    print(" AUGUST CAMPERS:")
    print(summerCamp.getAugustCampers())
    print(" AUGUST BUNKHOUSES:")
    print(summerCamp.getAugustBunkhouses())
    print(" AUGUST TRIBES:")
    print(summerCamp.getAugustTribes())
    print('|----------------------------------------------|')
