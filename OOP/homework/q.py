# Design and create an online store of products(name , price)
# Track total products being created
# craete static method to calculate discount on each product based on a % parameter

class Product:
    total_products=0 # track count of total products being created; class var
    # constructor to initialize instance variables
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.total_products+=1
    def get_info(self):
        print(f"Product name is {self.name} and its price is {self.price}")
    # static method to calculate discount
    @staticmethod
    def calc_discount(actual_price,disc_percent):
        final_price = actual_price- actual_price*disc_percent/100
        print(f"Congrats ! New price is {final_price} rupees!")
    
    @classmethod
    def get_total_products(cls):
        print(f"There are {cls.total_products} products available in store")

p1=Product("i-phone",1_50_000)
p2=Product("vivo",40_000)
p3=Product("oppo",34_000)
p4=Product("realme",20_000)

p1.calc_discount(1_50_000,5)
p1.get_info()
Product.get_total_products()
