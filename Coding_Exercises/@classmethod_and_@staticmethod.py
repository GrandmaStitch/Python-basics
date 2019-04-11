# This coding exercise requires you to complete two method implementations.
# 1. The franchise method, which takes in a store as argument. 
# It should return a new Store object, with a name equal to the argument + ' - franchise'.
# 2. The store_details method, which also takes in a store as argument. It should return a string representing the argument.

# e.g:
# store = Store('Test')
# store2 = Store('Amazon')
# store2.add_item('Keyboard', 160)

# Store.franchise(store) returns a Store with name 'Test - franchise'
# Store.franchise(store2) returns a Store with name 'Amazon - franchise'
# Store.store_details(store) returns 'Test, total stock price: 0'
# Store.store_details(store2) returns 'Amazon, total stock price: 160'

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []


    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })


    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total


    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        # method 1
        return cls(store.name + ' - franchise')
        # method 2
        # cls.name = '{} - franchise'.format(store.name)
        # return cls


    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))



# store is an object
store = Store('Test')
store2 = Store('Amazon')
store2.add_item('Keyboard', 160)


print(store)
print(Store.franchise(store))
print(type(Store.franchise(store)))

print(Store.franchise(store2))

print(Store.store_details(store))
print(Store.store_details(store2))

# Extended:
# call class method by the class
print(Store.franchise(Store('Apple')))
print(Store.franchise(Store('Apple')).name)
# call class method by it's object
obj = Store('Banana')
print(Store.franchise(obj))
print(Store.franchise(obj).name)

# check if Store.franchise() creates a new object
print(obj == Store.franchise(obj))

# 0x10bc84cc0, 0x102968cf8, 0x10b7a3cf8
