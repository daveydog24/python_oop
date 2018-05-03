# Bike Assignmet 
# NOTE--> I ADDED NAME JUST TO MAKE IT MORE OF A LITTLE STORY 

# class Bike has an object ready to be passed through if necessary 
class Bike(object):
    # initializes the instance passed through and is ready to take on 3 arguments
    def __init__(self, name, price, max_speed):
        self.name = name
        self.price = price
        self.max_speed = int(max_speed)
        self.miles = 0
    # Will print all the current info of the bike
    def displayInfo(self):
        print self.name + "'s price is: $" + str(self.price)
        print self.name + "'s max speed: " + str(self.max_speed) + "mph"
        print self.name + "'s total miles: " + str(self.miles) + " miles"  
        return self   
    # function that logs the miles of the bike being riden and stores the new information
    def ride(self):
        print "Riding " + self.name
        self.miles += 10
        return self
    # function that logs the miles of the bike going in reverse when called on and stores the new info
    def reverse(self):
        print "Reversing " + self.name
        if self.miles >= 5:
            self.miles -= 5
        return self

# my 3 instances of new bikes requrired by the assignment 
bike1 = Bike('Bike1', 200, 25)
bike2 = Bike('Bike2', 100, 40)
bike3 = Bike('Bike3', 300, 125)

bike1.ride().ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().displayInfo()
bike3.displayInfo()