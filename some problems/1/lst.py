from node import Node

class Lst():

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addStudent(self):
        new = Node()

        if self.count == 0:
            self.head = new
            self.tail = self.head
            self.count += 1
        else:
            self.tail.next = new
            self.tail = new
            self.count += 1
    
    def getHead(self):
        return self.head.elev.returnName()
    
    def getTail(self):
        return self.tail.elev.returnName
    
    def returnAddressOfHead(self):
        return self.head

    def displayAllStudentsData(self):
        current = self.head

        while current != None:
            average = 0
            for i in range(0,3):
                bla = current.elev.grades[i]
                average += bla
            print("First name: ", current.elev.returnName())
            print("Last name: ", current.elev.returnSurname())
            print("Grades: ", current.elev.grades)
            print("Average of: ", average/3)
            print("-----------------------------------------------")
            current = current.next

    def displayAverage(self):
        current = self.head
        grades = 0
        while current != None:
            bla = 0
            for i in range(0, 3):
                nota = current.elev.grades[i]
                bla += nota
            grades += bla
            current = current.next
        
        return grades / self.count
    