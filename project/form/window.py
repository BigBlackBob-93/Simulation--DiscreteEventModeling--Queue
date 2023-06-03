from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QSpinBox,
    QPushButton,
    QComboBox,
    QTableWidget,
)
from project.form.constants import (
    PARAMETERS,
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
        self.obj.set_obj(
            object=QLabel(self),
            title='Select parameter to track',
            above=self.obj.indent,
            case=0,
        )

        self.obj.add_obj(
            self.obj.set_obj(
                object=QComboBox(self),
                values=PARAMETERS,
                above=self.obj.indent,
                left=LEFT * 10,
            ),
            key='combobox',
        )

        self.obj.increase_indent()
        self.obj.set_obj(
            object=QLabel(self),
            title='Number of operators',
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
                value=4,
            ),
            key='spinbox',
        )

        self.obj.increase_indent(2)
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

