from project.form.window import MainWindow
from project.form.timer import Timer
from project.form.table import Table
from project.bank.bank import Bank
from project.bank.types import EventType
from typing import Any


class Simulation:
    def __init__(self):
        self.window: MainWindow = MainWindow()
        self.window.show()
        self.window.obj.objects.get('button')[0].clicked.connect(self.check_state)
        self.table: Table = Table(self.window.obj.objects.get('table')[0])

        self.sensor: bool = False
        self.timer: Timer = Timer()
        self.system: Bank = Any
        self.iteration: int = 0

    def check_state(self):
        if self.sensor:
            self.sensor = False
            self.stop()
        else:
            self.sensor = True
            self.start()

    def start(self):
        self.table.clear_table()
        self.system = Bank(self.window.obj.objects.get('spinbox')[0].value())
        self.timer.start(self.shot)

    def stop(self):
        self.timer.stop()
        self.iteration = 0

    def shot(self):

        if self.system.current_event_type is EventType.new_customer:
            self.system.new_customer()
        else:
            self.system.new_state()

        self.table.upd_table(
            data=[
                str(self.system.current_event_type.value),
                str(round(self.system.model_time, 2)),
                str(self.system.queue.customers),
                str(self.system.operators.get_number_of_free_operators())
            ],
            row=self.iteration,
        )
        self.iteration += 1
