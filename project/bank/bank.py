from project.bank.queue import Queue
from project.bank.operator import Operators, Operator
from project.bank.event import Events
from project.bank.types import EventType
from sys import exit


class Bank:
    def __init__(self, operators_count: int, average: int, scale: int):
        self.model_time: float = 0
        self.queue: Queue = Queue()
        self.operators: Operators = Operators(operators_count)
        self.events: Events = Events(average=average, scale=scale)
        self.current_event_type: EventType = EventType.new_customer

    def new_customer(self) -> None:
        self.events.add_event(model_time=self.model_time, event_type=EventType.new_customer)
        self.new_state()

    def new_service(self, operator: Operator) -> None:
        """Creates a new service end event, adds it to the current, and sets the operator to busy"""
        time: float = self.events.add_event(model_time=self.model_time, event_type=EventType.end_of_services)
        operator.set_busy(time=time)

    def customer_arrived(self) -> None:
        """Sends new customer to the operator or adds him to the queue"""
        operator: Operator | False = self.operators.get_free_operator()
        if operator:
            self.new_service(operator=operator)
        else:
            self.queue.add_customer()

    def service_ended(self) -> None:
        """Sends customer from the queue to the operator or sets operator to free"""
        operator: Operator = self.operators.get_operator_by_time(time=self.model_time)
        if self.queue.is_empty():
            operator.set_free()
        else:
            self.new_service(operator=operator)
            self.queue.del_customer()

    def new_state(self) -> None:
        """Handles the event by bringing the system to a new state, returns type of last event"""
        self.model_time, self.current_event_type = self.events.get_nearest_event()

        if self.current_event_type is EventType.new_customer:
            self.customer_arrived()
        elif self.current_event_type is EventType.end_of_services:
            self.service_ended()
        else:
            exit('Invalid event type')
