class Camper:
    def __int__(self, fullname, age, gender, address, session, appstatus, balance,
                    tribe, bunkhouse, acceptstatus, arrivalreqcert,
                    checkedin, assignmentrequest, datesentnotice, packetstatus):
            self.fullName = fullname
            self.age = age
            self.gender = gender
            self.address = address
            self.session = session
            self.appStatus = appstatus
            self.balance = balance
            self.tribe = tribe
            self.bunkhouse = bunkhouse
            self.acceptStatus = acceptstatus
            self.arrivalReqCert = arrivalreqcert
            self.checkedIn = checkedin
            self.assignmentRequest = assignmentrequest
            self.dateSentNotice = datesentnotice
            self.packetStatus = packetstatus
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

    def getIndex(self):
        return self.index

    def printApplication(self):
        print(self.appstatus)

    def printAcceptance(self):
        print(self.acceptstatus)

    def printPacket(self):
        print(self.packetstatus)

    def printBalance(self):
        print(self.balance)
