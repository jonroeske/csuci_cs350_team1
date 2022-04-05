from datetime import datetime
class Camper:
    def __int__(self, fullname, age, gender, address):
        self.fullName = fullname
        self.age = age
        self.gender = gender
        self.address = address
        self.session = None
        self.appStatus = 0
        self.balance = 0.00
        self.tribe = None
        self.bunkhouse = None
        self.acceptStatus = False
        self.arrivalReqCert = False
        self.checkedIn = False
        self.assignmentRequest = None
        self.dateSentNotice = None
        self.packetStatus = False
        self.medical = None
        self.legal = None
        self.emergencyContacts = None
        self.helmet = None
        self.boots = None
        self.sleepingBag = None
        self.waterBottle = None
        self.sunscreen = None
        self.bugSpray = None

    def __eq__(self, other):
        if isinstance(other, Camper):
            return (self.fullName, self.age, self.gender, self.address) == (other.fullName, other.age, other.gender, other.address)
        else:
            return False

    def getName(self):
        return self.fullName

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getAddress(self):
        return self.address

    def getAppStatus(self):
        return self.appStatus

    def getAcceptance(self):
        return self.acceptStatus

    def getPacket(self):
        return self.packetStatus

    def getBalance(self):
        return self.balance

    def getPacketSendDate(self):
        return self.dateSentNotice

    def getTribe(self):
        return self.tribe

    def getBunkhouse(self):
        return self.bunkhouse

    def setPacketSend(self):
        try:
            self.packetStatus = True
            self.dateSentNotice = datetime.now()
            return True
        except:
            return False

    def setAppStatus(self, status):
        try:
            self.appStatus = int(status)
            return True
        except:
            return False

    def setBalance(self, balance):
        try:
            self.balance = float(balance)
            return True
        except:
            return False

    def setTribe(self, tribe):
        try:
            self.tribe = int(tribe)
            return True
        except:
            return False

    def setBunkhouse(self, bunkhouse):
        try:
            self.bunkhouse = int(bunkhouse)
            return True
        except:
            return False

    def setRequest(self, camper):
        try:
            self.assignmentRequest = camper
            return True
        except:
            return False