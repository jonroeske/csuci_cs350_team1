from Handlers.dataHandler import summerCamp

from Handlers.uiHandler import *

# TODO - DEBUGGING
def viewSessions():
    try:
        clearScreen()
        print('|----------------------------------------------|')
        print('| Sessions:                                    |')


        print(f'   June:')
        print(f'    Amount: {sum(elem != "" for elem in summerCamp.getJuneCampers())}')
        genders = summerCamp.countGender(session=0)
        print(f'    Composition: {genders[0]} Male(s), {genders[1]} Female(s)')

        for camper in summerCamp.getJuneCampers():
            if isinstance(camper, Camper):
                printCamperUI(camper, simple=True)

        print(f'   July:')
        print(f'    Amount: {sum(elem != "" for elem in summerCamp.getJulyCampers())}')
        genders = summerCamp.countGender(session=1)
        print(f'    Composition: {genders[0]} Male(s), {genders[1]} Female(s)')

        for camper in summerCamp.getJulyCampers():
            if isinstance(camper, Camper):
                if isinstance(camper, Camper):
                    printCamperUI(camper, simple=True)

        print(f'   July:')
        print(f'    Amount: {sum(elem != "" for elem in summerCamp.getAugustCampers())}')
        genders = summerCamp.countGender(session=2)
        print(f'    Composition: {genders[0]} Male(s), {genders[1]} Female(s)')

        for camper in summerCamp.getAugustCampers():
            if isinstance(camper, Camper):
                printCamperUI(camper, simple=True)

        showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
        mainMenu()

    except Exception as e:
        print(e)
        mainMenu()
        statusGetFailure()


# TODO - DEBUGGING
def viewBunkhouses():
    try:
        locations = [summerCamp.getJuneBunkhouses(), summerCamp.getJulyBunkhouses(), summerCamp.getAugustBunkhouses()]

        while True:
            clearScreen()
            print('|----------------------------------------------|')
            print('| Sessions:                                    |')
            print('| (0)  June                                    |')
            print('| (1)  July                                    |')
            print('| (2)  August                                  |')
            print('|----------------------------------------------|')
            try:
                location = int(showPrompt("Which session would you like to view?", bottomBracket=True))
            except ValueError:
                showMessage("Invalid input!", bottomBracket=True, wait=2)
                continue

            if location != 0 and location != 1 and location != 2:
                showMessage("That is not a session!", bottomBracket=True, wait=2)
            else:
                break

        clearScreen()

        bunkhouseNumber = 1
        for bunkhouse in locations[location]:
            print(f'  Bunkhouse {bunkhouseNumber}:')

            print(f'   Amount: {sum(x != "" for x in bunkhouse)}')

            for camper in bunkhouse:
                printCamperUI(camper, simple=True)
            bunkhouseNumber += 1

        showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
        mainMenu()

    except Exception as e:
        print(e)
        mainMenu()
        statusGetFailure()


# TODO - DEBUGGING
def viewTribes():
    try:
        locations = [summerCamp.getJuneTribes(), summerCamp.getJulyTribes(), summerCamp.getAugustTribes()]

        while True:
            clearScreen()
            print('|----------------------------------------------|')
            print('| Sessions:                                    |')
            print('| (0)  June                                    |')
            print('| (1)  July                                    |')
            print('| (2)  August                                  |')
            print('|----------------------------------------------|')

            try:
                location = int(showPrompt("Which session would you like to view?", bottomBracket=True))
            except ValueError:
                showMessage("Invalid input!", bottomBracket=True, wait=2)
                continue

            if location != 0 and location != 1 and location != 2:
                showMessage("That is not a session!", bottomBracket=True, wait=2)
            else:
                break

        clearScreen()

        bunkhouseNumber = 1
        for bunkhouse in locations[location]:
            print(f'  Tribe {bunkhouseNumber}:')

            print(f'   Amount: {sum(x != "" for x in bunkhouse)}')

            for camper in bunkhouse:
                printCamperUI(camper, simple=True)
            bunkhouseNumber += 1

        showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
        mainMenu()

    except Exception as e:
        print(e)
        mainMenu()
        statusGetFailure()
