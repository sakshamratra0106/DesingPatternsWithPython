from abc import ABC, abstractmethod
import logging
from typing import List

logging.basicConfig(level=logging.INFO)


class Strategy(ABC):

    @abstractmethod
    def do_sort(self, data:  List):
        pass


class SortAsc(Strategy):

    def do_sort(self, data:  List):

        return sorted(data)


class SortDesc(Strategy):

    def do_sort(self, data: List):

        return sorted(data, reverse=True)


class Context:

    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_bussiness_logic(self):

        statement = "After Sorting array will be {}"
        result = self._strategy.do_sort(["a", "c", "d", "b", "e"])

        return statement.format(result)


if __name__ == '__main__':

    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = Context(SortAsc())
    print("Client : Call the Sorting Strategy Ascending {}".format(context.do_some_bussiness_logic()))
    context.strategy = SortDesc()
    print("Client : Call the Sorting Strategy Ascending {}".format(context.do_some_bussiness_logic()))

