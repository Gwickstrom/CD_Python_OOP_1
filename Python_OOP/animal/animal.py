class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "Animal:", self.name
        print "Health:", self.health
        print

animal = Animal("Giraffe")

animal.walk().walk().walk().run().run().displayHealth()

# class Dog(Animal):
#     def __init__(self, name):
#         super(Dog, self).__init__(name)
#         self.health = 150
#     def pet(self):
#         self.health += 5
#         return self
#
# class Dragon(Animal):
#     def __init__(self, name):
#         super(Dragon, self).__init__(name)
#         self.health = 170
#     def fly(self):
#         self.health -= 10
#         return self
#     def displayHealth(self):
#         print "This is a Dragon"
#         super(Dragon, self).displayHealth()
#
#
#
# dog = Dog("Dog")
# dog.walk().walk().walk().run().run().pet().displayHealth()
#
# dragon = Dragon("Dragon")
# dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
