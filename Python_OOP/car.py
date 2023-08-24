class Car(object):
    def __init__(self, price=0, speed=None, fuel=None, mileage=None):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if(self.price > 10000):
            self.tax = .15
        else:
            self.tax = .12
    def display_all(self):
        print "Price:",self.price
        print "Speed:",self.speed
        print "Fuelage:",self.fuel
        print "Mileage:",self.mileage
        print "Tax:",self.tax
        print

x = Car(2000,"35mph","Full", "15mpg")

x.display_all()

x2 = Car(200000, "40mph", "Empty", "300mph")

x2.display_all()

x3 = Car(300000, "50mph", "Half", "2550mph")

x3.display_all()

x4 = Car(20000, "40mph", "Stuff", "300mph")

x4.display_all()

x5 = Car(20000, "300mph", "Half", "20000mph")

x5.display_all()

x6 = Car(1000, "200mph", "Full", "200mph")

x6.display_all()
