import Handlers.camperHandler
from Handlers.camperHandler import summerCamp

from Objects.values import STATUS_CODES

from GUI.guiHandler import camperSubMenu, clearScreen, showPrompt, showMessage
from GUI.camperCommandsGUI import printCamperGUI

def assignCamperToSession():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return
    elif camper.getAppStatus() != 1:
        printCamperGUI(camper, attribute="applicationStatus", topBracket=True, bottomBracket=True)
        showMessage('Camper must be accepted!')

        showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
        camperSubMenu()
        return
    elif camper.getSession() is not False:
        while True:
            printCamperGUI(camper, attribute="applicationStatus", topBracket=True, bottomBracket=True)
            confirmation = showPrompt(["Camper already has a session. Would you like to reassign?", "This will clear Camper's session, bunkhouse, and Tribe!"],
                                      prompt= '"Y" for Yes, "N" for No', topBracket=True, bottomBracket=True)

            if confirmation == 'Y':
                camper.setSession(False)
                camper.setBunkhouse(False)
                camper.setTribe(False)

                summerCamp.updateCamper(camper)

                break
            elif confirmation == 'N':
                camperSubMenu()
                showMessage("Action aborted.", bottomBracket=True)
                return
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)


    locations = [summerCamp.getJuneCampers(), summerCamp.getJulyCampers(), summerCamp.getAugustCampers()]

    while True:
        clearScreen()

        print('|----------------------------------------------|')
        print('| Sessions:                                    |')
        print('| (0)  June                                    |')
        print(f'        Availability: {sum(elem == "" for elem in summerCamp.getJuneCampers())}')
        print('| (1)  July                                    |')
        print(f'        Availability: {sum(elem == "" for elem in summerCamp.getJulyCampers())}')
        print('| (2)  August                                  |')
        print(f'        Availability: {sum(elem == "" for elem in summerCamp.getAugustCampers())}')
        print('|----------------------------------------------|')
        location = showPrompt("Which session would you like to assign?", bottomBracket=True)

        if int(location) != 0 and int(location) != 1 and int(location) != 2:
            showMessage("That is not a session!", bottomBracket=True, wait=2)
        else:
            if not any(elem == "" for elem in locations[int(location)]):
                showMessage("There is no availability in that session!", bottomBracket=True, wait=2)
            else:
                break

    # TODO - ADD LOGIC FOR PARTNER

    clearScreen()

    camper.setSession(int(location))
    summerCamp.updateCamper(camper)

    printCamperGUI(camper, attribute="session", topBracket=True, bottomBracket=True)
    showPrompt("Press 'Enter' to Return!", bottomBracket=True)
    camperSubMenu()


