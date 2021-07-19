import unittest
import solver
from data import kiem_tra_co_so, kiem_tra_thtt, kiem_tra_dltt, tim_co_so

giai = solver.Giai()


class TestToHopTuyenTinh(unittest.TestCase):

    def test_valid(self):
        giai.nhap_du_lieu(kiem_tra_thtt["a"])
        result = giai.kiem_tra_thtt()
        self.assertEqual(result[0], True, "Should be True")

    def test_nghiem_duy_nhat(self):
        giai.nhap_du_lieu(kiem_tra_thtt["b"])
        result = giai.kiem_tra_thtt()
        self.assertEqual(result[0], True, "Should be True")

    def test_vo_nghiem(self):
        giai.nhap_du_lieu(kiem_tra_thtt["c"])
        result = giai.kiem_tra_thtt()
        self.assertEqual(result[0], False, "Should be False")

    def test_vo_so_nghiem(self):
        giai.nhap_du_lieu(kiem_tra_thtt["d"])
        result = giai.kiem_tra_thtt()
        self.assertEqual(result[0], False, "Should be False")

    def test_doc_lap_tuyen_tinh(self):
        giai.nhap_du_lieu(kiem_tra_dltt["a"])
        result = giai.kiem_tra_thtt()
        self.assertEqual(result[0], True, "Should be True")

    def test_phu_thuoc_tuyen_tinh(self):
        giai.nhap_du_lieu(kiem_tra_dltt["b"])
        result = giai.kiem_tra_thtt()
        self.assertEqual(result[0], False, "Should be False")


class TestKhongGianVector(unittest.TestCase):
    def test_valid(self):
        giai.nhap_du_lieu(kiem_tra_co_so["c"])
        result = giai.kiem_tra_co_so()
        self.assertEqual(result[0], True,
                         "Should be True as detA=3 => B3 độc lập tuyến tính và dimB3=3 = dimR^3=3")

    def test_khac_so_chieu(self):
        giai.nhap_du_lieu(kiem_tra_co_so["a"])
        result_1 = giai.kiem_tra_co_so()
        self.assertEqual(result_1[0], False, "Should be False as dimB1=2 != dimR^3=3")

        giai.nhap_du_lieu(kiem_tra_co_so["b"])
        result_2 = giai.kiem_tra_co_so()
        self.assertEqual(result_2[0], False, "Should be False as dimB2=4 != dimR^3=3")

    def test_khong_phai_thtt(self):
        giai.nhap_du_lieu(kiem_tra_co_so["d"])
        result = giai.kiem_tra_co_so()
        self.assertEqual(result[0], False, "Should be False as detA=0 => B4 không độc lập tuyến tính")

    def test_tim_theo_chieu(self):
        giai.nhap_du_lieu(tim_co_so["a"])
        result = giai.tim_co_so()
        self.assertEqual(result[0], True, "Should be True")

    def test_tim_theo_hang(self):
        giai.nhap_du_lieu(tim_co_so["b"])
        result = giai.tim_co_so()
        self.assertEqual(result[0], True, "Should be True")


if __name__ == '__main__':
    unittest.main()
