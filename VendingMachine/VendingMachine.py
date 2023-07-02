class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class VendingMachine:

    def __init__(self, products: list):
        self.products = products
        self.__cash_collected = 0

    def buy_product(self, name: str):
        for product in self.products:
            if name == product.name:
                self.__cash_collected += product.price
                self.products.remove(product)

    @property
    def cash_collected(self):
        return self.__cash_collected
    # წესით ეგ მიუწვდომელი უნდა იყოს, მაგრამ რადგან property-ს ვხმარობთ იგი შეგვიძლია გამოვიძახოთ

    @cash_collected.setter
    def cash_collected(self, cash: float):
        if cash >= 0.0:
            self.__cash_collected = cash
        else:
            print("invalid Cash, You really want to go bankrupt With minuses?")



prod1 = Product("cola", 2.4)
prod2 = Product("fanta", 1.2)
vend = VendingMachine([prod1, prod2])

vend.buy_product("cola")
print(vend.cash_collected)
vend.cash_collected = 200
vend.cash_collected = -10
print(vend.cash_collected)