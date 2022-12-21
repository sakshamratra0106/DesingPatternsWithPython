# https://www.geeksforgeeks.org/abstract-factory-method-python-design-patterns/

class DSA:
    """ Class for Data Structure and Algorithms """

    def __init__(self, price):
        self.price = price

    def fee(self):
        return self.price

    def __str__(self):
        return " Data Structure and Algorithms "


class STL:
    """ Class for Standard Template Library """

    def __init__(self, price):
        self.price = price

    def fee(self):
        return self.price

    def __str__(self):
        return " Standard Template Library "


class SDE:
    """ Class for Software Development Engineer """

    def __init__(self, price):
        self.price = price

    def fee(self):
        return self.price

    def __str__(self):
        return " Software Development Engineer "


if __name__ == '__main__':

    sde = SDE(15000)
    dsa = DSA(11000)
    stl = STL(8000)

    print("Course name is {} and its price is {}".format(
        sde, sde.fee()
    ))

    print("Course name is {} and its price is {}".format(
        dsa, dsa.fee()
    ))

    print("Course name is {} and its price is {}".format(
        stl, stl.fee()
    ))