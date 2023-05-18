# from product import Product
# from database import Database


class Store:
    def __init__(self, database, filename):
        self.db = database
        self.prod_filename = filename
        self.products = self.db.load(self.prod_filename)
        self.profit = 0

    def add(self, product):
        if product.name in self.products:
            if product.purchase_price != self.products[product.name]['purchase_price']:
                self.products[product.name]['Quantity'] += product.quantity
                self.products[product.name]['purchase_price'] = product.purchase_price
                print("Price and quantity of product has been changed:")
            else:
                self.products[product.name]['Quantity'] += product.quantity
                print("Quantity of the produce has been changed:")
        else:
            self.products[product.name] = {'Quantity': product.quantity,
                                           'purchase_price': product.purchase_price,
                                           'payment_price': product.payment_price}

            print("Product has been added: ")
        self.db.save(self.products, self.prod_filename)

    def sell(self, name, quantity):
        if name in self.products and self.products[name]['Quantity'] >= quantity:
            self.products[name]['Quantity'] -= quantity
            self.profit += (self.products[name]['payment_price'] - self.products[name]['purchase_price']) * quantity
            self.check_del(name)
            self.db.save(self.products, self.prod_filename)

        else:
            print("!!!Product is not available!!!")


    def check_del(self, name):
        if self.products[name]['Quantity'] == 0:
            del self.products[name]

    def show_profit(self):
        return self.profit



# if __name__ == '__main__':
#     filename = 'test.json'
#     db = Database()
#     store = Store(db, filename)
#     product = Product('apple', 30, 200)
#     product1 = Product('orange', 20, 400)
#     product2 = Product('orange', 40, 500)
#     product3 = Product('ananas', 40, 500)
#     print(store.products)
#     store.add(product)
#     store.add(product1)
# #     print(store.products)
#     store.sell("apple", 30)
# #     print(store.products)
# #     store.add(product2)
#     print(store.products)
#     store.add(product2)
#     print(store.products)
#     store.add(product3)
#
#     store.sell('orange', 20)
#     print(store.products)
#     store.sell("apple", 26)
#     print(store.products)
