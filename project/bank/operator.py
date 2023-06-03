from sys import exit


class Operator:
    def __init__(self, id: int):
        self.operator: int = id
        self.time: float | None = None

    def is_free(self) -> bool:
        if self.time is None:
            return True
        return False

    def set_busy(self, time: float):
        self.time = time

    def set_free(self):
        self.time = None

    def get_time(self) -> float | None:
        return self.time


class Operators:
    def __init__(self, count: int):
        self.operators: list[Operator] = [Operator(id=i) for i in range(count)]

    def get_free_operator(self) -> Operator | bool:
        """Returns the nearest free operator, or false if none exists"""
        for operator in self.operators:
            if operator.is_free():
                return operator
        return False

    def get_operator_by_time(self, time: float) -> Operator:
        """Returns the nearest operator by the ending service time, otherwise throws an exception"""
        for operator in self.operators:
            if operator.get_time() == time:
                return operator
        exit("Invalid end of services time")

    def get_number_of_free_operators(self) -> int:
        number: int = 0
        for operator in self.operators:
            if operator.is_free():
                number += 1
        return number
