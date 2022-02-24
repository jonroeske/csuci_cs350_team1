class Bunkhouse:
    def __int__(self, campers, agerange, gender):
        self.campers = campers
        self.agerange = agerange
        self.gender = gender

    def isFull(self):
        return len(campers) == 12

    def append(self, newcamper):
        if not isFull(self):
            campers.append(newcamper)
            return True
        else:
            return False
