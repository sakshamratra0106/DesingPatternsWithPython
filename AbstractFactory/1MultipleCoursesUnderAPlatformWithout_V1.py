# https://www.geeksforgeeks.org/abstract-factory-method-python-design-patterns/

class DSA:
    """ Class for Data Structure and Algorithms """

    def __init__(self, price):
        self.price = price

    def fee(self):
        return self.price

    def timings(self):
        return "9 AM to 10 AM"

    def __str__(self):
        return " Data Structure and Algorithms "


class STL:
    """ Class for Standard Template Library """

    def __init__(self, price):
        self.price = price

    def fee(self):
        return self.price

    def timings(self):
        return "10 AM to 11 AM"

    def __str__(self):
        return " Standard Template Library "


class SDE:
    """ Class for Software Development Engineer """

    def __init__(self, price):
        self.price = price

    def fee(self):
        return self.price

    def timings(self):
        return "11 AM to 12 PM"

    def __str__(self):
        return " Software Development Engineer "


if __name__ == '__main__':

    sde = SDE(15000)
    dsa = DSA(11000)
    stl = STL(8000)

    print("Course name is {}. Its details are : price is {} and timings is {}".format(
        sde, sde.fee(), sde.timings()
    ))

    print("Course name is {}. Its details are : price is {} and timings is {}".format(
        dsa, dsa.fee(), dsa.timings()
    ))

    print("Course name is {}. Its details are : price is {} and timings is {}".format(
        stl, stl.fee(), stl.timings()
    ))