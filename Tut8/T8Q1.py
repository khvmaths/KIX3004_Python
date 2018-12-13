class Person:
    def __init__(self,nm,mk,sn):
        self.name=nm
        self.mykad=mk
        self.id=sn
    def getName(self):
        return self.name
    def getMyKad(self):
        return self.mykad

class Student(Person):
    def __init__(self,nm,mk,sn):
        Person.__init__(self,nm,mk,sn)
    def getStudNumber(self):
        return self.id

class Lecturer(Person):
    def __init__(self,nm,mk,sn,sal):
        Person.__init__(self,nm,mk,sn)
        self.salary=sal
    def getStaffNumber(self):
        return self.id
    def getSalary(self):
        return self.salary