from abc import ABC, abstractmethod
import sdh_common_utilities
# Import everything required for all the checks

class Checks:

    @abstractmethod
    def check(self):
        pass

class Duplicate(Checks):

    def check(self, df) -> dict:
        """
        comments
        """

        #Implimentation


class CyclicHierarchy(Checks):

    def check(self, df) -> dict:
        """
        comments
        """

        #Implimentation


class NotInSFDC(Checks)

    def check(self, df) -> dict:
        """
        comments
        """

        #Implimentation

class YesterdayMissingCSN(Checks):

    def check(self, key) -> dict:
        """
        comments
        """

        #Implimentation

class ValidCSN(Checks):

    def check(self, df) -> dict:
        """
        comments
        """

        #Implimentation

