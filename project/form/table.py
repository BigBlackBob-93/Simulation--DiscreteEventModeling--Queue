from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
)


class Table:
    def __init__(self, table: QTableWidget):
        self.table: QTableWidget = table
        self.table.show()

    def upd_table(self, data: list[str], row: int) -> None:
        self.table.insertRow(row)
        for column, item in enumerate(data):
            self.table.setItem(row, column, QTableWidgetItem(item))
        self.table.resizeColumnsToContents()

    def clear_table(self) -> None:
        self.table.setRowCount(0)
