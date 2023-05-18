from product import Product
from store import Store
from database import Database



data = Database()
filename = 'stock.json'

store=Store(data, filename)


while True:
    action = input("enter ('add', 'sell', 'exit'): ")
    if action == 'exit':
        break
    elif action =='add':

        try:
            name = input("Enter the name:")
            quantity = int(input("enter quantity:"))
            purchase_price = int(input("enter purchase price:"))
            product=Product(name,quantity,purchase_price)
            store.add(product)
        except ValueError:
            print('something went wrong!!!')

    elif action == "sell":
        try:
            name = input("Enter the name:")
            quantity = int(input("enter quantity:"))
            store.sell(name,quantity)
        except ValueError:
            print('something went wrong!!!')



#     elif action == 'sell':
#         name = input("Enter the name:")
#         quantity = int(input("enter quantity:"))
#
# # if __name__ == '__main__':
#     filename = 'test.json'
#     db = Database()
#     dd={}
#     store = Store(db, filename)
#     # product = Product('apple', 30, 200)
    # product1 = Product('orange', 20, 400)
    # product2 = Product('orange', 40, 500)
    # product3 = Product('ananas', 40, 500)
    # print(store.products)
    # store.add()
    # store.add(product1)
    # print(store.products)








