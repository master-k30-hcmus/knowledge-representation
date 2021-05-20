import sys
from time import sleep

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow
)

from lab import process

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setupUi(self)
        loadUi('D:/master-k30-hcmus/knowledge-representation/exercise-2/chemistry-lab/app/ui/app.ui', self)


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
        return mytext

    def set_produce_steps_text(self, text: str):
        self.txtProduceSteps.setPlainText(text)

    def process_lab(self):
        self.get_text()
        solutions = process()

        unKnownChemistry = ['NaOH']

        txt_shown = ""
        for i, solution in enumerate(solutions):
            txt_shown += f"Ta cần điều chế {unKnownChemistry[i]}\n"
            for index, step in enumerate(solution):
                txt_shown += f"\nĐiều chế lần {index + 1}\n"
                txt_shown += f"Ta điều chế được {step[1].vars_VP} thông qua {step[1].name}\n"
                txt_shown += f"{step[1].vars_VT} => {step[1].vars_VP}\n"

                self.set_produce_steps_text(txt_shown)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
