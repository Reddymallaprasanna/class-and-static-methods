class student:
    def __init__(s,name,marks):
        s.name=name
        s.maks=marks
    def display(self):
        print(f"Student name:{s.name}")
        print(f"Student marks:{s.maks}")



name=str(input("Enter the name:"))
marks=int(input("Enter the marks:"))
s=student(name,marks)
s.display()