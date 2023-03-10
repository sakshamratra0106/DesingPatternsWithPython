class Knight:

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


class Archer:

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


class Baracks:

    def build_unit(self, unit_type, level):

        if unit_type == "knight":
            return Knight(level)
        elif unit_type == "archer":
            return Archer(level)


if __name__ == "__main__":
    baracks = Baracks()
    knight1 = baracks.build_unit("knight", 1)
    archer1 = baracks.build_unit("archer", 2)
    print("[knight1] {}".format(knight1))
    print("[archer1] {}".format(archer1))

