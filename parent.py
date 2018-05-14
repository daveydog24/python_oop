import product
if __name__ == "__main__":
    item1 = product.Product(5, "Frosted Flakes", 1, "Kellog")
    item1.sell().returned("damaged", "used").display_Info()

if __name__ == "__main__":
    item2 = product.Product(2, "King Size Snickers", .5, "Nestle")
    item2.sell().returned("defective", "new").display_Info()

if __name__ == "__main__":
    item3 = product.Product(10, "Tide Pods", 2, "Tide")
    item3.sell().returned("damaged", "new").display_Info()

class Store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        self.products.remove(product)
        return self

    def inventory(self):
        for product in self.products:
            print product.display_Info()

if __name__ == "__main__":
    product = Product([args])
    
#  add a location and a owner for each store 
if __name__ == "__main__":
    store1 = Store("Seattle, WA", "David Wukelic")

# print adding products plus execute the action between the two classes
print "Adding products..."
if __name__ == "__main__":
    store1.add_product(item1).add_product(item2).add_product(item3)

# display inventory
print "Store inventory:"
if __name__ == "__main__":
    store1.inventory()
