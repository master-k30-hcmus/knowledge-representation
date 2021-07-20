import numpy as np
import constants
import data


class BaiToan(object):
    du_lieu = None
    __loi_giai = []

    def __init__(self, de_bai=None):
        if de_bai:
            [dang, du_lieu] = self.phan_tich(de_bai)
            self.dang_bai_toan = dang
            self.du_lieu = du_lieu


    def nhap_du_lieu(self, du_lieu):
        self.du_lieu = du_lieu

    def phan_tich(self, de_bai):
        dang = "kiem_tra_co_so"
        # dang = "a"
        du_lieu = data.kiem_tra_co_so["a"]["given"]
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
        print("\nLời giải:")
        for step in self.__loi_giai:
            print(step)

    def kiem_tra_thtt(self):
        return [False, ""]

    def kiem_tra_dltt(self):
        return [False, ""]

    def kiem_tra_co_so(self):
        self.__buoc_giai__("Đặt ma trận A")

        return [False, ""]

    def tim_co_so(self):
        return [False, ""]

    def __buoc_giai__(self, step):
        self.__loi_giai.append(step)
