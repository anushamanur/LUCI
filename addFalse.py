import matplotlib.pyplot as plt
import cv2
src = cv2.imread("BAND2.tif", cv2.IMREAD_GRAYSCALE)
dst = cv2.applyColorMap(src, cv2.COLORMAP_JET)
cv2.imwrite("b2.jpg",dst)

src = cv2.imread("BAND3.tif", cv2.IMREAD_GRAYSCALE)
dst = cv2.applyColorMap(src, cv2.COLORMAP_JET)
cv2.imwrite("b3.jpg",dst)

src = cv2.imread("BAND4.tif", cv2.IMREAD_GRAYSCALE)
dst = cv2.applyColorMap(src, cv2.COLORMAP_JET)
cv2.imwrite("b4.jpg",dst)

src = cv2.imread("BAND5.tif", cv2.IMREAD_GRAYSCALE)
dst = cv2.applyColorMap(src, cv2.COLORMAP_JET)
cv2.imwrite("b5.jpg",dst)

src = cv2.imread("BAND2.tif", cv2.IMREAD_GRAYSCALE)
dst = cv2.applyColorMap(src, cv2.COLORMAP_RAINBOW)
cv2.imwrite("B2.jpg",dst)

src = cv2.imread("BAND3.tif", cv2.IMREAD_GRAYSCALE)
dst = cv2.applyColorMap(src, cv2.COLORMAP_RAINBOW)
cv2.imwrite("B3.jpg",dst)

src = cv2.imread("BAND4.tif", cv2.IMREAD_GRAYSCALE)
dst = cv2.applyColorMap(src, cv2.COLORMAP_RAINBOW)
cv2.imwrite("B4.jpg",dst)

src = cv2.imread("BAND5.tif", cv2.IMREAD_GRAYSCALE)
dst = cv2.applyColorMap(src, cv2.COLORMAP_RAINBOW)
cv2.imwrite("B5.jpg",dst)
