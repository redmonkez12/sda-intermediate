# Method resolution order

# Diamond problem

# class RandomClass(SomeClass, OtherClass):

class Food:
    def __repr__(self):
        return "Wooow super jidlo"


class Pizza(Food):
    def __repr__(self):
        return "Pizza s ananasem. Italie vraci uder!"


class Sandwich(Food):
    def __repr__(self):
        return "Yummy jidlo"


class Calzone(Pizza, Sandwich):
    pass


calzone = Calzone()
print(Calzone.__mro__)
print(calzone)
