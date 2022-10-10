import numpy as np


def creating_matrix(rows, columns):
    print("Enter row 1: ", end="")
    row = input()
    mat = np.zeros(int(columns))
    numbers = row.split(' ')
    for i in range(0, int(columns)):
        mat[i] = int(numbers[i])
    for i in range(1, int(rows)):
        print("Enter row {}: ".format(i + 1), end="")
        row = input()
        numbers = row.split(' ')
        new_row = np.zeros(int(columns))
        for j in range(0, int(columns)):
            new_row[j] = int(numbers[j])
        mat = np.vstack((mat, new_row))
    print("Enter constant values: ", end="")
    values = input()
    numbers = values.split(' ')
    values_array = np.zeros((int(rows), 1))
    for i in range(0, int(rows)):
        values_array[i][0] = int(numbers[i])
    mat = np.hstack((mat, values_array))
    # print(matrix)
    return mat


def finding_pivot_column(mat, column_number, row, pivot_number):
    not_zero = 0
    for i in range(int(pivot_number), int(row)):
        if mat[i][int(column_number)] != 0:
            not_zero += 1
    if not_zero > 0:
        return True
    else:
        return False


def find_row(mat, pivot_number, current_column, row):
    r = pivot_number
    while r < row:
        if mat[r][current_column] != 0:
            return r
        else:
            r += 1


def interchange(mat, columns, x, y, proper_number):
    for k in range(0, columns + 1):
        temp = matrix[x][k]
        matrix[x][k] = matrix[proper_number][k]
        matrix[proper_number][k] = temp
    return mat


def row_replacement(mat, column_number, row_number, row, column):
    for k in range(row_number + 1, row):
        # print(k)
        if mat[k][column_number] != 0:
            # print(mat[k][column_number])
            num = mat[k][column_number] / mat[row_number][column_number]
            # print("num")
            # print(num)
            for r in range(column_number, column + 1):
                # print("u")
                # print(mat[row_number][r])
                # print("d")
                # print(mat[k][r])
                mat[k][r] -= num * mat[row_number][r]
    return mat


def making_echelon_form(mat, pivot_matrix, row, column_number):
    for k in range(0, row):
        for q in range(0, int(pivot_matrix[k][0])):
            if mat[q][int(pivot_matrix[k][1])] != 0:
                # print(mat)
                # print(q, pivot_matrix[k][1], mat[q][int(pivot_matrix[k][1])])
                num = mat[q][int(pivot_matrix[k][1])] / mat[k][int(pivot_matrix[k][1])]
                # print(mat[k][int(pivot_matrix[k][1])])
                # print(num)
                for z in range(0, column_number + 1):
                    # print(mat[q][z])
                    # print(mat[k][z])
                    mat[q][z] -= num * mat[k][z]


def finding_free_variables(mat, pivot_matrix, row, coloumns):
    free_variables = []
    free_variable_num = 0
    for x in range(0, row):
        requested_row = int(pivot_matrix[x][0])
        requested_column = int(pivot_matrix[x][1])
        for y in range(0, coloumns):
            cnt = 0
            if mat[requested_row][y] != 0 and y != requested_column and mat[requested_row][coloumns] != 0:
                for z in range(0, free_variable_num):
                    if free_variables[z] == (y):
                        cnt += 1
                        break
                if cnt == 0:
                    free_variables.append(y)
                    free_variable_num += 1
    return free_variables


def print_result(mat, free_variables, columns, rows, pivot_matrix, pivot_row):
    p = 0
    # print(pivot_row)
    free_num = len(free_variables_list)
    for z in range(0, columns):
        if p < pivot_row and pivot_matrix[p][1] == z:
            r = int(pivot_matrix[p][0])
            c = int(pivot_matrix[p][1])
            print("x{} is ".format(z + 1), end="")
            if mat[r][c] != 1:
                print("{}*".format((1 / mat[r][c])), end="")
            print("({}".format(mat[r][columns]), end="")
            for q in range(0, columns):
                if mat[r][q] != 0 and q != c:
                    print("+{}".format(mat[r][q]), end="")
            print(")")
            p +=1
        else:
            for f in range(0, free_num):
                if free_variables[f] == z:
                    print("x{} is free".format(z+1))
        # print("\n")

print("Coefficient matrix")
print("Enter number of rows: ", end="")
rows = input()
print("Enter number of columns: ", end="")
columns = input()
matrix = creating_matrix(rows, columns)
columns = int(columns)
rows = int(rows)
print("Given Matrix:")
print(matrix)
# for i in range(0, columns):
i = 0
pivot_array = np.zeros((1, 2))
row_numbers = 0
while i < columns:
    j = i
    while j < columns:
        proper_row = j
        if finding_pivot_column(matrix, j, rows, i) is True:
            if matrix[i][j] == 0:
                proper_row = find_row(matrix, i, j, rows)
            if i == 0:
                pivot_array[0][0] = i
                pivot_array[0][1] = j
                row_numbers += 1
            else:
                new_pivot_array = np.zeros((1, 2))
                new_pivot_array[0][0] = i
                new_pivot_array[0][1] = j
                pivot_array = np.vstack((pivot_array, new_pivot_array))
                row_numbers += 1
            break
        else:
            j += 1
    if proper_row != j and i < rows and proper_row < rows:
        matrix = interchange(matrix, columns, i, j, proper_row)
    # print(matrix)
    matrix = row_replacement(matrix, j, i, rows, columns)
    # print("**************")
    # print(matrix)
    i += 1
# print(matrix)
making_echelon_form(matrix, pivot_array, row_numbers, columns)
# print(matrix)
# print(columns)
free_variables_list = finding_free_variables(matrix, pivot_array, row_numbers, columns)
# print(free_variables_list)
print_result(matrix, free_variables_list, columns, rows, pivot_array, row_numbers)