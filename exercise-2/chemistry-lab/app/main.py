import sys
from time import sleep

from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow
)

from PyQt5.uic import loadUi
import lab

# from ui.app_ui import Ui_MainWindow

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setupUi(self)
        loadUi('D:/master-k30-hcmus/knowledge-representation/exercise-2/chemistry-lab/app/ui/app.ui',self)


        # Chemistry input

        # Equations input

        # Lab process
        self.btnLab.clicked.connect(self.process_lab)

    def choose_input_file(self):
        return

    def clear_input(self):
        return

    def get_text(self):
        mytext = self.inputSourceChemistry.text()
        print(mytext)
        return

    def set_text(self):
        self.txtProduceSteps.setPlainText("hello world!")
        return

    def process_lab(self):
        self.get_text()
        sleep(4)
        self.set_text()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
