'''
code to calculate a product with its price by normal instance
and calculat he products tax by 10% in  Class method and print the total ount to be paid....
'''
class product:
    tax_rate=0.18
    def __init__(self,name,price,rate):
        self.name=name
        self.price=price
        self.rate=rate
    def final_price(self):
        tot=self.price*(1+product.tax_rate)
        print(f" Finalprice of {self.name} is  rs.{tot:.2f}")
    @classmethod
    def set_tax(cls,rate):
        cls.tax_rate=rate/100

name=str(input("Enter the prosuct name:"))
price=float(input("Enter th price of the product:"))
rate=int(input("Enter the tax rate in % :"))
product.set_tax(rate)
item=product(name,price,rate)
item.final_price()