import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy import fft


def wiener(input, PSF, eps, K=0.1):  # Wiener filtering，K=0.01
    input_fft = fft.fft2(input)
    PSF_fft = fft.fft2(PSF) + eps
    PSF_fft_1 = np.conj(PSF_fft) / (np.abs(PSF_fft) ** 2 + K)
    result = fft.ifft2(input_fft * PSF_fft_1)
    result = np.abs(fft.fftshift(result))
    return result


img = cv2.imread('../res/london_motion_blurred.jpg', 0)
PSF = np.ones((512, 768)) / 25

scale_percent = 30
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

result = wiener(resized_img, PSF, 1e-3)

cv2.imshow('image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

