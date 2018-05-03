class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        # checks the tax rate based on the cars price
        if price >= 10000:
            self.tax = .15
        else:
            self.tax = .12

        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        # calls the function display_all once all attributes of self have been declared
        self.display_all()
    
    def display_all(self):
        print "Price: " + str(self.price) # not sure if you want this-->> print "Price: " + str(self.price * self.tax + self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + self.fuel
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: " + str(self.tax)

car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, ' Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(2000, 45, 'Empty', 25)
car6 = Car(20000000, 35, 'Full', 15)

