# https://levelup.gitconnected.com/design-patterns-in-python-factory-pattern-beea1da31c17

from abc import ABC, abstractmethod


class AbstractCar(ABC):

    @abstractmethod
    def get_body_type(self):
        pass


class SedanCar(AbstractCar):

    def __init__(self):
        self.body = "Sedan"

    def get_body_type(self):

        return "Body Type : {}".format(self.body)


class HatchbackCar(AbstractCar):

    def __init__(self):
        self.body = "Hatchback"

    def get_body_type(self):

        return "Body Type : {}".format(self.body)


class PickupCar(AbstractCar):

    def __init__(self):
        self.body = "Pickup"

    def get_body_type(self):

        return "Body Type : {}".format(self.body)


class CarFactory:

    @staticmethod
    def build_car(plan):
        try:
            if plan == "Sedan":
                return SedanCar()
            elif plan == "Hatchback":
                return HatchbackCar()
            elif plan == "Pick-Up":
                return PickupCar()
            raise AssertionError("Car type is not valid.")
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    # plan_list = ["Sedan", "Hatchback", "Pick-Up", "Motobike"]
    plan_list = ["Sedan", "Hatchback", "Pick-Up", ]
    for p in plan_list:
        car = CarFactory.build_car(p)
        body = car.get_body_type()
        print(body)