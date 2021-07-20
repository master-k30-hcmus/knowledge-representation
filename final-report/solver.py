import numpy as np
import constants


class BaiToan(object):
    __loi_giai = []

    def __init__(self, dang_bai_toan, du_lieu):
        if not du_lieu:
            print("Thiếu dữ liệu")
            return

        self.du_lieu = du_lieu
        self.dang_bai_toan = dang_bai_toan

    def giai(self):
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

    def xuat_ket_qua(self):
        for step in self.__loi_giai:
            print(step)
        return

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
