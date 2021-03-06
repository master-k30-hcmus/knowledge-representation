# -*- coding: utf-8 -*-
"""BDTT - Bai2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NnLk_isWSmoCcncWlkf3oKH4Lues-Gku
"""

from re import sub
from typing import List


class EQUATION:
    vars_VP = []
    vars_VT = []

    def __init__(self, name, vars_VT, vars_VP):
        self.name = name
        self.vars_VT = vars_VT
        self.vars_VP = vars_VP

    # Tổng số chất đang có bên vế trái
    def get_num_vars(self):
        return len(self.vars_VT)


class PROBLEM:
    equations = []  # lưu các tri thức (các phương trình)
    knownVar = []  # lưu các hóa chất đã biết
    unknownVar = -1  # hóa chất cần điều chế
    steps = []  # lưu các bước giải bài toán

    def clear(self):
        self.known_vars.clear()
        self.unknown_vars = None
        self.steps.clear()

    # Cài đặt hóa chất nào đã biết
    def set_unknown_var(self, vars):
        self.unknown_vars = vars

    # Cài đặt hóa chất nào chưa biết
    def set_known_vars(self, vars):
        self.known_vars = vars

    # Thêm tri thức (phương trình) vào bài toán
    def set_equation_list(self, equations):
        self.equations = equations

    # Số lượng hóa chất đã biết (chỉ tính bên vế trái phương trình)
    def get_num_known_vars(self, equation):
        count = 0
        for var in equation.vars_VT:
            if var in self.known_vars:
                count += 1
        return count

    # Trả về yếu tố chưa biết trong phương trình
    def get_unknown_vars(self, equation):
        for var in equation.vars_VP:
            if var not in self.known_vars:
                return var

    # Trả về các hóa chát có thể điều chế được, trả về kết quả điều chế
    def get_known_vars(self, equation):
        if self.get_num_known_vars(equation) == equation.get_num_vars():
            return equation.vars_VP
        return -1

    # Kích hoạt hóa chất nào có thể điều chế
    def active_var(self, known_var):
        for var in known_var:
            self.known_vars.append(var)

    # Thêm bước giải
    def add_step(self, var, equation):
        self.steps.append((var, equation))

    # Kiểm tra điều chế thành công chưa?
    def is_success(self):
        if self.unknown_vars in self.known_vars:
            return True
        return False

    # Giải bài toán
    def solve(self):
        #Cờ đề truy vết
        flag = True
        while flag:
            flag = False
            print('self.equations', len(self.equations))
            print('self.steps', len(self.steps))
            #Duyệt từng phương trình
            for equation in self.equations:
                #Lấy chất điều chế bên VT phương trình
                known_var = self.get_known_vars(equation)
                #Nếu như 1 node (chất) có thể điều chế được (khác -1)
                if known_var != -1:
                    #Kích hoạt node có thể điều chế được
                    self.active_var(known_var)
                    #Tiến thành lưu lại pt có thể điều chế
                    self.add_step(known_var, equation)
                    flag = True
                    # Kiểm tra xem đã giải bài toán thành công chưa?
                    if self.is_success():
                        temp = []
                        solutions = temp
                        # Trả về lời giải đến đích
                        for step in self.steps:
                            solutions.append(step)
                        return [True, solutions]
        # Nếu không giải được trả về yêu cầu thêm thông tin, tri thức
        return [False, "Bài toán không thể giải, hãy bổ sung thêm thông tin hoặc tri thức."]


def clean_equation(line):
    temp = sub('\s+', '', line).split(sep="=")
    if len(temp) == 2:
        vars_VT = [sub("(^\d+)", "", var) for var in temp[0].split(sep="+")]
        vars_VP = [sub("(^\d+)", "", var) for var in temp[1].split(sep="+")]
        return [vars_VT, vars_VP]
    return [[], []]


def get_equation_list(texts):
    eq_list = []
    for line in texts:
        eq_list.append(clean_equation(line))
    return eq_list


def get_data(file_path: str = None, text_list: List[str] = None):
    eq_list = []
    if file_path:
        file = open(file_path, "r")
        eq_list = get_equation_list(file.readlines())
        file.close()
    elif text_list:
        eq_list = get_equation_list(text_list)
    return eq_list


def preprocess_input(text):
    return sub('\s+', '', text).split(",")


def process(given, unknown, data):
    print("Equation list:")
    eq_list = []
    for i, row in enumerate(data):
        print(i, row)
        eq = EQUATION("công thức " + str(i+1), row[0], row[1])
        eq_list.append(eq)
    
    problem = PROBLEM()
    problem.set_equation_list(eq_list)

    if "O_2" not in given:
        given.append('O_2')
    problem.set_known_vars(given)

    print("Given chemistry:", given)
    print("Unknown chemistry:", unknown)

    print("Find solutions:")
    solutions = []
    for chemistry in unknown:
        print(f"for {chemistry}:")
        problem.set_unknown_var(chemistry)
        solved = problem.solve()
        solutions.append(solved)
        print(solved)
    problem.clear()

    return solutions
