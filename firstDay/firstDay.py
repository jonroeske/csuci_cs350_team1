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


def assignBunkhouses(campers, bunkhouses):  # (1-3) 3 girl houses, (4-6) 3 boy houses with 12 each
    housenum = 1
    for camper in campers:
        if camper.gender == 'male':
            housenum += 3
        if not bunkhouses[housenum].isFull():
            if not bunkhouses[housenum+1].isFull():
                if not bunkhouses[housenum+2].isFull():
                    print('No capacity for camper')
                    return False
                else:
                    bunkhouses[housenum+2].append(camper)
                    return True
            else:
                bunkhouses[housenum+1].append(camper)
                return True
        else:
            bunkhouses[housenum].append(camper)
            return True


def assignTribes(campers):
    print('')

