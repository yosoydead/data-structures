import random
class Elev:
    def __init__(self):
        self.name = self.getName()
        self.surname = self.getSurname()
        self.grades = self.getGrades()
    
    def getName(self):
        nume = str(input("Your name is: "))
        return nume

    def getSurname(self):
        x = str(input("Your surname is: "))
        return x
    
    def getGrades(self):
        x = []
        for i in range(0, 3):
            bla = random.randint(5,10)
            x.append(bla)
        return x

    def returnName(self):
        return self.name
    
    def returnSurname(self):
        return self.surname

    def returnGrades(self):
        return self.grades