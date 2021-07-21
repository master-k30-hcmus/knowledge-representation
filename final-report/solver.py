import numpy as np
from sympy import Matrix, init_printing

import constants
from analyzer import PhanTich
from matrix import MatrixUtils

init_printing(use_unicode=True)


class BaiToan(object):
    du_lieu = None
    __loi_giai = []
    __error = []

    def __init__(self, de_bai=None):
        self.matrix_utils = MatrixUtils()
        if de_bai:
            [dang, du_lieu] = self.phan_tich(de_bai)
            self.dang_bai_toan = dang
            self.du_lieu = du_lieu

    def nhap_du_lieu(self, du_lieu):
        self.du_lieu = du_lieu

    def phan_tich(self, de_bai):
        parser = PhanTich(de_bai)
        key = parser.type_problem()
        return parser.parse_data(key)

    def giai(self):
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
        print("- Dữ liệu:", self.__in_du_lieu__())

    def xuat_ket_qua(self, last_only=False):
        if not self.__error:
            print("\nLời giải:")
            if not last_only:
                for step in self.__loi_giai:
                    print(step)
            else:
                print(self.__loi_giai[-1:])
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
        self.__buoc_giai__(self.matrix_utils.print_ma_tran(matrix_eq.tolist(), prefix='\t', split_at=he_so_tu_do))

        self.__buoc_giai__(f'\nBước 2: Biến đổi về ma trận bậc thang sử dụng biến đổi sơ cấp trên dòng')
        steps = []
        echelon_matrix = self.matrix_utils.ma_tran_bac_thang(matrix_eq, steps, free_coef=he_so_tu_do)
        for step in steps:
            self.__buoc_giai__(step)

        for row in range(echelon_matrix.shape[0]):
            sum_row = sum(np.array(echelon_matrix[row, :given.shape[0]]).squeeze())
            if sum_row == 0 and echelon_matrix[row, -1] != 0:
                self.__buoc_giai__(f'\tHệ phương trình vô nghiệm')
                ket_qua = False

        self.__buoc_giai__(f'\nKết luận: u{"" if ket_qua else " không"} là tổ hợp tuyến tính của các vector đã cho.')
        return ket_qua

    def kiem_tra_dltt(self):
        ket_qua = True
        given = np.array(self.du_lieu["given"])

        self.__buoc_giai__(f'\nBước 1: Ma trận hóa')
        matrix = Matrix(given)
        self.__buoc_giai__(self.matrix_utils.print_ma_tran(matrix.tolist(), prefix='\t'))

        self.__buoc_giai__(f'\nBước 2: Biến đổi về ma trận bậc thang')
        steps = []
        echelon_matrix = self.matrix_utils.ma_tran_bac_thang(matrix, steps)
        for step in steps:
            self.__buoc_giai__(step)

        self.__buoc_giai__(f'\nBước 3: Xác định hạng của ma trận')
        rank = self.matrix_utils.tinh_hang(echelon_matrix)
        self.__buoc_giai__(f'\trank(A) = {rank} {"=" if rank == len(given) else "<"} số vector')
        if rank < matrix.shape[0]:
            ket_qua = False

        self.__buoc_giai__(
            f'\nKết luận: tập vector đã cho {"độc lập tuyến tính" if ket_qua else "phụ thuộc tuyến tính"}.')
        return ket_qua

    def kiem_tra_co_so(self):
        ket_qua = False

        ten_tap_hop = self.du_lieu["name"] if "name" in self.du_lieu else "tập hợp vector đã cho"
        given = np.array(self.du_lieu["given"])
        dimR = self.du_lieu["dimR"]

        self.__buoc_giai__(f'\nBước 1: Lập ma trận A từ {ten_tap_hop}')
        matrix = Matrix(given)
        self.__buoc_giai__(self.matrix_utils.print_ma_tran(matrix.tolist(), prefix='\t'))
        self.__buoc_giai__(
            f'\n  Ta có dimA = {len(given)}{f" không bằng dimR = {dimR}" if len(given) != dimR else ""}')

        if len(given) == dimR:
            self.__buoc_giai__(f'\nBước 2: Tiến hành kiểm tra tính độc lập tuyến tính của {ten_tap_hop}')
            detA = self.matrix_utils.tinh_det(given)
            self.__buoc_giai__(f'\tTính được detA = {detA}{"" if detA == 0.0 else " != 0"}')

            dltt = self.kiem_tra_dltt()
            self.__buoc_giai__(f'\tSuy ra {ten_tap_hop}{"" if dltt else " không"} độc lập tuyến tính')
            if dltt:
                ket_qua = True

        self.__buoc_giai__(f'\nKết luận: {ten_tap_hop}{"" if ket_qua else " không"} là cơ sở của R^{dimR}.')
        return ket_qua

    def tim_co_so(self):
        given = np.array(self.du_lieu["given"])

        self.__buoc_giai__(f'\nBước 1: Lập ma trận A')
        matrix = Matrix(given)
        self.__buoc_giai__(self.matrix_utils.print_ma_tran(matrix.tolist(), prefix='\t'))

        self.__buoc_giai__(f'\nBước 2: Biến đổi về ma trận bậc thang')
        steps = []
        echelon_matrix = self.matrix_utils.ma_tran_bac_thang(matrix, steps)
        for step in steps:
            self.__buoc_giai__(step)

        tap_co_so = []
        for row in range(echelon_matrix.shape[0]):
            sum_row = sum(np.array(echelon_matrix[row, :]).squeeze())
            if sum_row != 0:
                tap_co_so.append(echelon_matrix[row, :].tolist()[0])
        self.__buoc_giai__(f'\nKết luận: {tap_co_so} là một cơ sở của W.')
        return tap_co_so

    def __kiem_tra_du_lieu__(self, req_fields):
        for field in req_fields:
            if field not in self.du_lieu:
                self.__error.append(f"- Thiếu dữ kiện {field}")

    def __buoc_giai__(self, step):
        self.__loi_giai.append(step)

    def __in_du_lieu__(self):
        output_str = ""
        vector_str = ""
        if "dimR" in self.du_lieu:
            output_str += f'\n\tKhông gian R^{self.du_lieu["dimR"]}'
        for v in self.du_lieu["given"]:
            vector_str += f"{tuple(v)}, "
        output_str += "\n\tCác vectors: " + vector_str[:-2]
        return output_str
