class Materials:
    def __init__(self):
        # FORMS
        self.medical = False
        self.legal = False
        self.emergencyContacts = False

        # EQUIPMENT
        self.helmet = False
        self.boots = False
        self.sleepingBag = False

        # SUPPLIES
        self.waterBottle = False
        self.sunscreen = False
        self.bugSpray = False


    def getMedical(self):
        return self.medical

    def getLegal(self):
        return self.legal

    def getEmergencyContacts(self):
        return self.emergencyContactss


    def getHelmet(self):
        return self.helmet

    def getBoots(self):
        return self.boots

    def getSleepingBag(self):
        return self.sleepingBag


    def getWaterBottle(self):
        return self.waterBottle

    def getSunscreen(self):
        return self.sunscreen

    def getBugSpray(self):
        return self.bugSpray


    def setMedical(self, medical):
        self.medical = medical

    def setLegal(self, legal):
        self.legal = legal

    def setEmergencyContacts(self, emergencyContactss):
        self.emergencyContactss = emergencyContactss


    def setHelmet(self, helmet):
        self.helmet = helmet

    def setBoots(self, boots):
        self.boots = boots

    def setSleepingBag(self, sleepingBag):
        self.sleepingBag = sleepingBag


    def setWaterBottle(self, waterBottle):
        self.waterBottle = waterBottle

    def setSunscreen(self, sunscreen):
        self.sunscreen = sunscreen

    def setBugSpray(self, bugSpray):
        self.bugSpray = bugSpray


