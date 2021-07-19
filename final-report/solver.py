class Giai(object):
    du_lieu = None
    __loi_giai = []

    def nhap_du_lieu(self, du_lieu):
        self.du_lieu = du_lieu

    def bai_toan(self, dang_bai_toan):
        phuong_phap = getattr(self, dang_bai_toan, lambda: None)
        if not phuong_phap():
            self.__loi_giai.append("Không xác định được bài toán.")
        else:
            return phuong_phap()

    def xuat_ket_qua(self):
        for step in self.__loi_giai:
            print(step)
        return

    def kiem_tra_thtt(self):
        return [False, ""]

    def kiem_tra_dltt(self):
        return [False, ""]

    def kiem_tra_co_so(self):
        return [False, ""]

    def tim_co_so(self):
        return [False, ""]
