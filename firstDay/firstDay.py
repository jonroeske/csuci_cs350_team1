# Clerk logic for handling day one of camp sessions
def checkInCert(camper):
    print('')


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

