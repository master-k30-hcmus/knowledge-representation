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

    bai_toan = args.de_bai
    print("Đề bài:", bai_toan)

    print("\nPhân tích bài toán:")
    [dang, du_lieu] = phan_tich(bai_toan)
    print("- Dạng bài:", dang)
    print("- Dữ liệu:", du_lieu)

    print("\nLời giải:")
    giai = solver.Giai()
    giai.nhap_du_lieu(du_lieu)
    giai.bai_toan(dang)
    giai.xuat_ket_qua()
