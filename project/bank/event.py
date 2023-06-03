from scipy.stats import expon
from math import log as ln
from random import random
from project.bank.types import EventType


def generator() -> float:
    return random()


class Events:
    def __init__(self, average: int, scale: int):
        self.scale: int = scale
        self.average: int = average
        self.times: list[float] = []
        self.types: list[EventType] = []

    def add_event(self, model_time: float, event_type: EventType = EventType.end_of_services) -> float:
        """Adds new event and returns its time"""
        time: float = self.get_next_time(model_time, event_type)
        self.times.append(time)
        self.types.append(event_type)
        return time

    def del_event(self, index: int):
        self.times.pop(index)
        self.types.pop(index)

    def get_nearest_event(self) -> tuple:
        """Returns data of the nearest event (tuple of time and type) after deleting this event from current"""
        index = self.times.index(min(self.times))
        time = self.times[index]
        event_type = self.types[index]
        self.del_event(index)
        return time, event_type

    def get_next_time(self, model_time: float, event_type: EventType) -> float:
        if event_type is EventType.new_customer:
            return model_time + self.get_customer_arrival_time()
        else:
            return model_time + self.get_end_of_service_time()

    def get_customer_arrival_time(self) -> float:
        return - ln(generator()) / self.average

    def get_end_of_service_time(self) -> float:
        return expon.rvs(scale=self.scale)
