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

    def setAppStatus(self, status):
        try:
            self.appStatus = status
            return True
        except:
            return False

    def setBalance(self, balance):
        try:
            self.balance = balance
            return True
        except:
            return False
