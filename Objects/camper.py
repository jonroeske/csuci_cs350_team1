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

        # CAMPER PARTNER REQUEST
        self.hasPartner = False
        self.partner = None

        # CAMPER CAMP DETAILS
        self.session = False
        self.bunkhouse = False
        self.tribe = False

        # CAMPER SUPPLIES + REQUEST
        self.checkedIn = False
        self.appNoticeIsSent = False
        self.dateAppNoticeSent = None
        self.materials = None

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


    def getHasPartner(self):
        return self.hasPartner

    def getPartner(self):
        return self.partner


    def getSession(self):
        return self.session

    def getBunkhouse(self):
        return self.bunkhouse

    def getTribe(self):
        return self.tribe


    def getCheckedIn(self):
        return self.checkedIn

    def getAppNoticeIsSent(self):
        return self.appNoticeIsSent

    def getDateAppNoticeSent(self):
        return self.dateAppNoticeSent

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
            self.balance = round(float(balance), 2)
            return True
        except:
            return False

    def setAppStatus(self, status):
        try:
            self.appStatus = int(status)
            return True
        except:
            return False


    def setHasPartner(self, boolean):
        try:
            self.hasPartner = boolean
            return True
        except:
            return False

    def setPartner(self, camper):
        try:
            self.partner = camper
            return True
        except:
            return False


    def setSession(self, session):
        try:
            self.session = session
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
            self.tribe = tribe
            return True
        except:
            return False


    def setCheckedIn(self, boolean):
        try:
            self.checkedIn = boolean
            return True
        except:
            return False

    def setAppNoticeIsSent(self, boolean):
        try:
            self.appNoticeIsSent = boolean
            return True
        except:
            return False

    def setDateAppNoticeSent(self, date):
        try:
            self.dateAppNoticeSent = date
            return True
        except:
            return False

    def setMaterials(self, materialsObject):
        try:
            self.materials = materialsObject
            return True
        except:
            return False


