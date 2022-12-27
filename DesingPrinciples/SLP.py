from abc import ABC, abstractmethod

class Phone(ABC):

    @abstractmethod
    def dail(self):
        pass

    @abstractmethod
    def hangup(self):
        pass

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def recieve(self):
        pass


# With Proper Abstraction and Segregation of Responsibility above class Phone would become

class DataHandler:

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def recieve(self):
        pass

class PhoneConnection:

    @abstractmethod
    def dail(self):
        pass

    @abstractmethod
    def hangup(self):
        pass

# If we start having trouble abstracting due to growth, we can go up one level.
# We can convert a line to a block, a block to a method, a method to a class, etc.