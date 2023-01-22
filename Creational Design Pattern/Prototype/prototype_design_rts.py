from abc import ABCMeta, abstractmethod, ABC
from copy import deepcopy


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass


class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)


class Knight(Prototype):

    def __init__(self, level):
        self.unit_type = "knight"
        filename = "{}_{}.dat".format(self.unit_type, level)
        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\n" \
               "Life: {1}\n" \
               "Speed: {2}\n" \
               "Attack Power: {3}\n" \
               "Attack Range: {4}\n" \
               "Weapon: {5}".format(
            self.unit_type,
            self.life,
            self.speed,
            self.attack_power,
            self.attack_range,
            self.weapon
        )

    def clone(self):
        return deepcopy(self)


class Archer(Prototype):

    def __init__(self, level):
        self.unit_type = "archer"
        filename = "{}_{}.dat".format(self.unit_type, level)

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\n" \
               "Life: {1}\n" \
               "Speed: {2}\n" \
               "Attack Power: {3}\n" \
               "Attack Range: {4}\n" \
               "Weapon: {5}".format(
            self.unit_type,
            self.life,
            self.speed,
            self.attack_power,
            self.attack_range,
            self.weapon
        )

    def clone(self):
        return deepcopy(self)


class Barracks(object):

    # Since with the creation of object of Barracks
    # Initialization Starts
    # We have to confirm if all Initialization of Knight and Archer Works
    def __init__(self):
        self.units = {
            "knight": {
                1: Knight(1),
                2: Knight(2)
            },
            "archer": {
                1: Archer(1),
                2: Archer(2)
            }
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    archer1 = barracks.build_unit("archer", 2)
    print("[knight1] {}".format(knight1))
    print("[archer1] {}".format(archer1))
