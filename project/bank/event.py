from random import random
from project.bank.types import EventType


def generator() -> float:
    return random()


class Events:
    def __init__(self):
        self.times: list[float] = []
        self.types: list[EventType] = []

    def add_event(self, model_time: float, event_type: EventType = EventType.end_of_services) -> float:
        """Adds new event and returns its time"""
        time: float = self.get_next_time(model_time)
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

    @staticmethod
    def get_next_time(model_time: float) -> float:
        return model_time + generator()
