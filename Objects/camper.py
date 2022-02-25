class Camper:
    def __int__(self, fullname, age, gender, address, session, appstatus, balance,
                    tribe, bunkhouse, acceptstatus, arrivalreqcert,
                    checkedin, assignmentrequest, datesentnotice, packetstatus):
            self.fullName = fullname
            self.age = age
            self.gender = gender
            self.address = address
            self.session = session
            self.appstatus = appstatus
            self.balance = balance
            self.tribe = tribe
            self.bunkhouse = bunkhouse
            self.acceptstatus = acceptstatus
            self.arrivalreqcert = arrivalreqcert
            self.checkedin = checkedin
            self.assignmentrequest = assignmentrequest
            self.datesentnotice = datesentnotice
            self.packetstatus = packetstatus

    def getName(self):
        return self.fullName

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getAddress(self):
        return self.address

    def printApplication(self):
        print(self.appstatus)

    def printAcceptance(self):
        print(self.acceptstatus)

    def printPacket(self):
        print(self.packetstatus)

    def printBalance(self):
        print(self.balance)
