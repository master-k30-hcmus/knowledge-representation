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

    def ma_tran_bac_thang(self, matrix, steps=None, free_coef=None):
        if not matrix:
            return

        if steps is None:
            steps = []

        lead = 0
        row_count = matrix.shape[0]
        col_count = matrix.shape[1]
        for r in range(row_count):
            if lead >= col_count:
                return matrix
            i = r
            while matrix[i, lead] == 0:
                i += 1
                if i == row_count:
                    i = r
                    lead += 1
                    if col_count == lead:
                        return matrix

            matrix[i, :], matrix[r, :] = matrix[r, :], matrix[i, :]
            # Phân tử nhân
            lv = matrix[r, lead]
            matrix[r, :] = matrix[r, :] / lv

            steps.append(f'\nLần lượt thực hiện phép biến đổi sơ cấp trên các dòng sau:')
            if lv != 1:
                steps.append(f'  - dòng_{r + 1} = dòng_{r + 1}/({lv})')
            for i in range(row_count):
                if i != r:
                    lv = matrix[i, lead]
                    matrix[i, :] = matrix[i, :] - lv * matrix[r, :]
                    steps.append(f'  - dòng_{i + 1} = dòng_{i + 1} - ({lv})*dòng_{r + 1}')
            lead += 1
            steps.append(self.print_ma_tran(matrix.tolist(), prefix='\t', split_at=free_coef))
        return matrix

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
