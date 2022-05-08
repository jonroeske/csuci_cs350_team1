STATUS_CODES = {
    "SUCCESS": 0,
    "NO_CAMPER": 1,
    "NO_CAMPER_SESSION": 2,
    "NO_CAMPER_BUNKHOUSE": 3,
    "NO_CAMPER_TRIBE": 4,
    "NO_SESSION": 5,
    "NO_BUNKHOUSE": 6,
    "NO_TRIBE": 7,
    "NO_CAPACITY": 8,
    "DUPLICATE": 9,
    "ARGUMENT_ERROR": 10
}

GLOBAL_VALUES = {
    "maxCampersTotal": 216,
    "maxCampersInSession": 72,
    "maxGendersInSession": 36,
    "maxBunkhouses": 6,
    "maxCampersInBunkhouse": 12,
    "maxTribes": 6,
    "maxCampersInTribe": 12
}

def sortByName(camper):
    if camper == "":
        return ""
    else:
        return camper.name

def sortByAge(camper):
    if camper == "":
        return ""
    else:
        return camper.age

def sortByAssignmentRequest(camper):
    if camper == "":
        return ""
    else:
        return camper.assignmentRequest

