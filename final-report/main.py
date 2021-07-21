import argparse
import solver
import utils


def usage():
    return """
        python main.py "đề bài"
    """


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Hệ thống giải bài tập vector", usage=usage())
    parser.add_argument(
        "de_bai", help="nhập đề bài cần giải trong dấu \"\" "
    )
    args = parser.parse_args()

    de_bai = args.de_bai
    utils.print_box_wrapper([f"Đề bài: {de_bai}"])

    bai_toan = solver.BaiToan(de_bai)
    bai_toan.giai()
    bai_toan.xuat_ket_qua()
    # bai_toan.xuat_ket_qua(last_only=True)
