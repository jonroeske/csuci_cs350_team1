import operator


# Clerk logic for handling day one of camp sessions
def checkInCert(camper):  # Verifies required forms for arrival packet
    camper.checkedIn = False

    print('--------Campers Arrival Packet--------')
    print('Please answer the following questions with True or False only')
    camper.medical = input('Does the camper have his/her medical information filled out?')
    camper.legal = input('Does the camper have his/her legal information filled out?')
    camper.emergencycontacts = input('Does the camper have his/her emergency contacts filled out?')
    print('--------Campers Required Equipment--------')
    print('Please answer the following questions with True or False only')
    camper.helmet = input('Does the camper have his/her riding helmet?')
    camper.boots = input('Does the camper have his/her boots?')
    camper.sleepingbag = input('Does the camper have his/her sleeping bag?')
    camper.waterbottle = input('Does the camper have his/her water bottle?')
    camper.sunscreen = input('Does the camper have his/her sun screen?')
    camper.bugspray = input('Does the camper have his/her bug spray?')

    if not camper.medical:
        print('Please provide the campers medical information.')
    elif not camper.legal:
        print('Please provide the campers legal information.')
    elif not camper.emergencycontacts:
        print('Please provide the campers emergency contacts.')
    elif not camper.helmet:
        print('Helmets can be rented/purchased from the camp store')
    elif not camper.boots:
        print('Boots can be rented/purchased from the camp store')
    elif not camper.sleepingbag:
        print('Sleeping bags can be rented/purchased from the camp store')
    elif not camper.waterbottle:
        print('Water bottles can be purchased from the camp store')
    elif not camper.sunscreen:
        print('Sunscreen can be purchased from the camp store')
    elif not camper.bugspray:
        print('Bug spray can be purchased from the camp store')
    else:
        print(camper.fullname + " has all required packet information and equipment for camp!")
        camper.checkedin = True


def assignBunkhouses(campers, bunkhouses):  # bunkhouses[0-2] 3 female houses, bunkhouses[3-5] 3 male houses with 12 cap
    campersAgeSorted = sorted(campers, key=operator.attrgetter('age'))
    housenum = 0
    camperHouseCap = int(campers.length() / 6) + 1
    for camper in campersAgeSorted:
        if camper.gender == 'M':
            housenum += 3
        if bunkhouses[housenum].length() == camperHouseCap:
            if bunkhouses[housenum+1].length() == camperHouseCap:
                if bunkhouses[housenum+2].length() == camperHouseCap:
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


def assignTribes(campers, tribes):  # tribes[0-5] 6 tribes, with 12 cap
    campersGenderSorted = sorted(campers, key=operator.attrgetter('gender'))
    tribenum = 0
    for camper in campersGenderSorted:
        if tribenum > 5:
            tribenum = 0
        if tribes[tribenum].length() == 12:
            tribenum += 1
            continue
        else:
            tribes[tribenum].append(camper)
            tribenum += 1
