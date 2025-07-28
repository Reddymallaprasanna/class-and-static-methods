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
        
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def div(self):
        try:
            result=self.a/self.b
            return result
        except ZeroDivisionError:
            print("Division by zero is not possible")
        
   
c=calculator.input()
print("Addition result:",c.add())
print("Subtraction result:",c.sub())
print("Division result:",c.div())