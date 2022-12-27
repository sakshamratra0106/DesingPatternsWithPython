# Open for extension and closed for changes
# OCP increases reusability and reduces maintenance costs.
# To reap these benefits, we must avoid low-cohesive structures.
# Dependencies should be installed with abstractions, not implementations


## Bad Example
def carBehaviourV1(totalSpeed: float, do_Something: str, speed: float):
    if do_Something == "accelerate":
        totalSpeed += speed
    elif do_Something == "brake":
        totalSpeed -= speed * 0.2
    print("0. {}! Current Speed : {}".format(
        do_Something, totalSpeed
    ))


carBehaviourV1(100, "brake", 30)

## After Applying OCP
# We make it more abratract and per do_something accelerat, brake etc So that it will be open extebnsion but closed to change

from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def do_it(self):
        pass


class CarAccelerate(Car):

    def do_it(self, totalSpeed: float, speed: float):
        totalSpeed += speed

        return totalSpeed


class CarBrake(Car):

    def do_it(self, totalSpeed: float, speed: float):
        totalSpeed -= speed + 0.2

        return totalSpeed


def carBehaviourV2(car : Car, totalSpeed: float, speed: float):

    final_Speed = car.do_it(totalSpeed, speed)

    return final_Speed


carAcc = CarAccelerate()
totalSpeed = 100
speed = 30
print("1. If car's total speed is {} and current speed is {} After Acceleration Final speed will be {}".format(
    totalSpeed, speed, carBehaviourV2(carAcc, totalSpeed, speed)
))

carAcc = CarBrake()
totalSpeed = 100
speed = 30
print("2. If car's total speed is {} and current speed is {} After Acceleration Final speed will be {}".format(
    totalSpeed, speed, carBehaviourV2(carAcc, totalSpeed, speed)
))