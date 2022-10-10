import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image


def get_image():
    user_input = input("Enter directory: ")
    image_data = image.imread(user_input)
    plt.imshow(image_data)
    plt.show()
    return image_data


def make_new_image(img):
    main_image = img
    shape = main_image.shape
    row_value = shape[0]
    column_value = shape[1] + 100
    new_image = np.zeros((row_value, column_value, 3), dtype='uint8')
    for row in range(0, shape[0], 1):
        for column in range(0, shape[1], 1):
            for RGB in range(0, 3, 1):
                if main_image[row][column][0] == 255 and main_image[row][column][1] == 255 and main_image[row][column][2] == 255:
                    new_image[row][column][RGB] = main_image[row][column][RGB]
                else:
                    new_image[row][column][RGB] = 100

    for row in range(0, shape[0], 1):
        for column in range(shape[1], column_value, 1):
            for RGB in range(0, 3, 1):
                new_image[row][column][RGB] = 255
    plt.imshow(new_image)
    plt.show()
    return new_image


def shear_transformation(img):
    gray_image = img
    shape = gray_image.shape
    row_value = shape[0]
    column_value = shape[1]
    new_image = np.zeros((row_value, column_value+gray_image.shape[0], 3), dtype='uint8')
    for row in range(0, shape[0], 1):
        for column in range(0, shape[1], 1):
            for RGB in range(0, 3, 1):
                new_image[row][-row+column][RGB] = gray_image[row][column][RGB]

    for row in range(0, new_image.shape[0], 1):
        for column in range(0, new_image.shape[1], 1):
            if new_image[row][column][0] == 0 and new_image[row][column][1] == 0 and new_image[row][column][2] == 0:
                for RGB in range(0, 3, 1):
                    new_image[row][column][RGB] = 255

    correct_image = np.zeros((new_image.shape[0], new_image.shape[1], 3), dtype='uint8')
    for row in range(0, correct_image.shape[0], 1):
        for column in range(0, int(correct_image.shape[1] / 2), 1):
            for RGB in range(0, 3, 1):
                correct_image[row][int(correct_image.shape[1] / 2) + column][RGB] = new_image[row][column][RGB]

    for row in range(0, correct_image.shape[0], 1):
        for column in range(int(correct_image.shape[1]/2)+1, correct_image.shape[1], 1):
            for RGB in range(0, 3, 1):
                correct_image[row][int(-correct_image.shape[1]/2)+column][RGB] = new_image[row][column][RGB]
    plt.imshow(correct_image)
    plt.show()
    return correct_image


def make_final_image(f_img, s_image):
    shape_first = f_img.shape
    shape_sheared = s_image.shape
    final_img = np.zeros((shape_sheared[0], shape_sheared[1], 3), dtype='uint8')
    for row in range(0, shape_first[0], 1):
        for column in range(0, shape_first[1], 1):
            if f_img[row][column][0] == 255 and f_img[row][column][1] == 255 and f_img[row][column][2] == 255:
                for RGB in range(0, 3, 1):
                    final_img[row][column][RGB] = s_image[row][column][RGB]

    for row in range(0, shape_sheared[0], 1):
        for column in range(shape_first[1], shape_sheared[1], 1):
            for RGB in range(0, 3, 1):
                final_img[row][column][RGB] = s_image[row][column][RGB]
    plt.imshow(final_img)
    plt.show()

    for row in range(0, shape_first[0], 1):
        for column in range(0, shape_first[1], 1):
            if final_img[row][column][0] == 0 and final_img[row][column][1] == 0 and final_img[row][column][2] == 0:
                for RGB in range(0, 3, 1):
                    final_img[row][column][RGB] = f_img[row][column][RGB]

    plt.imshow(final_img)
    plt.show()


if __name__ == '__main__':
    first_image = get_image()
    img = make_new_image(first_image)
    sheared_image = shear_transformation(img)
    make_final_image(first_image, sheared_image)
