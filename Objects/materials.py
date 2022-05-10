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

    def getCompletedForms(self):

        return self.medical and self.legal and self.emergencyContacts \
                and self.helmet and self.boots and self.sleepingBag \
                and self.waterBottle and self.sunscreen and self.bugSpray


    def getMedical(self):
        return self.medical

    def getLegal(self):
        return self.legal

    def getEmergencyContacts(self):
        return self.emergencyContacts


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

    def setEmergencyContacts(self, emergencyContacts):
        self.emergencyContacts = emergencyContacts


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


