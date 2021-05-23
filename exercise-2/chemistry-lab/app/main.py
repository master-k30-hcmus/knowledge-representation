import sys
from time import sleep

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (
    QApplication, QMessageBox, QMainWindow, QFileDialog, qApp
)
from PyQt5.QtCore import QDir

from lab import preprocess_input, process, get_data_from_file


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setupUi(self)
        loadUi('D:/master-k30-hcmus/knowledge-representation/exercise-2/chemistry-lab/app/ui/app.ui', self)

        self.file_path = ""
        # Chemistry input

        # Equations input
        self.btnBrowseFile.clicked.connect(self.get_file)
        self.btnClear.clicked.connect(self.init_equation_group)

        # Lab process
        self.btnProcessLab.clicked.connect(self.process_lab)

        # Menu bar handle
        self.actionNew.triggered.connect(self.init_states)
        self.actionAuthorInfo.triggered.connect(self.info_authors)
        self.actionLabInfo.triggered.connect(self.info_lab)
        self.actionExit.triggered.connect(qApp.quit)

    def info_authors(self):
        QMessageBox.about(self, "Nhóm 07", "Phan Thị Thùy An - 20C29002\n"
                                           "Định Thị Nữ - 20C29013\n"
                                           "Lý Phi Long - 20C29028\n"
                                           "Đặng Khánh Thi - 20C29038")

    def info_lab(self):
        QMessageBox.about(self, "Chemistry Lab", "Một chương trình demo các tri thức về điều chế chất hóa học trong "
                                                 "môn học Biểu diễn Tri thức.")

    def get_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Single File', QDir.rootPath(), '*.txt')
        self.file_path = file_path

        filename = file_path[file_path.rfind('/') + 1:]
        self.txtFilename.setText(f"{filename}")

        file = open(file_path, "r")
        file.seek(0)
        self.txtEquationList.setPlainText(file.read())
        self.txtEquationList.setReadOnly(True)  # prevent editing

        file.seek(0)
        num_equations = len(file.readlines())
        self.txtEquationListStatus.setText(f"Bao gồm {num_equations} phương trình.")

        file.close()

    def init_equation_group(self):
        self.file_path = ""
        self.txtFilename.setText("")

        self.txtEquationList.setPlainText("")
        self.txtEquationList.setReadOnly(False)

        self.txtEquationListStatus.setText("")

    def init_states(self):
        self.txtGivenChemistry.setText("")
        self.txtUnknownChemistry.setText("")

        self.init_equation_group()

        self.txtProduceSteps.setPlainText("")
        self.txtLabStatus.setText("")

    def set_produce_steps_text(self, text: str):
        self.txtProduceSteps.setPlainText(text)

    def valid_input(self) -> bool:
        if self.txtGivenChemistry.text() and self.txtUnknownChemistry.text() and self.txtEquationList.toPlainText():
            return True
        return False

    def set_lab_status(self, text, status=None):
        self.txtLabStatus.setText(text)
        if not status:
            self.txtLabStatus.setStyleSheet('color: black')
        elif status == 'error':
            self.txtLabStatus.setStyleSheet('color: red')
        elif status == 'processing':
            self.txtLabStatus.setStyleSheet('color: blue')
        elif status == 'done':
            self.txtLabStatus.setStyleSheet('color: green')

    def process_lab(self):
        given = preprocess_input(self.txtGivenChemistry.text())
        unknown = preprocess_input(self.txtUnknownChemistry.text())

        data = get_data_from_file(self.file_path)

        if not self.valid_input():
            self.set_lab_status(text='Thiếu dữ liệu cần thiết', status='error')
            return

        self.set_lab_status(text='Đang xử lý', status='processing')
        solutions = process(given, unknown, data)

        txt_shown = ""
        for i, solution in enumerate(solutions):
            txt_shown += f"Ta cần điều chế {unknown[i]}\n"
            print(solution)
            if solution[0]:
                for index, step in enumerate(solution[1]):
                    print(index, step)
                    txt_shown += f"\nĐiều chế lần {index + 1}\n"
                    txt_shown += f"Ta điều chế được {step[1].vars_VP} thông qua {step[1].name}\n"
                    txt_shown += f"{step[1].vars_VT} => {step[1].vars_VP}\n"

                    self.set_produce_steps_text(txt_shown)
            else:
                self.set_produce_steps_text(solution[1])

        self.set_lab_status(text='Hoàn thành', status='done')
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())