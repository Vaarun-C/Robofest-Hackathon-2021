import cv2 as cv
import numpy as np

#Read the Image from path
img = cv.imread("C:/Users/IB/Desktop/Test_Image.jpg")

#Convert Image to HSV format
img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#HSV value range for different colours
lower_yellow = np.array([22, 50, 0])
upper_yellow = np.array([56, 255, 255])

lower_green = np.array([33, 30, 30])
upper_green = np.array([117, 255, 255])

lower_red = np.array([0, 30, 39])
upper_red = np.array([17, 255, 255])

lower_blue = np.array([64, 30, 0])
upper_blue = np.array([174, 255, 255])

lower_orange = np.array([4, 29, 20])
upper_orange = np.array([25, 255, 255])

#Set Masks
mask1 = cv.inRange(img_HSV, lower_yellow, upper_yellow)
mask2 = cv.inRange(img_HSV, lower_green, upper_green)
mask3 = cv.inRange(img_HSV, lower_red, upper_red)
mask4 = cv.inRange(img_HSV, lower_blue, upper_blue)
mask5 = cv.inRange(img_HSV, lower_orange, upper_orange)

#Get contours of a given image, here we'll be using the masks
def getContours(img):

	contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
	boxes = []

	for cnt in contours:
		area = cv.contourArea(cnt)

		if(area > 500):
			boxes.append(cnt)

	return boxes

#Get the squares
yellow_boxes = getContours(mask1)
green_boxes = getContours(mask2)
red_boxes = getContours(mask3)
blue_boxes = getContours(mask4)
orange_boxes = getContours(mask5)

#For yellow squares
for box in yellow_boxes:

	M = cv.moments(box)
	cx = int(M["m10"]/M["m00"])  #Get Center of the box
	cy = int(M["m01"]/M["m00"])

	cv.putText(img, "Yellow", (cx-20, cy), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#For Green squares
for box in green_boxes:

	M = cv.moments(box)
	cx = int(M["m10"]/M["m00"])	#Get Center of the box
	cy = int(M["m01"]/M["m00"])

	cv.putText(img, "Green", (cx-20, cy), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#For Red squares
for box in red_boxes:

	M = cv.moments(box)
	cx = int(M["m10"]/M["m00"])	#Get Center of the box
	cy = int(M["m01"]/M["m00"])

	cv.putText(img, "Red", (cx-20, cy), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#For Blue squares
for box in blue_boxes:

	M = cv.moments(box)
	cx = int(M["m10"]/M["m00"])	#Get Center of the box
	cy = int(M["m01"]/M["m00"])

	cv.putText(img, "Blue", (cx-20, cy), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#For Orange squares
for box in orange_boxes:

	M = cv.moments(box)
	cx = int(M["m10"]/M["m00"]) #Get Center of the contour
	cy = int(M["m01"]/M["m00"])

	cv.putText(img, "Orange", (cx-20, cy), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

#Show the labelled image in a new window
cv.imshow("New", img)

#Delay so that output window is visible
cv.waitKey(0)