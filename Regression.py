import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def get_info():
    user_input = input("Enter directory: ")
    df = pd.read_csv(user_input)
    return df


def find_years(df):
    total_rows = len(df.axes[0])
    date_list = df.head(total_rows - 10).Date.to_list()
    year_list = []
    for i in range(0, len(date_list)):
        date = date_list[i].split('/')
        year_list.append(date[2])
    return year_list


def find_data(df):
    total_rows = len(df.axes[0])
    open_l = df.head(total_rows - 10).Open.to_list()
    return open_l


# linear regression
def make_x_matrix(x):
    mat = np.zeros(2)
    mat[0] = 1
    mat[1] = 1
    for i in range(1, len(x)):
        row = np.zeros(2)
        row[0] = 1
        row[1] = i + 1
        mat = np.vstack((mat, row))
    return mat


# polynomial regression
def make_x2_matrix(x):
    mat = np.zeros(3)
    mat[0] = 1
    mat[1] = 1
    mat[2] = 1
    for i in range(1, len(x)):
        row = np.zeros(3)
        row[0] = 1
        row[1] = i + 1
        row[2] = row[1] * row[1]
        mat = np.vstack((mat, row))
    return mat


def find_b(x_mat, y_mat):
    y_mat = np.array(y_mat)
    x = np.dot(x_mat.transpose(), x_mat)
    y = np.dot(x_mat.transpose(), y_mat.transpose())
    b = np.linalg.solve(x, y)
    return b


# linear regression
def find_new_values(x, b):
    new_y = []
    for i in range(0, len(x)):
        new_y.append(float(b[0]) + float(b[1]) * (i + 1))
    return new_y


# polynomial regression
def find_new_values2(x, b):
    new_y = []
    for i in range(0, len(x)):
        new_y.append(float(b[0]) + float(b[1]) * (i + 1) + float(b[2]) * (i + 1) * (i + 1))
    return new_y


def plot_values(linear_y, polynomial_y, df):
    open_list = find_data(df)
    plt.plot(linear_y, color='purple', label='linear')
    plt.plot(polynomial_y, color='orange', label='poly')
    plt.plot(open_list, color='green', label='actual values')
    plt.legend()
    plt.show()


# linear regression
def find_errors(df, b):
    total_rows = len(df.axes[0])
    open_l = df.tail(10).Open.to_list()
    o = df.head(total_rows).Open.to_list()
    print("linear regression: ")
    for i in range(0, 10):
        print(i+1)
        calculated = float(b[0]) + float(b[1]) * (total_rows - 10 + i + 1)
        print("calculated value: {}".format(calculated))
        actual = open_l[i]
        print("actual value: {}".format(actual))
        error = actual - calculated
        print("error: {}".format(error))


# polynomial regression
def find_errors2(df, b):
    total_rows = len(df.axes[0])
    open_l = df.tail(10).Open.to_list()
    print("____________________________")
    print("Polynomial regression: ")
    for i in range(0, 10):
        print(i+1)
        calculated = float(b[0]) + float(b[1]) * (total_rows - 10 + i +1) + float(b[2]) * (total_rows - 10 + i + 1)**2
        print("calculated value: {}".format(calculated))
        actual = open_l[i]
        print("actual value: {}".format(actual))
        error = actual - calculated
        print("error: {}".format(error))


def linear_regression(df):
    years = find_years(df)
    open_list = find_data(df)
    x_matrix = make_x_matrix(years)
    beta = find_b(x_matrix, open_list)
    y = find_new_values(years, beta)
    find_errors(df, beta)
    return y


def polynomial_regression(df):
    years = find_years(df)
    open_list = find_data(df)
    x_matrix = make_x2_matrix(years)
    beta = find_b(x_matrix, open_list)
    y = find_new_values2(years, beta)
    find_errors2(df, beta)
    return y


if __name__ == '__main__':
    all_data = get_info()
    lin_y = linear_regression(all_data)
    pol_y = polynomial_regression(all_data)
    plot_values(lin_y, pol_y, all_data)
