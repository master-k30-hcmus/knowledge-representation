from sympy import Matrix, init_printing
import numpy as np

init_printing(use_unicode=True)


def ToReducedRowEchelonForm(M):
    if not M: return
    lead = 0
    rowCount = M.shape[0]
    columnCount = M.shape[1]
    for r in range(rowCount):
        if lead >= columnCount:
            return M
        i = r
        while M[i, lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return M

        M[i, :], M[r, :] = M[r, :], M[i, :]
        # Phân tử nhân
        lv = M[r, lead]
        M[r, :] = M[r, :] / lv
        # M[r] = [ mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i, lead]
                M[i, :] = M[i, :] - lv * M[r, :]
                # M[i] = [iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1

        # print("======")
        print(M)
    return M


def determineCombineLinear(tagert, choice):
    '''
    Input tagert 2-D Array
          choice 2-D Array
    Return
    '''
    # Buoc 1
    matrix = np.append(choice, tagert, axis=0)
    matrix_eq = Matrix(matrix.T)
    print(matrix_eq)

    # Buoc 2
    Echelon_matrix = ToReducedRowEchelonForm(matrix_eq)
    print(Echelon_matrix)

    # Buoc 3
    for row in range(Echelon_matrix.shape[0]):
        sum_row = sum(np.array(Echelon_matrix[row, :choice.shape[0]]).squeeze())
        if (sum_row == 0 and Echelon_matrix[row, -1] != 0):
            return False
    print("Tổ hợp tuyến tính")
    return True


def dltt(setVector):
    # Buoc 1
    matrix = Matrix(setVector)
    print(matrix)

    # Buoc 2
    Echelon_matrix = ToReducedRowEchelonForm(matrix)
    print(Echelon_matrix)

    # Buoc 3
    tmp = 0
    for row in range(Echelon_matrix.shape[0]):
        sum_row = sum(np.array(Echelon_matrix[row, :]).squeeze())
        if (sum_row == 0):
            tmp += 1

        rank = matrix.shape[0] - tmp
    if rank < matrix.shape[0]:
        print("Phụ thuộc tuyến tính")
    else:
        print("Độc lập tuyến tính")


###########Test#########################
tar = np.array([[1, 4, -3]])
choice = np.array([[2, 1, 1], [-1, 1, -1], [1, 1, -2]])
determineCombineLinear(tar, choice)

print("=======")
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dltt(arr2)
