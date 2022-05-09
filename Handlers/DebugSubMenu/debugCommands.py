from Handlers.camperHandler import summerCamp

from Handlers.guiHandler import *

from Objects.camp import Camp
from Objects.camper import Camper
from Objects.values import STATUS_CODES, changeDate, resetDate

# When we get Docker working, remove this!
from faker import Faker

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

    mainMenu()
    showMessage("Date change successful!", bottomBracket=True)


def resetTodaysDate():
    resetDate()
    mainMenu()
    showMessage("Date reset successful!", bottomBracket=True)


def populateMaxCampers():

    print('| Creating max campers...                      |')
    print('|----------------------------------------------|')

    random.seed()
    fake = Faker()

    global summerCamp

    for camper in summerCamp.getAllCampers():
        if camper == "":
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

            try:
                summerCamp.insertCamper(newCamper)
            except Exception as e:
                pass
                # we shouldn't be getting this error, as above the empty check confirms
                #  there is an empty slot to use


    for camper in summerCamp.getAllCampers():

        try:
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
                            try:
                                index = random.randint(0, len(matchingCampers) - 1)

                                partner = matchingCampers[index]

                                camper.setHasPartner(True)
                                partner.setHasPartner(True)

                                camper.setPartner(partner)
                                partner.setPartner(camper)

                                summerCamp.updateCamper(camper)
                                summerCamp.updateCamper(partner)
                            except Exception as e:
                                print(e)

        except Exception as e:
            print(e)

    summerCamp.getAllCampers().sort()

    time.sleep(1)

    mainMenu()
    print('| Max campers created, calm down there God...  |')
    print('|----------------------------------------------|')


def resetAllCampers():
    print('| Clearing all campers...                      |')
    print('|----------------------------------------------|')

    global summerCamp
    summerCamp.__init__()

    time.sleep(1)

    mainMenu()
    print('| Cleared all campers, you monster!            |')
    print('|----------------------------------------------|')


def resetSessions():
    print('| Resetting all sessions...                    |')
    print('|----------------------------------------------|')

    time.sleep(1)

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
