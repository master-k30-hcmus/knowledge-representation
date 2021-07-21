import numpy as np
import constants
import data
from functools import reduce 
import re
import numpy as np

from sympy import Matrix, init_printing
init_printing(use_unicode=True)


class BaiToan(object):
    du_lieu = None
    __loi_giai = []
    __error = []

    def __init__(self, de_bai=None):
        if de_bai:
            [dang, du_lieu] = self.phan_tich(de_bai)
            self.dang_bai_toan = dang[0]
            self.du_lieu = du_lieu

    def nhap_du_lieu(self, du_lieu):
        self.du_lieu = du_lieu

    def phan_tich(self, de_bai):
        key = self.type_problem(de_bai)
        if (key[0] == "kiem_tra_thtt"):
            vector_space = self.extract_vector(de_bai)
            data = {'target': vector_space[0] , 'given': vector_space[1:]}
        elif (key[0] == "kiem_tra_dltt"):
            vector_space = self.extract_vector(de_bai)
            data = {'given': vector_space}
        elif (key[0] == "kiem_tra_co_so"):
            pattern = ''
            for i, char in enumerate(de_bai):
                if char in {'R', 'Real'}:
                    pattern += de_bai[i:i+4]
            de_bai = de_bai.replace(pattern,'');
            vector_space = self.extract_vector(de_bai)
            space = int(re.findall('([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)', pattern)[0])
            data = {"given": vector_space, "dimR": space}
        elif (key[0] == "tim_co_so"):
            vector_space = self.extract_vector(de_bai)
            data = {'given': vector_space}
        else:
            return False
        return [key, data]

    def giai(self):
        if not self.du_lieu:
            print("Thiếu dữ liệu")
            return

        if self.dang_bai_toan == constants.KIEM_TRA_THTT:
            self.__kiem_tra_du_lieu__(["target", "given"])
            if not self.__error:
                self.kiem_tra_thtt()
        elif self.dang_bai_toan == constants.KIEM_TRA_DLTT:
            self.__kiem_tra_du_lieu__(["given"])
            if not self.__error:
                self.kiem_tra_dltt()
        elif self.dang_bai_toan == constants.KIEM_TRA_CO_SO:
            self.__kiem_tra_du_lieu__(["given", "dimR"])
            if not self.__error:
                self.kiem_tra_co_so()
        elif self.dang_bai_toan == constants.TIM_CO_SO:
            self.__kiem_tra_du_lieu__(["given"])
            if not self.__error:
                self.tim_co_so()
        else:
            self.__buoc_giai__("Không xác định được dạng bài toán.")
            return

        print("\nPhân tích bài toán:")
        print("- Dạng bài toán:", constants.DANG_BAI_TOAN[self.dang_bai_toan])
        print("- Dữ liệu:", self.du_lieu)

    def xuat_ket_qua(self):
        if not self.__error:
            print("\nLời giải:")
            for step in self.__loi_giai:
                print(step)
        else:
            print("\nLỗi:")
            for err in self.__error:
                print(err)

    def kiem_tra_thtt(self):
        ket_qua = True

        given = np.array(self.du_lieu["given"])
        target = np.array([self.du_lieu["target"]])
        he_so_tu_do = len(given)

        self.__buoc_giai__(f'\nBước 1: Ma trận hóa')
        matrix = np.append(given, target, axis=0)
        matrix_eq = Matrix(matrix.T)
        self.__buoc_giai__(self.print_ma_tran(matrix_eq.tolist(), prefix='\t', split_at=he_so_tu_do))

        self.__buoc_giai__(f'\nBước 2: Biến đổi về ma trận bậc thang sử dụng biến đổi sơ cấp trên dòng')
        echelon_matrix = self.ma_tran_bac_thang(matrix_eq)
        self.__buoc_giai__(self.print_ma_tran(echelon_matrix.tolist(), prefix='\t', split_at=he_so_tu_do))

        for row in range(echelon_matrix.shape[0]):
            sum_row = sum(np.array(echelon_matrix[row, :given.shape[0]]).squeeze())
            if sum_row == 0 and echelon_matrix[row, -1] != 0:
                self.__buoc_giai__(f'\tHệ phương trình vô nghiệm')
                ket_qua = False

        self.__buoc_giai__(f'\nKết luận: u{"" if ket_qua else " không"} là tổ hợp tuyến tính của các vector đã cho')
        return ket_qua

    def kiem_tra_dltt(self):
        ket_qua = True
        given = np.array(self.du_lieu["given"])

        self.__buoc_giai__(f'\nBước 1: Ma trận hóa')
        matrix = Matrix(given)
        self.__buoc_giai__(self.print_ma_tran(matrix.tolist(), prefix='\t'))

        self.__buoc_giai__(f'\nBước 2: Biến đổi về ma trận bậc thang')
        echelon_matrix = self.ma_tran_bac_thang(matrix)
        self.__buoc_giai__(self.print_ma_tran(echelon_matrix.tolist(), prefix='\t'))

        self.__buoc_giai__(f'\nBước 3: Xác định hạng của ma trận')
        rank = self.tinh_hang(echelon_matrix)
        self.__buoc_giai__(f'\trank(A) = {rank} {"=" if rank == len(given) else "<"} số vector')
        if rank < matrix.shape[0]:
            ket_qua = False

        self.__buoc_giai__(
            f'\nKết luận: tập vector đã cho {"độc lập tuyến tính" if ket_qua else "phụ thuộc tuyến tính"}')
        return ket_qua

    def kiem_tra_co_so(self):
        ket_qua = False

        ten_tap_hop = self.du_lieu["name"] if "name" in self.du_lieu else "tập hợp vector đã cho"
        given = np.array(self.du_lieu["given"])
        dimR = self.du_lieu["dimR"]

        self.__buoc_giai__(f'\nBước 1: Lập ma trận A từ {ten_tap_hop}')
        matrix = Matrix(given)
        self.__buoc_giai__(self.print_ma_tran(matrix.tolist(), prefix='\t'))
        self.__buoc_giai__(
            f'\tTa có dimA = {len(given)}{f" không bằng dimR = {dimR}" if len(given) != dimR else ""}')

        if len(given) == dimR:
            self.__buoc_giai__(f'\nBước 2: Tiến hành kiểm tra tính độc lập tuyến tính của {ten_tap_hop}')
            detA = self.tinh_det(given)
            self.__buoc_giai__(f'\tTính được detA = {detA}{"" if detA == 0.0 else " != 0"}')

            dltt = self.kiem_tra_dltt()
            self.__buoc_giai__(f'\tSuy ra {ten_tap_hop}{"" if dltt else " không"} độc lập tuyến tính')
            if dltt:
                ket_qua = True

        self.__buoc_giai__(f'\nKết luận: {ten_tap_hop}{"" if ket_qua else " không"} là cơ sở của R{dimR}')
        return ket_qua

    def tim_co_so(self):
        given = np.array(self.du_lieu["given"])

        self.__buoc_giai__(f'\nBước 1: Lập ma trận A')
        matrix = Matrix(given)
        self.__buoc_giai__(self.print_ma_tran(matrix.tolist(), prefix='\t'))

        self.__buoc_giai__(f'\nBước 2: Biến đổi về ma trận bậc thang')
        echelon_matrix = self.ma_tran_bac_thang(matrix)
        self.__buoc_giai__(self.print_ma_tran(echelon_matrix.tolist(), prefix='\t'))

        tap_co_so = []
        for row in range(echelon_matrix.shape[0]):
            sum_row = sum(np.array(echelon_matrix[row, :]).squeeze())
            if sum_row != 0:
                tap_co_so.append(echelon_matrix[row, :].tolist()[0])
        self.__buoc_giai__(f'\nKết luận: {tap_co_so} là một cơ sở của W')
        return tap_co_so

    @staticmethod
    def tinh_det(matrix):
        det = np.linalg.det(np.array(matrix))
        try:
            det = int(det)
        except Exception as e:
            print(e)
        finally:
            return det

    @staticmethod
    def tinh_hang(matrix):
        rank = matrix.shape[0]
        for row in range(matrix.shape[0]):
            sum_row = sum(np.array(matrix[row, :]).squeeze())
            if sum_row == 0:
                rank -= 1
        return rank

    def ma_tran_bac_thang(self, matrix):
        if not matrix:
            return
        lead = 0
        row_count = matrix.shape[0]
        col_count = matrix.shape[1]
        for r in range(row_count):
            if lead >= col_count:
                return matrix
            i = r
            while matrix[i, lead] == 0:
                i += 1
                if i == row_count:
                    i = r
                    lead += 1
                    if col_count == lead:
                        return matrix

            matrix[i, :], matrix[r, :] = matrix[r, :], matrix[i, :]
            # Phân tử nhân
            lv = matrix[r, lead]
            matrix[r, :] = matrix[r, :] / lv
            for i in range(row_count):
                if i != r:
                    lv = matrix[i, lead]
                    matrix[i, :] = matrix[i, :] - lv * matrix[r, :]
            lead += 1
            self.__buoc_giai__(self.print_ma_tran(matrix.tolist(), prefix='\t'))
        return matrix

    def type_problem(self, de_bai):
        dang = []
        for pattern in constants.CONST_THTT:
            if (de_bai.find(pattern) != -1):
                dang.append("kiem_tra_thtt")
                return dang
        for pattern in constants.CONST_DLTT:
            if (de_bai.find(pattern) != -1):
                dang.append("kiem_tra_dltt")
                return dang
        for pattern in constants.CONST_KTCS:
            if (de_bai.find(pattern) != -1):
                dang.append("kiem_tra_co_so")
                return dang
        for pattern in constants.CONST_TCS:
            if (de_bai.find(pattern) != -1):
                dang.append("tim_co_so")
                return dang

    def extract_vector(self, de_bai):
        process1 = re.split("[a-zA-Z]([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)", de_bai)
        if len(process1) == 1:
            process1 = re.split('_([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)', process1[0])
        results = []
        if len(process1) == 1:
            x = re.findall('([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)', process1[0])
            results = x
        else:
            for process in process1:
                process2 = re.split("_([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)", process)
                for path in process2:
                    if (len(path) == 1 or path is None):
                        del path
                    else:
                        x = re.findall('([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)', path)
                        results.append(x)

        for result in results:
            if (len(result) == 0):
                results.remove(result)

        if type(results[0]) is not str:
            data = reduce(lambda a, b: a+b, results)
        else:
            data = results

        data = [int(string) for string in data]

        numEq = de_bai.count("(")
        data = np.array_split(data, numEq)
        return data

    def __kiem_tra_du_lieu__(self, req_fields):
        for field in req_fields:
            if field not in self.du_lieu:
                self.__error.append(f"- Thiếu dữ kiện {field}")

    def __buoc_giai__(self, step):
        self.__loi_giai.append(step)

    @staticmethod
    def print_ma_tran(matrix, prefix='', split_at=None):
        matrix_str = ''
        for row in matrix:
            matrix_str += f'\n{prefix}'
            matrix_str += '\t'.join([str(cell) for cell in row[:split_at]])
            if split_at and row[split_at:]:
                matrix_str += f'\t|\t{str(row[split_at:][0])}'
        return matrix_str
