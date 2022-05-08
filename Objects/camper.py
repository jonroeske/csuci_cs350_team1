from datetime import datetime
from Objects.materials import *
from Objects.values import *

class Camper:
    def __init__(self):
        # CAMPER DESCRIPTION
        self.name = ""
        self.age = ""
        self.gender = ""
        self.address = ""
        self.balance = 1000.00
        self.appStatus = 0

        # CAMPER CAMP DETAILS
        self.session = False
        self.bunkhouse = False
        self.tribe = False
        self.arrivalReqCert = False
        self.checkedIn = False

        # CAMPER SUPPLIES + REQUEST
        self.assignmentRequest = False
        self.assignment = None
        self.packetStatus = False
        self.dateSentNotice = False
        self.materials = False

    def __eq__(self, other):
        if isinstance(other, Camper):
            return (self.name, self.age, self.gender) \
                   == (other.getName(), other.getAge(), other.getGender())

        return False

    def __lt__(self, other):
        if isinstance(other, Camper):
            return self.name < other.name

        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Camper):
            return self.name > other.name
        else:
            return False

    def searchByFullName(self, campers):
        returnList = []

        for camper in campers:
            if isinstance(camper, Camper) and not camper.__eq__(self):
                if camper.getName() == self.name:
                    returnList.append(camper)

        if len(returnList) == 0:
            return STATUS_CODES["NO_CAMPER"]

        return returnList

    def searchByLastName(self, campers):
        returnList = []

        for camper in campers:
            if isinstance(camper, Camper) and not camper.__eq__(self):
                selfLastName = self.name.split(" ")[1]
                camperLastName = camper.getName().split(" ")[1]

                if camperLastName == selfLastName:
                    returnList.append(camper)

        if len(returnList) == 0:
            return STATUS_CODES["NO_CAMPER"]

        return returnList

    def searchByGender(self, campers):
        returnList = []

        for camper in campers:
            if isinstance(camper, Camper) and not camper.__eq__(self):
                if camper.getGender() == self.gender:
                    returnList.append(camper)

        if len(returnList) == 0:
            return STATUS_CODES["NO_CAMPER"]

        return returnList

    def countGender(self, campers):
        count = [0, 0]

        for camper in campers:
            if isinstance(camper, Camper) and not camper.__eq__(self):
                if camper.getGender() == self.gender:
                    count += 1

        return count


    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getAddress(self):
        return self.address

    def getBalance(self):
        return self.balance

    def getAppStatus(self):
        return self.appStatus


    def getSession(self):
        return self.session

    def getBunkhouse(self):
        return self.bunkhouse

    def getTribe(self):
        return self.tribe

    def getArrivalReqCert(self):
        return self.arrivalReqCert

    def getCheckedIn(self):
        return self.checkedIn

    def getAssignmentRequest(self):
        return self.assignmentRequest

    def getAssignment(self):
        return self.assignment

    def getPacket(self):
        return self.packetStatus

    def getPacketSendDate(self):
        return self.dateSentNotice

    def getMaterials(self):
        return self.materials


    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setGender(self, gender):
        self.gender = gender

    def setAddress(self, address):
        self.address = address

    def setBalance(self, balance):
        try:
            self.balance = float(balance)
            return True
        except:
            return False

    def setAppStatus(self, status):
        try:
            self.appStatus = int(status)
            return True
        except:
            return False


    def setSession(self, session):
        try:
            self.session = int(session)
            return True
        except:
            return False

    def setBunkhouse(self, bunkhouse):
        try:
            self.bunkhouse = bunkhouse
            return True
        except:
            return False

    def setTribe(self, tribe):
        try:
            self.tribe = int(tribe)
            return True
        except:
            return False

    #def setArrivalReqCert(self):

    #def setCheckedIn(self):

    def setAssignmentRequest(self, request):
        try:
            self.assignmentRequest = request
            return True
        except:
            return False

    def setAssignment(self, camper):
        try:
            self.assignment = camper
            return True
        except:
            return False

    def setPacket(self):
        try:
            self.packetStatus = True
            return True
        except:
            return False

    def setPacketSendDate(self):
        try:
            self.packetStatus = True
            self.dateSentNotice = datetime.now().replace(microsecond = 0)
            return True
        except:
            return False

    #def setMaterials(self):



