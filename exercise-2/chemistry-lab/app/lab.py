# -*- coding: utf-8 -*-
"""BDTT - Bai2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NnLk_isWSmoCcncWlkf3oKH4Lues-Gku
"""

from re import sub, compile, IGNORECASE


class EQUATION:
    vars = []
    vars_VP = []
    vars_VT = []

    def __init__(self, name, vars_VT, vars_VP):
        self.name = name
        self.vars_VT = vars_VT
        self.vars_VP = vars_VP

    # Tổng số chất đang có bên vế trái
    def getNumVar(self):
        return len(self.vars_VT)


class STEP:
    var_value = -1
    equation = -1

    def __init__(self, var, equation):
        self.var_value = var
        self.equation = equation


class PROBLEM:
    equations = []  # lưu các tri thức (các phương trình)
    knownVar = []  # lưu các hóa chất đã biết
    unknownVar = -1  # hóa chất cần điều chế
    steps = []  # lưu các bước giải bài toán

    def clear(self):
        self.knownVar.clear()
        self.unknownVar.clear()
        self.steps.clear()
        self.unknownVar = -1

    # Cài đặt hóa chất nào đã biết
    def setUnknownVar(self, var):
        self.unknownVar = var

    # Cài đặt hóa chất nào chưa biết
    def setKnownVars(self, vars):
        self.knownVars = vars

    # Thêm tri thức (phương trình) vào bài toán
    def addEquation(self, equations):
        self.equations = equations

    # Số lượng hóa chất đã biết (chỉ tính bên vế trái phương trình)
    def getNumKnownVar(self, equation):
        count = 0
        for var in equation.vars_VT:
            # print(var)
            if (var in self.knownVars):
                count += 1
        return count

    # Trả về yếu tố chưa biết trong phương trình
    def getUnknownVar(self, equation):
        for var in equation.vars_VP:
            if (var not in self.knownVars):
                return var

    # Trả về các hóa chát có thể điều chế được, trả về kết quả điều chế
    def getKnownVar(self, equation):
        # print(self.getNumKnownVar(equation))
        if ((self.getNumKnownVar(equation) == equation.getNumVar())):
            return equation.vars_VP
        return -1

    # Kích hoạt hóa chất nào có thể điều chế
    def activeVar(self, knownVar):
        for var in knownVar:
            self.knownVars.append(var)
        # print(self.knownVars)

    # Thêm bước giải
    def addStep(self, var, equation):
        self.steps.append((var, equation))

    # Kiểm tra điều chế thành công chưa?
    def isSuccess(self):
        if (self.unknownVar in self.knownVars):
            return True
        return False

    # Giải bài toán
    def solve(self):
        flag = True
        while (flag):
            flag = False
            for equation in self.equations:
                knownVar = self.getKnownVar(equation)
                # print(knownVar)
                if (knownVar != -1):
                    self.activeVar(knownVar)
                    self.addStep(knownVar, equation)
                    flag = True
                    if (self.isSuccess()):
                        temp = []
                        solutions = temp
                        for step in self.steps:
                            solutions.append(step)
                        return [True, solutions]
        return [False, "Bài toán không thể giải, hãy bổ sung thêm thông tin hoặc tri thức."]


def get_data_from_file(file_path: str):
    file = open(file_path, "r")
    eq_list = []
    for line in file.readlines():
        temp = sub('\s+', '', line).split(sep="=")
        vars_VT = [sub("(^\d+)", "", var) for var in temp[0].split(sep="+")]
        vars_VP = [sub("(^\d+)", "", var) for var in temp[1].split(sep="+")]
        eq_list.append([vars_VT, vars_VP])
    file.close()
    return eq_list


def preprocess_input(text):
    return sub('\s+', '', text).split(",")


def process(given, unknown, data):
    eq_list = []
    for i, row in enumerate(data):
        print(row)
        eq = EQUATION("công thức " + str(i+1), row[0], row[1])
        eq_list.append(eq)

    problem = PROBLEM()

    problem.addEquation(eq_list)

    if "O_2" not in given:
        given.append('O_2')
    problem.setKnownVars(given)

    solutions = []
    for chemistry in unknown:
        problem.setUnknownVar(chemistry)
        solutions.append(problem.solve())

    return solutions