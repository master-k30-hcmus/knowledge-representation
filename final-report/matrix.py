import numpy as np


class MatrixUtils(object):
    @staticmethod
    def print_ma_tran(matrix, prefix='', split_at=None):
        matrix_str = ''
        for row in matrix:
            matrix_str += f'\n{prefix}'
            matrix_str += '\t'.join([str(cell) for cell in row[:split_at]])
            if split_at and row[split_at:]:
                matrix_str += f'\t|\t{str(row[split_at:][0])}'
        return matrix_str

    @staticmethod
    def ma_tran_bac_thang(matrix):
        if not matrix:
            return

        steps = []

        lead = 0
        row_count = matrix.shape[0]
        col_count = matrix.shape[1]
        for r in range(row_count):
            if lead >= col_count:
                return [matrix, steps]
            i = r
            while matrix[i, lead] == 0:
                i += 1
                if i == row_count:
                    i = r
                    lead += 1
                    if col_count == lead:
                        return [matrix, steps]

            matrix[i, :], matrix[r, :] = matrix[r, :], matrix[i, :]
            # Phân tử nhân
            lv = matrix[r, lead]
            matrix[r, :] = matrix[r, :] / lv
            for i in range(row_count):
                if i != r:
                    lv = matrix[i, lead]
                    matrix[i, :] = matrix[i, :] - lv * matrix[r, :]
            lead += 1
            steps.append(matrix)
        return [matrix, steps]

    @staticmethod
    def tinh_hang(matrix):
        rank = matrix.shape[0]
        for row in range(matrix.shape[0]):
            row_squeezed = np.array(matrix[row, :]).squeeze()
            if (row_squeezed == 0).all():
                rank -= 1
        return rank

    @staticmethod
    def tinh_det(matrix):
        det = np.linalg.det(np.array(matrix))
        try:
            det = int(det)
        except Exception as e:
            print(e)
        finally:
            return det
