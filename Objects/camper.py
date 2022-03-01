class Camper:
    def __int__(self, fullname, age, gender, address):
        self.fullName = fullname
        self.age = age
        self.gender = gender
        self.address = address
        self.session = None
        self.appStatus = False
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
        self.emergencycontacts = None
        self.helmet = None
        self.boots = None
        self.sleepingbag = None
        self.waterbottle = None
        self.sunscreen = None
        self.bugspray = None

    def getName(self):
        return self.fullName

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getAddress(self):
        return self.address

    def getApplication(self):
        return self.appStatus

    def getAcceptance(self):
        return self.acceptStatus

    def getPacket(self):
        return self.packetStatus

    def getBalance(self):
        return self.balance
