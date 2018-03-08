# USAGE
# python roi.py --image band2.tif
# press c to crop and r to reset
# use mouse to draw cropping area

# import the necessary packages
import argparse
import cv2
import numpy as np
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
img = cv2.imread(args["image"])
image = cv2.resize(img, (750, 750))
clone = image.copy()

img1 = cv2.imread('band3.tif',0)
image1 = cv2.resize(img1, (750, 750))
clone1 = image1.copy()

img2 = cv2.imread('band4.tif',0)
image2 = cv2.resize(img2, (750, 750))
clone2 = image2.copy()

img3 = cv2.imread('band5.tif',0)
image3 = cv2.resize(img3, (750, 750))
clone3 = image3.copy()

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF

	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()

	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break

# if there are two reference points, then crop the region of interest
# from the image and display it
if len(refPt) == 2:
	roi2 = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imshow("ROI", roi2)
	cv2.waitKey(0)
	cv2.imwrite("roi2.jpg",roi2)
	
	roi3 = clone1[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imwrite("roi3.jpg",roi3)
	
	roi4 = clone2[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imwrite("roi4.jpg",roi4)
	
	roi5 = clone3[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imwrite("roi5.jpg",roi5)
	
	# drawing histogram 
	#hist = cv2.calcHist( [roi], [0], None, [256], [0, 256] )
	#cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
	#bin_count = hist.shape[0]
	#bin_w = 1
	#img1 = np.zeros((256, bin_count*bin_w, 3), np.uint8)
	#for i in xrange(bin_count):
	#	h = int(hist[i])
	#	cv2.rectangle(img1, (i*bin_w+2, 255), ((i+1)*bin_w-2, 255-h), (int(180.0*i/bin_count), 255, 255), -1)
	#	img1 = cv2.cvtColor(img1, cv2.COLOR_HSV2BGR)
	#	cv2.imshow('hist', img1)            
	#cv2.waitKey(0)

# close all open windows
cv2.destroyAllWindows()
