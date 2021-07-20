import unittest
import solver
from data import kiem_tra_co_so, kiem_tra_thtt, kiem_tra_dltt, tim_co_so

bai_toan = solver.BaiToan()


class TestToHopTuyenTinh(unittest.TestCase):

    def test_valid(self):
        bai_toan.nhap_du_lieu(kiem_tra_thtt["a"])
        result = bai_toan.kiem_tra_thtt()
        self.assertEqual(result[0], True, "Should be True")

    def test_nghiem_duy_nhat(self):
        bai_toan.nhap_du_lieu(kiem_tra_thtt["b"])
        result = bai_toan.kiem_tra_thtt()
        self.assertEqual(result[0], True, "Should be True")

    def test_vo_nghiem(self):
        bai_toan.nhap_du_lieu(kiem_tra_thtt["c"])
        result = bai_toan.kiem_tra_thtt()
        self.assertEqual(result[0], False, "Should be False")

    def test_vo_so_nghiem(self):
        bai_toan.nhap_du_lieu(kiem_tra_thtt["d"])
        result = bai_toan.kiem_tra_thtt()
        self.assertEqual(result[0], False, "Should be False")

    def test_doc_lap_tuyen_tinh(self):
        bai_toan.nhap_du_lieu(kiem_tra_dltt["a"])
        result = bai_toan.kiem_tra_thtt()
        self.assertEqual(result[0], True, "Should be True")

    def test_phu_thuoc_tuyen_tinh(self):
        bai_toan.nhap_du_lieu(kiem_tra_dltt["b"])
        result_1 = bai_toan.kiem_tra_thtt()
        self.assertEqual(result_1[0], False, "Should be False")

        bai_toan.nhap_du_lieu(kiem_tra_dltt["c"])
        result_2 = bai_toan.kiem_tra_thtt()
        self.assertEqual(result_2[0], False, "Should be False")


class TestKhongGianVector(unittest.TestCase):
    def test_valid(self):
        bai_toan.nhap_du_lieu(kiem_tra_co_so["c"])
        result = bai_toan.kiem_tra_co_so()
        self.assertEqual(result[0], True,
                         "Should be True as detA=3 => B3 độc lập tuyến tính và dimB3=3 = dimR^3=3")

    def test_khac_so_chieu(self):
        bai_toan.nhap_du_lieu(kiem_tra_co_so["a"])
        result_1 = bai_toan.kiem_tra_co_so()
        self.assertEqual(result_1[0], False, "Should be False as dimB1=2 != dimR^3=3")

        bai_toan.nhap_du_lieu(kiem_tra_co_so["b"])
        result_2 = bai_toan.kiem_tra_co_so()
        self.assertEqual(result_2[0], False, "Should be False as dimB2=4 != dimR^3=3")

    def test_khong_phai_thtt(self):
        bai_toan.nhap_du_lieu(kiem_tra_co_so["d"])
        result = bai_toan.kiem_tra_co_so()
        self.assertEqual(result[0], False, "Should be False as detA=0 => B4 không độc lập tuyến tính")

    def test_tim_theo_chieu(self):
        bai_toan.nhap_du_lieu(tim_co_so["a"])
        result = bai_toan.tim_co_so()
        self.assertEqual(result[0], True, "Should be True")

    def test_tim_theo_hang(self):
        bai_toan.nhap_du_lieu(tim_co_so["b"])
        result = bai_toan.tim_co_so()
        self.assertEqual(result[0], True, "Should be True")


if __name__ == '__main__':
    unittest.main()
