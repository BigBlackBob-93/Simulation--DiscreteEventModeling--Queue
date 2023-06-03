from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QSpinBox,
    QPushButton,
    QTableWidget,
)
from project.form.constants import (
    WIDTH,
    HEIGHT,
    LEFT,
)
from project.form.base_object import Object


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Simulation: Discrete-event modeling")
        self.setGeometry(350, 300, WIDTH, HEIGHT)

        self.obj: Object = Object()
        self.create_objects()

    def create_objects(self):
        labels: list[str] = ['Number of operators', 'Average customers', 'Service scale']
        for label in labels:
            self.obj.set_obj(
                object=QLabel(self),
                title=label,
                above=self.obj.indent,
                case=0,
            )

            self.obj.add_obj(
                self.obj.set_obj(
                    object=QSpinBox(self),
                    above=self.obj.indent,
                    left=LEFT * 10,
                    step=1,
                    span=[0, 100000000],
                    value=5,
                ),
                key='spinbox',
            )
            self.obj.increase_indent()
        self.obj.increase_indent()

        self.obj.add_obj(
            self.obj.set_obj(
                object=QPushButton(self),
                title='Start/Stop',
                above=self.obj.indent,
                left=LEFT * 3,
            ),
            key='button',
        )
        self.obj.add_obj(
            self.obj.set_obj(
                object=QTableWidget(),
                columns=4,
                title='Bank simulation',
                values=['event type', 'event time', 'queue', 'free operators'],
                width=WIDTH,
            ),
            key='table',
        )
