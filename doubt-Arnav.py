
'''class Student:
    name=""
    age=0
    gender = ""
    marks=0
    def getStudent(self,r,s,t):
        self.name = r
        self.age = s
        self.gender = t
    def getMarks(self):
        n = 0
        x = 0

        n=int(input("How many tests did you take?"))
        for i in range(n):
            x=x+int(input("What is the mark of one of your tests??"))
        self.marks=x/n
        print(self.marks)
b=int(input("What is your age?"))
a=input("What is your name?")
c=input("What is your gender?")
s1=Student()
s1.getStudent(a,b,c)
s1.getMarks()'''

class Base:
    a=""
    def __init__(self,a):
        self.a=a
    def disp(self):
        print(self.a)
class Derived(Base):
    b=""
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
    def disp(self):
        super().disp()
        print(self.b)
d1=Derived("Arnav","Rishabh")
d1.disp()
import sys
if(True):
    sys.exit()