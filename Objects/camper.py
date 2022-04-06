from datetime import datetime
class Camper:
    def __int__(self, fullname, age, gender, address):
        # CAMPER DESCRIPTION
        self.fullName = fullname
        self.age = age
        self.gender = gender
        self.address = address
        self.balance = 0.00
        self.appStatus = 0
        #self.acceptStatus = False  DEPRECIATED
        # CAMPER CAMP DETAILS
        self.session = None
        self.bunkhouse = None
        self.tribe = None
        self.arrivalReqCert = False
        self.checkedIn = False

        # CAMPER SUPPLIES + REQUEST
        self.assignmentRequest = None
        self.packetStatus = False
        self.dateSentNotice = None
        self.materials = None

    def __eq__(self, other):
        if isinstance(other, Camper):
            return (self.fullName, self.age, self.gender, self.address) == (other.fullName, other.age, other.gender, other.address)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Camper):
            return (self.fullName < other.fullName)
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Camper):
            return (self.fullName > other.fullName)
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

    def getBalance(self):
        return self.balance

    def getAppStatus(self):
        return self.appStatus

    #def getAcceptance(self):       DEPRECIATED
    #    return self.acceptStatus

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

    def getPacket(self):
        return self.packetStatus

    def getPacketSendDate(self):
        return self.dateSentNotice

    def getMaterials(self):
        return self.materials



    def setPacketSend(self):
        try:
            self.packetStatus = True
            self.dateSentNotice = datetime.now().replace(microsecond = 0)
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

    def setSession(self, session):
        try:
            self.session = session
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

    def setAssignmentRequest(self, camper):
        try:
            self.assignmentRequest = camper
            return True
        except:
            return False