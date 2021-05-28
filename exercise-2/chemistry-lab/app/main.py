import sys
from os import getcwd

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog, qApp
from PyQt5.QtCore import QDir

from lab import preprocess_input, process, get_data


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi(f'{getcwd()}/app/ui/app.ui', self)
        self.file_path = ""

        # Equations input
        self.btnBrowseFile.clicked.connect(self.get_file)
        self.btnClear.clicked.connect(self.clear_equation_group)

        # Lab process
        self.btnProcessLab.clicked.connect(self.process_lab)

        # Menu bar handle
        self.actionNew.triggered.connect(self.clear_all_groups)
        self.actionAuthorInfo.triggered.connect(self.info_authors)
        self.actionLabInfo.triggered.connect(self.info_lab)
        self.actionExit.triggered.connect(qApp.quit)

    def info_authors(self):
        QMessageBox.about(self, "Nhóm 07", "Phan Thị Thùy An - 20C29002\n"
                                           "Đinh Thị Nữ - 20C29013\n"
                                           "Lý Phi Long - 20C29028\n"
                                           "Đặng Khánh Thi - 20C29038")

    def info_lab(self):
        QMessageBox.about(self, "Chemistry Lab", "Một chương trình demo các tri thức về điều chế các chất hóa học trong "
                                                 "môn học Biểu diễn Tri thức sử dụng mạng ngữ nghĩa.")

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

    def clear_equation_group(self):
        self.file_path = ""
        self.txtFilename.setText("")

        self.txtEquationList.setPlainText("")
        self.txtEquationList.setReadOnly(False)

        self.txtEquationListStatus.setText("")
        
    def clear_steps_group(self):
        self.txtProduceSteps.setPlainText("")
        self.txtLabStatus.setText("")

    def clear_all_groups(self):
        self.txtGivenChemistry.setText("")
        self.txtUnknownChemistry.setText("")

        self.clear_equation_group()
        self.clear_steps_group()

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

        if not self.valid_input():
            self.set_lab_status(text='Thiếu dữ liệu cần thiết', status='error')
            return

        self.clear_steps_group()

        if self.file_path:
            data = get_data(file_path=self.file_path)
        else:
            texts = self.txtEquationList.toPlainText().split(sep='\n')
            data = get_data(text_list=texts)
            self.txtEquationListStatus.setText(f"Đã nhập {len(texts)} phương trình.")

        self.set_lab_status(text='Đang xử lý', status='processing')
        solutions = process(given, unknown, data)

        txt_shown = ""
        for i, solution in enumerate(solutions):
            txt_shown += f"Ta cần điều chế {unknown[i]}\n"
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
