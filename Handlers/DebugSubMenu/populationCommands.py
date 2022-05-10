from Handlers.dataHandler import summerCamp
from Handlers.guiHandler import *
from Objects.camp import Camp
from Objects.camper import Camper
from Objects.values import STATUS_CODES

# When we get Docker working, remove this!
from Libraries.faker.proxy import Faker

import random

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

    for location in locations:
        for camper in location[0]:
            if isinstance(camper, Camper):
                camper.setSession(False)
                camper.setBunkhouse(False)
                camper.setTribe(False)
                summerCamp.updateCamper(camper)

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


def resetBunkhouses():
    showMessage("Resetting all bunkhouses...", bottomBracket=True, wait=1)

    locations = [summerCamp.getJuneBunkhouses(), summerCamp.getJulyBunkhouses(), summerCamp.getAugustBunkhouses()]

    for location in locations:
        for bunkhouse in location:
            for camper in bunkhouse:
                if isinstance(camper, Camper):
                    camper.setBunkhouse(False)
                    summerCamp.updateCamper(camper)

    summerCamp.setJuneBunkhouses([["" for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"])] for _ in range(GLOBAL_VALUES["maxBunkhouses"])])
    summerCamp.setJulyBunkhouses([["" for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"])] for _ in range(GLOBAL_VALUES["maxBunkhouses"])])
    summerCamp.setAugustBunkhouses([["" for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"])] for _ in range(GLOBAL_VALUES["maxBunkhouses"])])

    clearScreen()
    debugSubMenu()

    showMessage("All bunkhouses reset!", bottomBracket=True)


def resetTribes():
    showMessage("Resetting all tribes...", bottomBracket=True, wait=1)

    locations = [summerCamp.getJuneTribes(), summerCamp.getJulyTribes(), summerCamp.getAugustTribes()]

    for location in locations:
        for tribe in location:
            for camper in tribe:
                if isinstance(camper, Camper):
                    camper.setTribe(False)
                    summerCamp.updateCamper(camper)

    summerCamp.setJuneTribes([["" for _ in range(GLOBAL_VALUES["maxCampersInTribe"])] for _ in range(GLOBAL_VALUES["maxTribes"])])
    summerCamp.setJulyTribes([["" for _ in range(GLOBAL_VALUES["maxCampersInTribe"])] for _ in range(GLOBAL_VALUES["maxTribes"])])
    summerCamp.setAugustTribes([["" for _ in range(GLOBAL_VALUES["maxCampersInTribe"])] for _ in range(GLOBAL_VALUES["maxTribes"])])

    clearScreen()
    debugSubMenu()

    showMessage("All tribes reset!", bottomBracket=True)
