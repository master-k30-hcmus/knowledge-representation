import numpy as np
import constants
import data
import sys


class BaiToan(object):
    du_lieu = None
    __loi_giai = []
    __error = []

    def __init__(self, de_bai=None):
        if de_bai:
            [dang, du_lieu] = self.phan_tich(de_bai)
            self.dang_bai_toan = dang
            self.du_lieu = du_lieu

    def nhap_du_lieu(self, du_lieu):
        self.du_lieu = du_lieu

    def phan_tich(self, de_bai):
        dang = "kiem_tra_co_so"
        du_lieu = data.kiem_tra_co_so["d"]
        return [dang, du_lieu]

    def giai(self):
        if not self.du_lieu:
            print("Thiếu dữ liệu")
            return

        if self.dang_bai_toan == constants.KIEM_TRA_THTT:
            self.kiem_tra_thtt()
        elif self.dang_bai_toan == constants.KIEM_TRA_DLTT:
            self.kiem_tra_dltt()
        elif self.dang_bai_toan == constants.KIEM_TRA_CO_SO:
            self.__kiem_tra_du_lieu__(["name", "given", "dimR"])
            if not self.__error:
                self.kiem_tra_co_so()
        elif self.dang_bai_toan == constants.TIM_CO_SO:
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
        return False

    def kiem_tra_dltt(self):
        return False

    def kiem_tra_co_so(self):
        ket_qua = False

        ten_tap_hop = self.du_lieu["name"]
        matranA = self.du_lieu["given"]
        dimR = self.du_lieu["dimR"]

        self.__buoc_giai__(f'\nBước 1: Xây dựng ma trận từ tập hợp vector {ten_tap_hop}')
        self.__buoc_giai__(f'\tĐặt ma trận A = {matranA}')
        self.__buoc_giai__(
            f'\tTa có dimA = {len(matranA)}{f" không bằng dimR = {dimR}" if len(matranA) != dimR else ""}')

        if len(matranA) == dimR:
            self.__buoc_giai__(f'\nBước 2: Tiến hành kiểm tra tính độc lập tuyến tính của tập hợp vector {ten_tap_hop}')

            detA = self.tinh_det(matranA)
            self.__buoc_giai__(f'\tTính được detA = {detA}{"" if detA == 0.0 else " != 0"}')

            # dltt = self.kiem_tra_dltt()
            dltt = True if detA != 0 else False
            self.__buoc_giai__(f'\tSuy ra {ten_tap_hop}{"" if dltt else " không"} độc lập tuyến tính')
            if dltt:
                ket_qua = True

        self.__buoc_giai__(f'\nKết luận: {ten_tap_hop}{"" if ket_qua else " không"} là cơ sở của R{dimR}')

        return ket_qua

    def tim_co_so(self):
        return [False, ""]

    def tinh_det(self, matrix):
        det = np.linalg.det(np.array(matrix))
        try:
            det = int(det)
        except Exception as e:
            print(e)
        finally:
            return det

    def __kiem_tra_du_lieu__(self, req_fields):
        for field in req_fields:
            if field not in self.du_lieu:
                self.__error.append(f"- Thiếu dữ kiện {field}")

    def __buoc_giai__(self, step):
        self.__loi_giai.append(step)
