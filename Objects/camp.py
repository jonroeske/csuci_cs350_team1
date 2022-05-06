from Objects.camper import *
from Objects.values import *

from operator import *

class Camp:

    def __init__(self):
        self.allCampers = [None for _ in range(GLOBAL_VALUES["maxCampersTotal"])]
        self.juneCampers = [[None for _ in range(GLOBAL_VALUES["maxCampersInSession"])],
                            [None for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"]) for _ in range(GLOBAL_VALUES["maxBunkhouses"])],
                            [None for _ in range(GLOBAL_VALUES["maxCampersInTribe"]) for _ in range(GLOBAL_VALUES["maxTribes"])]]
        self.julyCampers = [[None for _ in range(GLOBAL_VALUES["maxCampersInSession"])],
                            [None for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"]) for _ in range(GLOBAL_VALUES["maxBunkhouses"])],
                            [None for _ in range(GLOBAL_VALUES["maxCampersInTribe"]) for _ in range(GLOBAL_VALUES["maxTribes"])]]
        self.augustCampers =[[None for _ in range(GLOBAL_VALUES["maxCampersInSession"])],
                            [None for _ in range(GLOBAL_VALUES["maxCampersInBunkhouse"]) for _ in range(GLOBAL_VALUES["maxBunkhouses"])],
                            [None for _ in range(GLOBAL_VALUES["maxCampersInTribe"]) for _ in range(GLOBAL_VALUES["maxTribes"])]]


    def sortCamp(self):
        try:
            self.allCampers.sort(key=lambda x: (x is None, x))

            self.juneCampers[0].sort(key=lambda x: (x is None, x))
            self.julyCampers[0].sort(key=lambda x: (x is None, x))
            self.augustCampers[0].sort(key=lambda x: (x is None, x))

            #for i in range(GLOBAL_VALUES["maxBunkhouses"]):
            #    self.juneCampers[1][i].sort(key=lambda x: (x is None, x))
            #    self.julyCampers[1][i].sort(key=lambda x: (x is None, x))
            #    self.augustCampers[1][i].sort(key=lambda x: (x is None, x))

            #for i in range(GLOBAL_VALUES["maxTribes"]):
            #    self.juneCampers[2][i].sort(key=lambda x: (x is None, x))
            #    self.julyCampers[2][i].sort(key=lambda x: (x is None, x))
            #    self.augustCampers[2][i].sort(key=lambda x: (x is None, x))

        except TypeError:
            pass
            #This will always throw if there are Nones present, which odds are, you will have, so just pass

    def countGender(self, session = -1, bunkOrTribe = -1, bOTSelection = -1):
        count = [0, 0]

        campers = []

        match session:
            case -1:
                campers = self.allCampers
            case 0:
                if bunkOrTribe != -1 and bOTSelection != -1:
                    campers = self.juneCampers[bunkOrTribe+1][bOTSelection]
                else:
                    campers = self.juneCampers[0]
            case 1:
                if bunkOrTribe != -1 and bOTSelection != -1:
                    campers = self.julyCampers[bunkOrTribe + 1][bOTSelection]
                else:
                    campers = self.julyCampers[0]
            case 2:
                if bunkOrTribe != -1 and bOTSelection != -1:
                    campers = self.augustCampers[bunkOrTribe + 1][bOTSelection]
                else:
                    campers = self.augustCampers[0]


        for camper in campers:
            if isinstance(camper, Camper):
                if camper.getGender() == "M":
                    count[0] += 1
                elif camper.getGender() == "F":
                    count[1] += 1

        return count


    def updateCamper(self, camper):
        session = camper.getSession()
        bunkhouse = camper.getBunkhouse()
        tribe = camper.getTribe()


        for currentCamper in self.allCampers:
            if currentCamper.getName() == camper.getName():
                try:
                    self.allCampers.remove(currentCamper)
                    self.allCampers.append(camper)
                    break
                except ValueError:
                    return STATUS_CODES["NO_CAMPER"]

        if session is not None:
            match session:
                case 0:
                    for currentCamper in self.juneCampers[0]:
                        if currentCamper.getName() == camper.getName():
                            try:
                                self.juneCampers[0].remove(currentCamper)
                                self.juneCampers[0].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_SESSION"]

                case 1:
                    for currentCamper in self.julyCampers[0]:
                        if currentCamper.getName() == camper.getName():
                            try:
                                self.julyCampers[0].remove(currentCamper)
                                self.julyCampers[0].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_SESSION"]

                case 2:
                    for currentCamper in self.augustCampers[0]:
                        if currentCamper.getName() == camper.getName():
                            try:
                                self.augustCampers[0].remove(currentCamper)
                                self.augustCampers[0].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_SESSION"]

        if bunkhouse is not None:
            match session:
                case 0:
                    for currentCamper in self.juneCampers[1][bunkhouse]:
                        if currentCamper.getName() == camper.getName():
                            try:
                                self.juneCampers[1][bunkhouse].remove(currentCamper)
                                self.juneCampers[1][bunkhouse].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_BUNKHOUSE"]

                case 1:
                    for currentCamper in self.julyCampers[1][bunkhouse]:
                        if currentCamper.getName() == camper.getName():
                            try:
                                self.julyCampers[1][bunkhouse].remove(currentCamper)
                                self.julyCampers[1][bunkhouse].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_BUNKHOUSE"]

                case 2:
                    for currentCamper in self.augustCampers[1][bunkhouse]:
                        if currentCamper.getName() == camper.getName():
                            try:
                                self.augustCampers[1][bunkhouse].remove(currentCamper)
                                self.augustCampers[1][bunkhouse].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_BUNKHOUSE"]

        if tribe is not None:
            match session:
                case 0:
                    for currentCamper in self.juneCampers[2][tribe]:
                        if currentCamper.getName() == camper.getName():
                            try:
                                self.juneCampers[2][tribe].remove(currentCamper)
                                self.juneCampers[2][tribe].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_TRIBE"]

                case 1:
                    for currentCamper in self.julyCampers[2][tribe]:
                        if currentCamper.getName() == camper.getName():
                            try:
                                self.julyCampers[2][tribe].remove(currentCamper)
                                self.julyCampers[2][tribe].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_TRIBE"]

                case 2:
                    for currentCamper in self.augustCampers[2][tribe]:
                        if currentCamper.getName() == camper.getName():
                            try:
                                self.augustCampers[2][tribe].remove(currentCamper)
                                self.augustCampers[2][tribe].append(camper)
                                break
                            except ValueError:
                                return STATUS_CODES["NO_CAMPER_TRIBE"]

        self.sortCamp()

        return STATUS_CODES["SUCCESS"]


    def insertCamper(self, camper):
        try:
            self.allCampers.index(camper)
            return STATUS_CODES["DUPLICATE"]
        except ValueError:
            try:
                self.allCampers.remove(None)
                self.allCampers.append(camper)

                self.allCampers.sort(key=lambda x: (x is None, x))

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
                        self.juneCampers[0].remove(None)
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
                        self.julyCampers[0].remove(None)
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
                        self.augustCampers[0].remove(None)
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
                        self.juneCampers[1][bunkhouse].remove(None)
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
                        self.julyCampers[1][bunkhouse].remove(None)
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
                        self.augustCampers[1][bunkhouse].remove(None)
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
                        self.juneCampers[2][tribe].remove(None)
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
                        self.julyCampers[2][tribe].remove(None)
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
                        self.augustCampers[2][tribe].remove(None)
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


