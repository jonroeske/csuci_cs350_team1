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


def searchCamperArr(camperArr, name):
    try:
        for currCamper in camperArr:
            if str(currCamper.getName()) == name:
                return currCamper
    except:
        print("Cannot find camper")
    return None


def assignBunkhouses(campers):  # bunkhouses[0-2] 3 female houses, bunkhouses[3-5] 3 male houses with 12 cap
    campersAgeSorted = sorted(campers, key=operator.attrgetter('age'))
    bunkhouses = [[], [], [], [], [], []]
    requests = []
    camperHouseCap = int(len(campers) / 6) + 1
    for camper in campersAgeSorted: # initial sort
        housenum = 0
        if camper.gender == 'M':
            housenum += 3
        if camper.assignmentRequest:
            requests.append(camper)
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
    for camper in requests:  # scrubs assignment requests
        requestingbunkhouse = camper.getBunkhouse()
        requestingcamper = searchCamperArr(campers, camper.assignmentRequest.getName())
        if not bunkhouses[requestingbunkhouse].__contains__(requestingcamper):
            if not len(bunkhouses[requestingbunkhouse]) == 12:  # if requesting bunkhouse is not full, append request
                bunkhouses[requestingcamper.getBunkhouse()].remove(requestingcamper)
                bunkhouses[requestingbunkhouse].append(requestingcamper)
                requestingcamper.setBunkhouse(requestingbunkhouse)
            else:  # if requesting bunkhouse is full
                bunkagesorted = sorted(bunkhouses[requestingbunkhouse], key=operator.attrgetter('age'))
                for bunkmember in bunkagesorted:
                    if not camper:  # adds requestingcamper
                        bunkhouses[requestingbunkhouse].remove(bunkmember)
                        bunkhouses[requestingbunkhouse].append(requestingcamper)
                        requestingcamper.setBunkhouse(requestingbunkhouse)
                        if requestingbunkhouse < 3:
                            for potentialhouse in range(0, 2):
                                if not len(bunkhouses[potentialhouse]) == 12:  # if potential bunkhouse is not full
                                    bunkhouses[potentialhouse].append(bunkmember)
                                    bunkmember.setBunkhouse(potentialhouse)
                        else:
                            for potentialhouse in range(3, 5):
                                if not len(bunkhouses[potentialhouse]) == 12:  # if potential bunkhouse is not full
                                    bunkhouses[potentialhouse].append(bunkmember)
                                    bunkmember.setBunkhouse(potentialhouse)


def assignTribes(campers):  # tribes[0-5] 6 tribes, with 12 cap; 50-50 gender mix
    campersGenderSorted = sorted(campers, key=operator.attrgetter('gender'))
    tribenum = 0
    tribes = [[], [], [], [], [], []]
    requests = []
    for camper in campersGenderSorted:  # initial sort
        if camper.assignmentRequest:
            requests.append(camper)
        if tribenum > 5:
            tribenum = 0
        elif len(tribes[tribenum]) == 12:
            tribenum += 1
            continue
        else:
            tribes[tribenum].append(camper)
            camper.setTribe(tribenum)
            tribenum += 1
    for camper in requests:  # scrubs assignment requests
        requestingtribe = camper.getTribe()
        requestingcamper = searchCamperArr(campers, camper.assignmentRequest.getName())
        if not tribes[requestingtribe].__contains__(requestingcamper):
            if not len(tribes[requestingtribe]) == 12:  # if requesting tribe is not full, append requesting camper
                tribes[requestingcamper.getTribe()].remove(requestingcamper)
                requestingcamper.setTribe(requestingtribe)
                tribes[requestingtribe].append(requestingcamper)
            else:  # if requesting tribe is full
                tribegendersorted = sorted(tribes[requestingtribe], key=operator.attrgetter('gender'))
                for tribemember in tribegendersorted:
                    if tribemember.getGender() == requestingcamper.getGender() and not camper:  # adds requestingcamper
                        tribes[requestingtribe].remove(tribemember)
                        tribes[requestingtribe].append(requestingcamper)
                        requestingcamper.setTribe(requestingtribe)
                        for tribe in range(0, 5):
                            if not len(tribes[tribe]) == 12:  # if potential tribe for tribemember is not full
                                tribes[tribe].append(tribemember)
                                tribemember.setTribe(tribe)
