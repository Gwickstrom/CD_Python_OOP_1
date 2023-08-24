class Bike(object):
    def __init__(self, price=0, max_speed=0, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print self.price, self.max_speed, self.miles
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self

x = Bike(100, 100,10)
x2 = Bike(100,400,20)
x3 = Bike(200,300,30)
x.displayinfo()

x.ride().ride().ride().reverse().displayinfo()

x2.ride()
x2.ride()
x2.reverse()
x2.reverse()

x2.displayinfo()

x3.reverse()
x3.reverse()
x3.reverse()
x3.displayinfo()
