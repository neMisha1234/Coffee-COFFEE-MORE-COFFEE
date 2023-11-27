from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
import sqlite3
import sys
import random


class CoffeeWidjet(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.tableWidget.setColumnCount(7)
        self.add_from_db_to_table()

    def add_from_db_to_table(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        i = 0
        for el in cur.execute("SELECT * FROM coffee").fetchall():
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(el[j])))
            i += 1
        con.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    yc = CoffeeWidjet()
    yc.show()
    sys.exit(app.exec())
