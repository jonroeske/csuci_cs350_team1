from Objects.camper import *
from Objects.values import *

class Camp:

    def __init__(self):
        self.allCampers = ["" for _ in range(GLOBAL_VALUES["maxCampersTotal"])]
        self.juneCampers = [["" for _ in range(GLOBAL_VALUES["maxCampersInSession"])],
                            [["" for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"])] for _ in
                             range(GLOBAL_VALUES["maxBunkhouses"])],
                            [["" for _ in range(GLOBAL_VALUES["maxCampersInTribe"])] for _ in
                             range(GLOBAL_VALUES["maxTribes"])]]

        self.julyCampers = [["" for _ in range(GLOBAL_VALUES["maxCampersInSession"])],
                            [["" for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"])] for _ in
                             range(GLOBAL_VALUES["maxBunkhouses"])],
                            [["" for _ in range(GLOBAL_VALUES["maxCampersInTribe"])] for _ in
                             range(GLOBAL_VALUES["maxTribes"])]]

        self.augustCampers = [["" for _ in range(GLOBAL_VALUES["maxCampersInSession"])],
                              [["" for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"])] for _ in
                               range(GLOBAL_VALUES["maxBunkhouses"])],
                              [["" for _ in range(GLOBAL_VALUES["maxCampersInTribe"])] for _ in
                               range(GLOBAL_VALUES["maxTribes"])]]

    def countGender(self, **kwargs):
        count = [0, 0]

        campers = self.getList(**kwargs)

        for camper in campers:
            if isinstance(camper, Camper):
                if camper.getGender() == "M":
                    count[0] += 1
                elif camper.getGender() == "F":
                    count[1] += 1

        return count

    def sortList(self, **kwargs):
        campers = self.getList(**kwargs)

        if not "parameter" in kwargs:
            campers.sort(key=sortByName)

        try:
            match kwargs["parameter"]:
                case "age":
                    campers.sort(key=sortByAge)
                case "name":
                    campers.sort(key=sortByName)
                case "assignmentRequest":
                    campers.sort(reverse=True, key=sortByAssignmentRequest)
        except Exception as e:
            print(e)

    def getList(self, **kwargs):
        if not "session" in kwargs:
            return self.allCampers

        match kwargs["session"]:
            case 0:
                if "bunkOrTribe" in kwargs and "bunkOrTribeindex" in kwargs:
                    return self.juneCampers[kwargs["bunkOrTribe"] + 1][kwargs["bunkOrTribeIndex"]]
                else:
                    return self.juneCampers[0]
            case 1:
                if "bunkOrTribe" in kwargs and "bunkOrTribeindex" in kwargs:
                    return self.julyCampers[kwargs["bunkOrTribe"] + 1][kwargs["bunkOrTribeIndex"]]
                else:
                    return self.julyCampers[0]
            case 2:
                if "bunkOrTribe" in kwargs and "bunkOrTribeindex" in kwargs:
                    return self.augustCampers[kwargs["bunkOrTribe"] + 1][kwargs["bunkOrTribeIndex"]]
                else:
                    return self.augustCampers[0]

    def searchCamper(self, camperOrName):
        if isinstance(camperOrName, str):
            for camper in self.allCampers:
                if isinstance(camper, Camper):
                    if camperOrName == camper.getName():
                        return camper
            return STATUS_CODES["NO_CAMPER"]

        elif isinstance(camperOrName, Camper):
            try:
                self.allCampers.index(camperOrName)
                return STATUS_CODES["SUCCESS"]
            except ValueError:
                return STATUS_CODES["NO_CAMPER"]

    def updateCamper(self, camper, **kwargs):
        for currentCamper in self.allCampers:
            if isinstance(currentCamper, str):
                continue

            if currentCamper.getName() == camper.getName():
                try:
                    self.allCampers.remove(currentCamper)
                except ValueError:
                    self.allCampers.remove("")

                if "remove" in kwargs and kwargs["remove"] is True:
                    self.allCampers.append("")

                elif "remove" not in kwargs:
                    self.allCampers.append(camper)
                break

        locations = [self.juneCampers, self.julyCampers, self.augustCampers]

        session = camper.getSession()
        bunkhouse = camper.getBunkhouse()
        tribe = camper.getTribe()

        if session is not False:
            try:
                locations[session][0].remove(camper)
            except ValueError:
                locations[session][0].remove("")
            locations[session][0].append(camper)

        elif session is False:
            for location in locations:
                try:
                    location[0].remove(camper)
                    location[0].append("")
                except ValueError:
                    pass

            
        if bunkhouse is not False and session is not False:
            try:
                locations[session][1][bunkhouse].remove(camper)
            except ValueError:
                locations[session][1][bunkhouse].remove("")

            locations[session][1][bunkhouse].append(camper)

        elif bunkhouse is False or session is False:
            camper.setBunkhouse(False)
            for location in locations:
                for i in range(0, GLOBAL_VALUES["maxBunkhouses"]):
                    try:
                        location[2][i].remove(camper)
                        location[2][i].append("")
                    except ValueError:
                        pass


        if tribe is not False and session is not False:
            try:
                locations[session][2][tribe].remove(camper)
            except ValueError:
                locations[session][2][tribe].remove("")

            locations[session][2][tribe].append(camper)

        elif tribe is False or session is False:
            camper.setTribe(False)
            for location in locations:
                for i in range(0, GLOBAL_VALUES["maxTribes"]):
                    try:
                        location[2][i].remove(camper)
                        location[2][i].append("")
                    except ValueError:
                        pass


        return STATUS_CODES["SUCCESS"]

    def insertCamper(self, camper):
        try:
            self.allCampers.remove("")
            self.allCampers.append(camper)
        except ValueError:
            return STATUS_CODES["NO_CAPACITY"]


        locations = [self.juneCampers, self.julyCampers, self.augustCampers]

        session = camper.getSession()
        bunkhouse = camper.getBunkhouse()
        tribe = camper.getTribe()

        if session is not False:
            try:
                self.locations[session][0].remove("")
                self.locations[session][0].append(camper)
            except ValueError:
                return STATUS_CODES["NO_CAPACITY"]

        if bunkhouse is not False and session is not False:
            try:
                self.locations[session][1][bunkhouse].remove("")
                self.locations[session][1][bunkhouse].append(camper)
            except ValueError:
                return STATUS_CODES["NO_CAPACITY"]



        if tribe is not False and session is not False:
            try:
                self.locations[session][2][tribe].remove("")
                self.locations[session][2][tribe].append(camper)
            except ValueError:
                return STATUS_CODES["NO_CAPACITY"]

        return STATUS_CODES["SUCCESS"]

    #def insertCamperInSession(self, camper):
    #    session = camper.getSession()
#
    #    if session is None:
    #        return STATUS_CODES["NO_SESSION"]
#
    #    match session:
    #        case 0:
    #            try:
    #                self.juneCampers[0].index(camper)
    #                return STATUS_CODES["DUPLICATE"]
    #            except ValueError:
    #                try:
    #                    self.juneCampers[0].remove("")
    #                    self.juneCampers[0].append(camper)
#
    #                    return STATUS_CODES["SUCCESS"]
    #                except ValueError:
    #                    return STATUS_CODES["NO_CAPACITY"]
    #        case 1:
    #            try:
    #                self.julyCampers[0].index(camper)
    #                return STATUS_CODES["DUPLICATE"]
    #            except ValueError:
    #                try:
    #                    self.julyCampers[0].remove("")
    #                    self.julyCampers[0].append(camper)
    #                    return STATUS_CODES["SUCCESS"]
    #                except ValueError:
    #                    return STATUS_CODES["NO_CAPACITY"]
    #        case 2:
    #            try:
    #                self.augustCampers[0].index(camper)
    #                return STATUS_CODES["DUPLICATE"]
    #            except ValueError:
    #                try:
    #                    self.augustCampers[0].remove("")
    #                    self.augustCampers[0].append(camper)
    #                    return STATUS_CODES["SUCCESS"]
    #                except ValueError:
    #                    return STATUS_CODES["NO_CAPACITY"]

    #def insertCamperInBunkhouse(self, camper):
    #    session = camper.getSession()
#
    #    if session is None:
    #        return STATUS_CODES["NO_SESSION"]
#
    #    bunkhouse = camper.getBunkhouse()
#
    #    if bunkhouse is None:
    #        return STATUS_CODES["NO_BUNKHOUSE"]
#
    #    match session:
    #        case 0:
    #            try:
    #                self.juneCampers[1][bunkhouse].index(camper)
    #                return STATUS_CODES["DUPLICATE"]
    #            except ValueError:
    #                try:
    #                    self.juneCampers[1][bunkhouse].remove("")
    #                    self.juneCampers[1][bunkhouse].append(camper)
    #                    return STATUS_CODES["SUCCESS"]
    #                except ValueError:
    #                    return STATUS_CODES["NO_CAPACITY"]
    #        case 1:
    #            try:
    #                self.julyCampers[1][bunkhouse].index(camper)
    #                return STATUS_CODES["DUPLICATE"]
    #            except ValueError:
    #                try:
    #                    self.julyCampers[1][bunkhouse].remove("")
    #                    self.julyCampers[1][bunkhouse].append(camper)
    #                    return STATUS_CODES["SUCCESS"]
    #                except ValueError:
    #                    return STATUS_CODES["NO_CAPACITY"]
    #        case 2:
    #            try:
    #                self.augustCampers[1][bunkhouse].index(camper)
    #                return STATUS_CODES["DUPLICATE"]
    #            except ValueError:
    #                try:
    #                    self.augustCampers[1][bunkhouse].remove("")
    #                    self.augustCampers[1][bunkhouse].append(camper)
    #                    return STATUS_CODES["SUCCESS"]
    #                except ValueError:
    #                    return STATUS_CODES["NO_CAPACITY"]

    #def insertCamperInTribe(self, camper):
    #    session = camper.getSession()
#
    #    if session is None:
    #        return STATUS_CODES["NO_SESSION"]
#
    #    tribe = camper.getTribe()
#
    #    if tribe is None:
    #        return STATUS_CODES["NO_TRIBE"]
#
    #    match session:
    #        case 0:
    #            try:
    #                self.juneCampers[2][tribe].index(camper)
    #                return STATUS_CODES["DUPLICATE"]
    #            except ValueError:
    #                try:
    #                    self.juneCampers[2][tribe].remove("")
    #                    self.juneCampers[2][tribe].append(camper)
    #                    return STATUS_CODES["SUCCESS"]
    #                except ValueError:
    #                    return STATUS_CODES["NO_CAPACITY"]
    #        case 1:
    #            try:
    #                self.julyCampers[2][tribe].index(camper)
    #                return STATUS_CODES["DUPLICATE"]
    #            except ValueError:
    #                try:
    #                    self.julyCampers[2][tribe].remove("")
    #                    self.julyCampers[2][tribe].append(camper)
    #                    return STATUS_CODES["SUCCESS"]
    #                except ValueError:
    #                    return STATUS_CODES["NO_CAPACITY"]
    #        case 2:
    #            try:
    #                self.augustCampers[2][tribe].index(camper)
    #                return STATUS_CODES["DUPLICATE"]
    #            except ValueError:
    #                try:
    #                    self.augustCampers[2][tribe].remove("")
    #                    self.augustCampers[2][tribe].append(camper)
    #                    return STATUS_CODES["SUCCESS"]
    #                except ValueError:
    #                    return STATUS_CODES["NO_CAPACITY"]

    def getAllCampers(self):
        return self.allCampers

    def getJune(self):
        return self.juneCampers

    def getJuly(self):
        return self.julyCampers

    def getAugust(self):
        return self.augustCampers

    def getJuneCampers(self):
        return self.juneCampers[0]

    def getJuneBunkhouses(self):
        return self.juneCampers[1]

    def getJuneBunkhouseAtIndex(self, i):
        return self.juneCampers[1][i]

    def getJuneTribes(self):
        return self.juneCampers[2]

    def getJuneTribeAtIndex(self, i):
        return self.juneCampers[2][i]

    def getJulyCampers(self):
        return self.julyCampers[0]

    def getJulyBunkhouses(self):
        return self.julyCampers[1]

    def getJulyBunkhouseAtIndex(self, i):
        return self.julyCampers[1][i]

    def getJulyTribes(self):
        return self.julyCampers[2]

    def getJulyTribeAtIndex(self, i):
        return self.julyCampers[2][i]

    def getAugustCampers(self):
        return self.augustCampers[0]

    def getAugustBunkhouses(self):
        return self.augustCampers[1]

    def getAugustBunkhouseAtIndex(self, i):
        return self.augustCampers[1]

    def getAugustTribes(self):
        return self.augustCampers[2]

    def getAugustTribeAtIndex(self, i):
        return self.augustCampers[2][i]

    def setAllCampers(self, allCampers):
        self.allCampers = allCampers

    def setJune(self, juneCampers):
        self.juneCampers = juneCampers

    def setJuly(self, julyCampers):
        self.julyCampers = julyCampers

    def setAugust(self, augustCampers):
        self.augustCampers = augustCampers

    def setJuneCampers(self, campers):
        self.juneCampers[0] = campers

    def setJuneBunkhouses(self, bunkhouses):
        self.juneCampers[1] = bunkhouses

    def setJuneBunkhouseAtIndex(self, bunkhouse, i):
        self.juneCampers[1][i] = bunkhouse

    def setJuneTribes(self, tribes):
        self.juneCampers[2] = tribes

    def setJuneTribeAtIndex(self, tribe, i):
        self.juneCampers[2][i] = tribe

    def setJulyCampers(self, campers):
        self.julyCampers[0] = campers

    def setJulyBunkhouses(self, bunkhouses):
        self.julyCampers[1] = bunkhouses

    def setJulyBunkhouseAtIndex(self, bunkhouse, i):
        self.julyCampers[1][i] = bunkhouse

    def setJulyTribes(self, tribes):
        self.julyCampers[2] = tribes

    def setJulyTribeAtIndex(self, tribe, i):
        self.julyCampers[2][i] = tribe

    def setAugustCampers(self, campers):
        self.augustCampers[0] = campers

    def setAugustBunkhouses(self, bunkhouses):
        self.augustCampers[1] = bunkhouses

    def setAugustBunkhouseAtIndex(self, bunkhouse, i):
        self.augustCampers[1][i] = bunkhouse

    def setAugustTribes(self, tribes):
        self.augustCampers[2] = tribes

    def setAugustTribeAtIndex(self, tribe, i):
        self.augustCampers[2][i] = tribe
