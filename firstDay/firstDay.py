import operator


# Clerk logic for handling day one of camp sessions
def checkInCert(camper):  # Verifies required forms for arrival packet
    camper.checkedIn = False

    print('--------Campers Arrival Packet--------')
    print('Please answer the following questions with "Y" for Yes, "N" for No')
    camper.medical = input('Does the camper have his/her medical information filled out? ')
    camper.legal = input('Does the camper have his/her legal information filled out? ')
    camper.emergencyContacts = input('Does the camper have his/her emergency contacts filled out? ')

    if camper.medical == "Y":
        camper.medical = True
    else:
        camper.medical = False
    if camper.legal == "Y":
        camper.legal = True
    else:
        camper.legal = False
    if camper.emergencyContacts == "Y":
        camper.emergencyContacts = True
    else:
        camper.emergencyContacts = False

    print('--------Campers Required Equipment--------')
    print('Please answer the following questions with "Y" for Yes, "N" for No')
    camper.helmet = input('Does the camper have his/her riding helmet? ')
    camper.boots = input('Does the camper have his/her boots? ')
    camper.sleepingBag = input('Does the camper have his/her sleeping bag? ')
    camper.waterBottle = input('Does the camper have his/her water bottle? ')
    camper.sunscreen = input('Does the camper have his/her sun screen? ')
    camper.bugSpray = input('Does the camper have his/her bug spray? ')

    if camper.helmet == "Y":
        camper.helmet = True
    else:
        camper.helmet = False
    if camper.boots == "Y":
        camper.boots = True
    else:
        camper.boots = False
    if camper.sleepingBag == "Y":
        camper.sleepingBag = True
    else:
        camper.sleepingBag = False
    if camper.waterBottle == "Y":
        camper.waterBottle = True
    else:
        camper.waterBottle = False
    if camper.sunscreen == "Y":
        camper.sunscreen = True
    else:
        camper.sunscreen = False
    if camper.bugSpray == "Y":
        camper.bugSpray = True
    else:
        camper.bugSpray = False

    if not camper.medical:
        print('Please provide the campers medical information.')
    elif not camper.legal:
        print('Please provide the campers legal information.')
    elif not camper.emergencyContacts:
        print('Please provide the campers emergency contacts.')
    elif not camper.helmet:
        print('Helmets can be rented/purchased from the camp store')
    elif not camper.boots:
        print('Boots can be rented/purchased from the camp store')
    elif not camper.sleepingBag:
        print('Sleeping bags can be rented/purchased from the camp store')
    elif not camper.waterBottle:
        print('Water bottles can be purchased from the camp store')
    elif not camper.sunscreen:
        print('Sunscreen can be purchased from the camp store')
    elif not camper.bugSpray:
        print('Bug spray can be purchased from the camp store')
    else:
        print(camper.fullName + " has all required packet information and equipment for camp!")
        camper.checkedIn = True


def assignBunkhouses(campers, bunkhouses):  # bunkhouses[0-2] 3 female houses, bunkhouses[3-5] 3 male houses with 12 cap
    campersAgeSorted = sorted(campers, key=operator.attrgetter('age'))
    housenum = 0
    bunkhouses = [[], [], [], [], [], []]
    camperHouseCap = int(len(campers) / 6) + 1
    for camper in campersAgeSorted:
        housenum = 0
        if camper.gender == 'M':
            housenum += 3
        if len(bunkhouses[housenum]) == camperHouseCap:
            if len(bunkhouses[housenum+1]) == camperHouseCap:
                if len(bunkhouses[housenum+2]) == camperHouseCap:
                    print('No capacity for camper: ' + camper.getName())
                    return False
                else:
                    bunkhouses[housenum+2].append(camper)
                    camper.setBunkhouse(housenum+2)
                    continue
            else:
                bunkhouses[housenum+1].append(camper)
                camper.setBunkhouse(housenum+1)
                continue
        else:
            bunkhouses[housenum].append(camper)
            camper.setBunkhouse(housenum)
            continue


def assignTribes(campers, tribes):  # tribes[0-5] 6 tribes, with 12 cap; 50-50 gender mix
    campersGenderSorted = sorted(campers, key=operator.attrgetter('gender'))
    tribenum = 0
    tribes = [[], [], [], [], [], []]
    for camper in campersGenderSorted:
        if tribenum > 5:
            tribenum = 0
        elif len(tribes[tribenum]) == 12:
            tribenum += 1
            continue
        else:
            tribes[tribenum].append(camper)
            camper.setTribe(tribenum)
            tribenum += 1
