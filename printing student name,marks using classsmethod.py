class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @classmethod
    def input(cls):
        name=str(input("Enter Student name:"))
        marks=int(input("Enter Student marks:"))
        return cls(name,marks)
    def display(self):
        print(f"Student name is:{self.name},Student marks is:{self.marks}")

s=student.input()
s.display()