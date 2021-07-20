import argparse
import solver


def usage():
    return """
        python main.py "đề bài"
    """


def phan_tich(bai_toan):
    dang = "dang"
    du_lieu = ["du_lieu"]
    return [dang, du_lieu]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Hệ thống giải bài tập vector", usage=usage())
    parser.add_argument(
        "de_bai", help="nhập đề bài cần giải trong dấu \" \" "
    )
    args = parser.parse_args()

    de_bai = args.de_bai
    print("Đề bài:", de_bai)

    print("\nPhân tích bài toán:")
    [dang, du_lieu] = phan_tich(de_bai)
    print("- Dạng bài:", dang)
    print("- Dữ liệu:", du_lieu)

    print("\nLời giải:")
    bai_toan = solver.BaiToan()
    bai_toan.nhap_du_lieu(du_lieu)
    bai_toan.giai(dang)
    bai_toan.xuat_ket_qua()
