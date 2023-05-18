class Product:
    def __init__(self, name, quantity, purchase_price):
        self.name = name
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.payment_price = self.purchase_price + self.purchase_price* 0.2



