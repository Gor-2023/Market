import json

class Database:
    def load(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

    def save(self,dict_val, filename):
        with open(filename, 'w') as f:
            json.dump(dict_val, f, indent=4)

# if __name__ == '__main__':
#
#     db = Database()
#     filename = 'stock.json'
#     filename2 = 'test.json'
#
#     testdict2 = db.load(filename2)
#     print(testdict2)
#     testdict2['er']= 456546455
#     print(testdict2)
#     db.save(testdict2, filename2)