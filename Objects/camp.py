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
                    return self.juneCampers[kwargs["bunkOrTribe"] + 1][kwargs["bunkOrTribeIndex"] ]
                else:
                    return self.juneCampers[0]
            case 1:
                if "bunkOrTribe" in kwargs and "bunkOrTribeindex" in kwargs:
                    return self.julyCampers[kwargs["bunkOrTribe"] + 1][kwargs["bunkOrTribeIndex"] ]
                else:
                    return self.julyCampers[0]
            case 2:
                if "bunkOrTribe" in kwargs and "bunkOrTribeindex" in kwargs:
                    return self.augustCampers[kwargs["bunkOrTribe"] + 1][kwargs["bunkOrTribeIndex"] ]
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
                    if not "delete" in kwargs:
                        self.allCampers.append(camper)
                    break
                except ValueError:
                    return STATUS_CODES["NO_CAMPER"]

        session = camper.getSession()
        bunkhouse = camper.getBunkhouse()
        tribe = camper.getTribe()

        if session != "":
            match session:
                case 0:
                    for currentCamper in self.juneCampers[0]:
                        if isinstance(currentCamper, str):
                            continue

                        if currentCamper.getName() == camper.getName():
                            try:
                                self.juneCampers[0].remove(currentCamper)
                                if not "delete" in kwargs:
                                    self.juneCampers[0].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_SESSION"]

                case 1:
                    for currentCamper in self.julyCampers[0]:
                        if isinstance(currentCamper, str):
                            continue

                        if currentCamper.getName() == camper.getName():
                            try:
                                self.julyCampers[0].remove(currentCamper)
                                if not "delete" in kwargs:
                                    self.julyCampers[0].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_SESSION"]

                case 2:
                    for currentCamper in self.augustCampers[0]:
                        if isinstance(currentCamper, str):
                            continue

                        if currentCamper.getName() == camper.getName():
                            try:
                                self.augustCampers[0].remove(currentCamper)
                                if not "delete" in kwargs:
                                    self.augustCampers[0].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_SESSION"]

        if bunkhouse != "":
            match session:
                case 0:
                    for currentCamper in self.juneCampers[1][bunkhouse]:
                        if isinstance(currentCamper, str):
                            continue

                        if currentCamper.getName() == camper.getName():
                            try:
                                self.juneCampers[1][bunkhouse].remove(currentCamper)
                                if not "delete" in kwargs:
                                    self.juneCampers[1][bunkhouse].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_BUNKHOUSE"]

                case 1:
                    for currentCamper in self.julyCampers[1][bunkhouse]:
                        if isinstance(currentCamper, str):
                            continue

                        if currentCamper.getName() == camper.getName():
                            try:
                                self.julyCampers[1][bunkhouse].remove(currentCamper)
                                if not "delete" in kwargs:
                                    self.julyCampers[1][bunkhouse].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_BUNKHOUSE"]

                case 2:
                    for currentCamper in self.augustCampers[1][bunkhouse]:
                        if isinstance(currentCamper, str):
                            continue

                        if currentCamper.getName() == camper.getName():
                            try:
                                self.augustCampers[1][bunkhouse].remove(currentCamper)
                                if not "delete" in kwargs:
                                    self.augustCampers[1][bunkhouse].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_BUNKHOUSE"]

        if tribe != "":
            match session:
                case 0:
                    for currentCamper in self.juneCampers[2][tribe]:
                        if isinstance(currentCamper, str):
                            continue

                        if currentCamper.getName() == camper.getName():
                            try:
                                self.juneCampers[2][tribe].remove(currentCamper)
                                if not "delete" in kwargs:
                                    self.juneCampers[2][tribe].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_TRIBE"]

                case 1:
                    for currentCamper in self.julyCampers[2][tribe]:
                        if isinstance(currentCamper, str):
                            continue

                        if currentCamper.getName() == camper.getName():
                            try:
                                self.julyCampers[2][tribe].remove(currentCamper)
                                if not "delete" in kwargs:
                                    self.julyCampers[2][tribe].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_TRIBE"]

                case 2:
                    for currentCamper in self.augustCampers[2][tribe]:
                        if isinstance(currentCamper, str):
                            continue

                        if currentCamper.getName() == camper.getName():
                            try:
                                self.augustCampers[2][tribe].remove(currentCamper)
                                if not "delete" in kwargs:
                                    self.augustCampers[2][tribe].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_TRIBE"]

        return STATUS_CODES["SUCCESS"]

    def insertCamper(self, camper):
        try:
            self.allCampers.index(camper)
            return STATUS_CODES["DUPLICATE"]
        except ValueError:
            try:
                self.allCampers.remove("")
                self.allCampers.append(camper)

                self.allCampers.sort(key=lambda x: (x == "", x))

                return STATUS_CODES["SUCCESS"]
            except ValueError:
                return STATUS_CODES["NO_CAPACITY"]

    def insertCamperInSession(self, camper):
        session = camper.getSession()

        if session is None:
            return STATUS_CODES["NO_SESSION"]

        match session:
            case 0:
                try:
                    self.juneCampers[0].index(camper)
                    return STATUS_CODES["DUPLICATE"]
                except ValueError:
                    try:
                        self.juneCampers[0].remove("")
                        self.juneCampers[0].append(camper)

                        return STATUS_CODES["SUCCESS"]
                    except ValueError:
                        return STATUS_CODES["NO_CAPACITY"]
            case 1:
                try:
                    self.julyCampers[0].index(camper)
                    return STATUS_CODES["DUPLICATE"]
                except ValueError:
                    try:
                        self.julyCampers[0].remove("")
                        self.julyCampers[0].append(camper)
                        return STATUS_CODES["SUCCESS"]
                    except ValueError:
                        return STATUS_CODES["NO_CAPACITY"]
            case 2:
                try:
                    self.augustCampers[0].index(camper)
                    return STATUS_CODES["DUPLICATE"]
                except ValueError:
                    try:
                        self.augustCampers[0].remove("")
                        self.augustCampers[0].append(camper)
                        return STATUS_CODES["SUCCESS"]
                    except ValueError:
                        return STATUS_CODES["NO_CAPACITY"]

    def insertCamperInBunkhouse(self, camper):
        session = camper.getSession()

        if session is None:
            return STATUS_CODES["NO_SESSION"]

        bunkhouse = camper.getBunkhouse()

        if bunkhouse is None:
            return STATUS_CODES["NO_BUNKHOUSE"]

        match session:
            case 0:
                try:
                    self.juneCampers[1][bunkhouse].index(camper)
                    return STATUS_CODES["DUPLICATE"]
                except ValueError:
                    try:
                        self.juneCampers[1][bunkhouse].remove("")
                        self.juneCampers[1][bunkhouse].append(camper)
                        return STATUS_CODES["SUCCESS"]
                    except ValueError:
                        return STATUS_CODES["NO_CAPACITY"]
            case 1:
                try:
                    self.julyCampers[1][bunkhouse].index(camper)
                    return STATUS_CODES["DUPLICATE"]
                except ValueError:
                    try:
                        self.julyCampers[1][bunkhouse].remove("")
                        self.julyCampers[1][bunkhouse].append(camper)
                        return STATUS_CODES["SUCCESS"]
                    except ValueError:
                        return STATUS_CODES["NO_CAPACITY"]
            case 2:
                try:
                    self.augustCampers[1][bunkhouse].index(camper)
                    return STATUS_CODES["DUPLICATE"]
                except ValueError:
                    try:
                        self.augustCampers[1][bunkhouse].remove("")
                        self.augustCampers[1][bunkhouse].append(camper)
                        return STATUS_CODES["SUCCESS"]
                    except ValueError:
                        return STATUS_CODES["NO_CAPACITY"]

    def insertCamperInTribe(self, camper):
        session = camper.getSession()

        if session is None:
            return STATUS_CODES["NO_SESSION"]

        tribe = camper.getTribe()

        if tribe is None:
            return STATUS_CODES["NO_TRIBE"]

        match session:
            case 0:
                try:
                    self.juneCampers[2][tribe].index(camper)
                    return STATUS_CODES["DUPLICATE"]
                except ValueError:
                    try:
                        self.juneCampers[2][tribe].remove("")
                        self.juneCampers[2][tribe].append(camper)
                        return STATUS_CODES["SUCCESS"]
                    except ValueError:
                        return STATUS_CODES["NO_CAPACITY"]
            case 1:
                try:
                    self.julyCampers[2][tribe].index(camper)
                    return STATUS_CODES["DUPLICATE"]
                except ValueError:
                    try:
                        self.julyCampers[2][tribe].remove("")
                        self.julyCampers[2][tribe].append(camper)
                        return STATUS_CODES["SUCCESS"]
                    except ValueError:
                        return STATUS_CODES["NO_CAPACITY"]
            case 2:
                try:
                    self.augustCampers[2][tribe].index(camper)
                    return STATUS_CODES["DUPLICATE"]
                except ValueError:
                    try:
                        self.augustCampers[2][tribe].remove("")
                        self.augustCampers[2][tribe].append(camper)
                        return STATUS_CODES["SUCCESS"]
                    except ValueError:
                        return STATUS_CODES["NO_CAPACITY"]

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
