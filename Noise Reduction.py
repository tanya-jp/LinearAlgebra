import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image


def get_image():
    # user_input = input("Enter directory: ")
    image_data = image.imread('noisy.jpg')
    return image_data


def find_new_s(s_row, s_column, s):
    new_s = np.zeros((s_row, s_column))
    for i in range(0, s.shape[0], 1):
        if s[i] > 1750:
            new_s[i][i] = s[i]
    return new_s


def process(noisy_image):
    row = noisy_image.shape[0]
    column = noisy_image.shape[1]
    matrix0 = np.zeros((row, column))
    for r in range(0, row, 1):
        for c in range(0, column, 1):
            matrix0[r][c] = noisy_image[r][c][0]
    u0, s0, v0 = np.linalg.svd(matrix0)
    s_row = u0.shape[1]
    s_column = v0.shape[0]
    new_s0 = find_new_s(s_row, s_column, s0)

    matrix1 = np.zeros((row, column))
    for r in range(0, row, 1):
        for c in range(0, column, 1):
            matrix1[r][c] = noisy_image[r][c][1]
    u1, s1, v1 = np.linalg.svd(matrix1)
    new_s1 = find_new_s(s_row, s_column, s1)

    matrix2 = np.zeros((row, column))
    for r in range(0, row, 1):
        for c in range(0, column, 1):
            matrix2[r][c] = noisy_image[r][c][2]
    u2, s2, v2 = np.linalg.svd(matrix2)
    new_s2 = find_new_s(s_row, s_column, s0)

    new_image = np.zeros((row, column, 3), dtype='uint8')
    matrix0 = np.dot(u0, new_s0)
    matrix0 = np.dot(matrix0, v0)
    matrix1 = np.dot(u1, new_s1)
    matrix1 = np.dot(matrix1, v1)
    matrix2 = np.dot(u2, new_s2)
    matrix2 = np.dot(matrix2, v2)
    for r in range(0, row, 1):
        for c in range(0, column, 1):
            new_image[r][c][0] = matrix0[r][c]
            new_image[r][c][1] = matrix1[r][c]
            new_image[r][c][2] = matrix2[r][c]
    plt.imsave('cleaned image.jpeg', new_image)
    plt.imshow(new_image)
    plt.show()


if __name__ == '__main__':
    input_image = get_image()
    process(input_image)
