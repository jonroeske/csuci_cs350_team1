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
            printCamperGUI(camper, attribute="session", topBracket=True, bottomBracket=True)
            confirmation = showPrompt(["Camper already has a session. Would you like to reassign?",
                                       "This will clear Camper's session, bunkhouse, and Tribe!"],
                                      prompt='"Y" for Yes, "N" for No', bottomBracket=True)

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
    elif camper.getSession() is False:
        printCamperGUI(camper, attribute="session", topBracket=True, bottomBracket=True)
        showMessage('Camper must be assigned to a session!')

        showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
        camperSubMenu()
        return
    elif camper.getBunkhouse() is not False:
        while True:
            printCamperGUI(camper, attribute="bunkhouse", topBracket=True, bottomBracket=True)
            confirmation = showPrompt("Camper already has a bunkhouse. Would you like to reassign?",
                                      prompt='"Y" for Yes, "N" for No', bottomBracket=True)

            if confirmation == 'Y':
                camper.setBunkhouse(False)

                summerCamp.updateCamper(camper)

                break
            elif confirmation == 'N':
                camperSubMenu()
                showMessage("Action aborted.", bottomBracket=True)
                return
            else:
                showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    locations = [summerCamp.getJuneBunkhouses(), summerCamp.getJulyBunkhouses(), summerCamp.getAugustBunkhouses()]
    session = locations[int(camper.getSession())]

    while True:
        clearScreen()

        gender = camper.getGender()

        # TODO - COMPREHRENSION CHECK: FIRST THREE BUNKHOUSES ARE MALE, SECOND THREE ARE FEMALE
        if gender == "M":
            print('|----------------------------------------------|')
            print('| Bunkhouses:                                  |')
            print('| (0)  Bunkhouse 1                             |')
            print(f'        Availability: {sum(elem == "" for elem in session[0])}')
            print('| (1)  Bunkhouse 2                             |')
            print(f'        Availability: {sum(elem == "" for elem in session[1])}')
            print('| (2)  Bunkhouse 3                             |')
            print(f'        Availability: {sum(elem == "" for elem in session[2])}')
            print('|----------------------------------------------|')

        elif gender == "F":
            print('|----------------------------------------------|')
            print('| Bunkhouses:                                  |')
            print('| (0)  Bunkhouse 4                             |')
            print(f'        Availability: {sum(elem == "" for elem in session[3])}')
            print('| (1)  Bunkhouse 5                             |')
            print(f'        Availability: {sum(elem == "" for elem in session[4])}')
            print('| (2)  Bunkhouse 6                             |')
            print(f'        Availability: {sum(elem == "" for elem in session[5])}')
            print('|----------------------------------------------|')

        try:
            location = int(showPrompt("Which bunkhouse would you like to assign?", bottomBracket=True))
        except ValueError:
            showMessage("Invalid input!", bottomBracket=True, wait=2)
            continue

        if not 0 <= location <= 2:
            showMessage("That is not a session!", bottomBracket=True, wait=2)
        else:
            if gender == "F":
                location += 3

            if not any(elem == "" for elem in session[location]):
                showMessage("There is no availability in that session!", bottomBracket=True, wait=2)
            else:
                camper.setBunkhouse(location)
                break

    # TODO - ADD LOGIC FOR PARTNER

    clearScreen()

    summerCamp.updateCamper(camper)

    printCamperGUI(camper, attribute="bunkhouse", topBracket=True, bottomBracket=True)
    showPrompt("Press 'Enter' to Return!", bottomBracket=True)
    camperSubMenu()


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
