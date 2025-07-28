'''
static method @staticmethod
'''
class student:
    gender='Male'
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"name :{self.name}")
    @classmethod
    def getname(cls):
        return cls.gender
    @staticmethod
    def residence(type_of_resedent):
        if type_of_resedent=="Indian" or "India" or "indian" or "INDIA":
            return "The person is Indian"
        else:
            return "The person is not Indian"
name=str(input("Enter your name:"))
type=input("Enter resedence or non-resedence:")
s=student(name)
s.display()
print("Student name:",student.getname())
print(s.residence(type))