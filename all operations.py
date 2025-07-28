'''
basic math operation using @classmethod
'''
class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    @classmethod
    def input(cls):
            a = int(input("Enter the value of a:"))
            b = int(input("Enter the value of b:"))
            return cls(a,b)
        
    def  calculations(self):
        print("Addition:",self.a+self.b)
        print("Sutraction:",self.a-self.b)
        print("Multiplication",self.a*self.b)
        print("Power :",self.a**self.b)
    def div(self):
        try:
            print("Division:",self.a/self.b)
            
        except ZeroDivisionError:
            print("Division by zero is not possible")
c=calculator.input()
c.calculations()
c.div()