def assignCamperToBunkhouse():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        if (camper is None):
            pass  # TODO - WE NEED TO SET CONDITIONS FOR MISSPELLED NAMES

        session = camper.getSession()

        if (session == "June"):
            session = globals()["juneCampers"][1]
        elif (session == "July"):
            session = globals()["julyCampers"][1]
        elif (session == "August"):
            session = globals()["augustCampers"][1]
        elif session is None:
            camperSubMenu()
            print('| Camper must be assigned to a session!        |')
            print('|----------------------------------------------|')
            return

        maleOrFemaleBunkhouse = []

        if (camper.getGender() == 'M'):
            maleOrFemaleBunkhouse = [0, 1, 2]
        elif (camper.getGender() == 'F'):
            maleOrFemaleBunkhouse = [3, 4, 5]

        availability = [searchEmptySlot(session[maleOrFemaleBunkhouse[0]]),
                        searchEmptySlot(session[maleOrFemaleBunkhouse[1]]),
                        searchEmptySlot(session[maleOrFemaleBunkhouse[2]])]

        if camper.getAppStatus() != 1:
            camperSubMenu()
            print('| Camper must be accepted!                     |')
            print('|----------------------------------------------|')
            return

        elif not any(availability):
            camperSubMenu()
            print('| Sorry, all bunkhouses are full!              |')
            print('|----------------------------------------------|')
            return

        for bunkhouse in session:
            try:
                bunkhouse.index(camper)
                camperSubMenu()
                camperAlreadyEnrolled("bunkhouse")
                return
            except ValueError:
                pass
            # if this camper isn't a duplicate, then we want to create it

        while 1:

            clearScreen()

            print('|----------------------------------------------|')
            print('| What bunkhouse would you like to assign?     |')
            print('| (0)  Bunkhouse ' + str(maleOrFemaleBunkhouse[0] + 1) + '                             |')
            print(
                f'|  Availability: {maxCampersInBunkhouse - session[maleOrFemaleBunkhouse[0]].index(None)}' + '                            |')
            print('| (1)  Bunkhouse ' + str(maleOrFemaleBunkhouse[1] + 1) + '                             |')
            print(
                f'|  Availability: {maxCampersInBunkhouse - session[maleOrFemaleBunkhouse[1]].index(None)}' + '                            |')
            print('| (2)  Bunkhouse ' + str(maleOrFemaleBunkhouse[2] + 1) + '                             |')
            print(
                f'|  Availability: {maxCampersInBunkhouse - session[maleOrFemaleBunkhouse[2]].index(None)}' + '                            |')

            command = int(input(">> "))

            bunkhouse = session[maleOrFemaleBunkhouse[command]]

            if camper.getAssignmentRequest() is None and availability[bunkhouse]:
                bunkhouse[bunkhouse.index(None)] = camper
                camper.setBunkhouse(maleOrFemaleBunkhouse[command])
                break

            elif camper.getAssignmentRequest():
                slotsRemaining = maxCampersInBunkhouse - bunkhouse.index(None)
                partner = camper.getAssignmentRequest()

                if partner.getBunkhouse() is not None or partner.getSession() != camper.getSession():
                    bunkhouse[bunkhouse.index(None)] = camper
                    camper.setBunkhouse(maleOrFemaleBunkhouse[command])
                    break

                while 1:
                    confirmation = partnerPrompt(partner)

                    if confirmation == "Y" or confirmation == "N":
                        break
                    else:
                        nonFatalError("Incorrect Input!")

                if slotsRemaining > 1 and confirmation == "Y":
                    bunkhouse[bunkhouse.index(None)] = camper
                    camper.setBunkhouse(maleOrFemaleBunkhouse[command])

                    bunkhouse[bunkhouse.index(None)] = partner
                    partner.setBunkhouse(maleOrFemaleBunkhouse[command])
                    break

                elif slotsRemaining <= 1 and confirmation == "Y":
                    nonFatalError("There is not enough capacity for both campers!")

                elif confirmation == "N":
                    bunkhouse[bunkhouse.index(None)] = camper
                    camper.setBunkhouse(maleOrFemaleBunkhouse[command])
                    break

            else:
                nonFatalError('That bunkhouse is full!')

        camperSubMenu()
        print('| Camper successfully added to bunkhouse!      |')
        print('|----------------------------------------------|')


    except Exception as e:
        print(e)
        # mainMenu()
        # statusGetFailure()


