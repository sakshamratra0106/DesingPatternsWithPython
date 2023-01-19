# Adding new changes to the existing code where we add timings to the courses

import random


class Courses:
    """
    Abstract Factory for courses
    """

    def __init__(self, course_factory=None):
        """ Random Function is being passed as an Object here"""
        self.course_factory = course_factory

    def show_course(self):
        """Initialize the object of course and get its details
        Below lines were repeated 3 times in previous code"""

        # Random Function is being called and Course is being assigned randomly
        course = self.course_factory()

        print("Course name is {}. Its details are : price is {} and timings is {}".format(
            course, course.fee(), course.timings()
        ))


class DSA:
    """ Class for Data Structure and Algorithms """

    def fee(self):
        return 11000

    def timings(self):
        return "9 AM to 10 AM"

    def __str__(self):
        return " Data Structure and Algorithms "


class STL:
    """ Class for Standard Template Library """

    def fee(self):
        return 8000

    def timings(self):
        return "10 AM to 11 AM"

    def __str__(self):
        return " Standard Template Library "


class SDE:
    """ Class for Software Development Engineer """

    def fee(self):
        return 15000

    def timings(self):
        return "11 AM to 12 PM"

    def __str__(self):
        return " Software Development Engineer "


def random_course():
    """ Choose random Course Class"""

    # Below line Selects a random Class
    # random.choice([SDE, STL, DSA])
    # Below line instantiates an object of a class
    # random.choice([SDE, STL, DSA])()

    return random.choice([SDE, STL, DSA])()


if __name__ == '__main__':

    # Passing function as an argument to the class Courses
    course = Courses(random_course)

    for i in range(5):
        course.show_course()
