class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price >10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        
        
    def display_all(self):
        print "Price: ${}".format(self.price)
        print "Speed: {}MPH".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}MPG".format(self.mileage)
        print "Tax: {}".format(self.tax)
        return self
        

car1 = Car(2000, 35, "Full", 15)
car2 = Car(2000, 5, "Full", 105)
car3 = Car(2000, 50, "Kind of Full", 95)
car4 = Car(2000, 25, "Full", 25)
car5 = Car(2000, 45, "Empty", 35)
car6 = Car(2000000, 35, "Empty", 15)

print car1.display_all()
print "*" * 50
print car2.display_all()
print "*" * 50
print car3.display_all()
print "*" * 50
print car4.display_all()
print "*" * 50
print car5.display_all()
print "*" * 50
print car6.display_all()