def assignCamperToTribe():
    try:
        fullname = namePrompt()
        camper = searchCamperFullName(allCampers, fullname)

        if (camper is None):
            pass  # TODO - WE NEED TO SET CONDITIONS FOR MISSPELLED NAMES

        session = camper.getSession()

        if (session == "June"):
            session = globals()["juneCampers"][2]
        elif (session == "July"):
            session = globals()["julyCampers"][2]
        elif (session == "August"):
            session = globals()["augustCampers"][2]
        elif session is None:
            camperSubMenu()
            print('| Camper must be assigned to a session!        |')
            print('|----------------------------------------------|')
            return

        availability = [searchEmptySlot(session[0]),
                        searchEmptySlot(session[1]),
                        searchEmptySlot(session[2]),
                        searchEmptySlot(session[3]),
                        searchEmptySlot(session[4]),
                        searchEmptySlot(session[5])]

        if camper.getAppStatus() != 1:
            camperSubMenu()
            print('| Camper must be accepted!                     |')
            print('|----------------------------------------------|')
            return

        elif not any(availability):
            camperSubMenu()
            print('| Sorry, all tribes are full!                  |')
            print('|----------------------------------------------|')
            return

        for tribe in session:
            try:
                tribe.index(camper)
                camperSubMenu()
                camperAlreadyEnrolled("tribe")
                return
            except ValueError:
                pass
            # if this camper isn't a duplicate, then we want to create it

        while 1:

            clearScreen()

            print('|----------------------------------------------|')
            print('| What tribe would you like to assign?     |')
            print('| (0)  Tribe 1                                 |')
            print(
                f'|  Availability: {maxCampersInTribe - session[0].index(None)}' + '                            |')
            print('| (1)  Tribe 2                                 |')
            print(
                f'|  Availability: {maxCampersInTribe - session[1].index(None)}' + '                            |')
            print('| (2)  Tribe 3                                 |')
            print(
                f'|  Availability: {maxCampersInTribe - session[2].index(None)}' + '                            |')
            print('| (3)  Tribe 4                                 |')
            print(
                f'|  Availability: {maxCampersInTribe - session[3].index(None)}' + '                            |')
            print('| (4)  Tribe 5                                 |')
            print(
                f'|  Availability: {maxCampersInTribe - session[4].index(None)}' + '                            |')
            print('| (5)  Tribe 6                                 |')
            print(
                f'|  Availability: {maxCampersInTribe - session[5].index(None)}' + '                            |')

            command = int(input(">> "))

            tribe = session[command]

            if camper.getAssignmentRequest() is None and availability[tribe]:
                tribe[tribe.index(None)] = camper
                camper.setTribe(command)
                break

            elif camper.getAssignmentRequest():
                slotsRemaining = maxCampersInTribe - tribe.index(None)
                partner = camper.getAssignmentRequest()

                if partner.getTribe() is not None or partner.getSession() != camper.getSession():
                    tribe[tribe.index(None)] = camper
                    camper.setTribe(command)
                    break

                while 1:
                    confirmation = partnerPrompt(partner)

                    if confirmation == "Y" or confirmation == "N":
                        break
                    else:
                        nonFatalError("Incorrect Input!")

                if slotsRemaining > 1 and confirmation == "Y":
                    tribe[tribe.index(None)] = camper
                    camper.setTribe(command)

                    tribe[tribe.index(None)] = partner
                    partner.setTribe(command)
                    break

                elif slotsRemaining <= 1 and confirmation == "Y":
                    nonFatalError("There is not enough capacity for both campers!")

                elif confirmation == "N":
                    tribe[tribe.index(None)] = camper
                    camper.setTribe(command)
                    break

            else:
                nonFatalError('That tribe is full!')
        camperSubMenu()
        print('| Camper successfully added to tribe!          |')
        print('|----------------------------------------------|')


    except Exception as e:
        print(e)
        # mainMenu()
        # statusGetFailure()


def assignPairRequest():
    try:
        subjectname = namePrompt()
        subjectcamper = searchCamperFullName(allCampers, subjectname)

        if subjectcamper.getAssignmentRequest() is not None:
            print('| Camper already has request:                  |')
            print(f'|  {subjectcamper.getAssignmentRequest().getName()}')
            print('|----------------------------------------------|')
            print('| Press "Enter" to return!                     |')
            print('|----------------------------------------------|')
            input(">> ")
            camperSubMenu()
            return

        requestname = namePrompt()
        requestcamper = searchCamperFullName(allCampers, requestname)

        if requestcamper.getAssignmentRequest() is not None:
            print('| Camper already has request:                  |')
            print(f'|  {requestcamper.getAssignmentRequest().getName()}')
            print('|----------------------------------------------|')
            print('| Press "Enter" to return!                     |')
            print('|----------------------------------------------|')
            input(">> ")
            camperSubMenu()
            return

        if (subjectcamper.getGender() != requestcamper.getGender()):
            print('| Campers must have the same gender!           |')
            print('|----------------------------------------------|')
            print('| Press "Enter" to return!                     |')
            print('|----------------------------------------------|')
            input(">> ")
            camperSubMenu()
            return

        subjectcamper.setAssignmentRequest(requestcamper)
        requestcamper.setAssignmentRequest(subjectcamper)

        camperSubMenu()
        print(' Added pair request between ' + str(subjectcamper.getName()) + ' and ' + str(requestcamper.getName()))
        print('|----------------------------------------------|')
    except:
        camperSubMenu()
        statusGetFailure()