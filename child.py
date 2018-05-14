class Product(object):
    # initialize attributes to the product passing through
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    # function marks the item as sold and then moves to tax it
    def sell(self):
        self.status = "sold"
        self.addTax()
        return self

    # function adds sales tax
    def addTax(self):
        self.price = self.price + (self.price * .0988888)
        return self
        
    # function checks reasoning and condition of item being returned and adjust info accordingly
    def returned(self, reason, box_condition):
        self.reason = reason
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if box_condition == "in the box" or "new":
            self.status = "for sale"
        else:
            self.status = "used"
            self.price = self.price * (.80)
        return self

    # function displays all the information of the current product
    def display_Info(self):
        print "Item Price: $" + str(self.price)
        print "Item Name: " + self.item_name
        print "Item Status: " + self.status
        print "Item Weight: " + str(self.weight) + " lb"
        print "Item Brand: " + self.brand