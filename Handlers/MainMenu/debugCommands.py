import Handlers.camperHandler
from Handlers.camperHandler import summerCamp

from Handlers.guiHandler import *

from Objects.camp import Camp
from Objects.camper import Camper
from Objects.values import STATUS_CODES, changeDate, resetDate

# When we get Docker working, remove this!
from faker import Faker

import time, random

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
            if camper.getAssignmentRequest() is False:
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

                                camper.setAssignmentRequest(True)
                                partner.setAssignmentRequest(True)

                                camper.setAssignment(partner)
                                partner.setAssignment(camper)

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


def clearAllCampers():
    print('| Clearing all campers...                      |')
    print('|----------------------------------------------|')

    global summerCamp
    summerCamp.__init__()

    time.sleep(1)

    mainMenu()
    print('| Cleared all campers, you monster!            |')
    print('|----------------------------------------------|')


def changeTodaysDate():
    while True:
        clearScreen()
        date = showPrompt("What would you like to set today's date to?",
                          prompt=["(Month)/(Day)/(Year)", "Example: 12/25/1998"], topBracket=True, bottomBracket=True)

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






