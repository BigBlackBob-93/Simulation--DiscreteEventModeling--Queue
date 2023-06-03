from PyQt6.QtWidgets import QApplication
import sys
from project.form.simulation import Simulation

if __name__ == '__main__':
    app = QApplication(sys.argv)

    sim: Simulation = Simulation()

    sys.exit(app.exec())
