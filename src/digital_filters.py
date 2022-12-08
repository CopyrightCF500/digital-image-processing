import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def mean_filter(img: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    pass


if __name__ == '__main__':
    print('Digital Image Processing - Different Filters')
    img = cv.imread('../res/HM_Karlstr.jpg', 0)
    plt.imshow(img, cmap='gray')

