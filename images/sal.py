import cv2
import numpy as np
# load the input image
image = cv2.imread('/home/arul/Desktop/fetal/images/4C.jpg',0)
# initialize OpenCV's static saliency spectral residual detector and
# compute the saliency map
cv2.imshow("Image", image)
cv2.imshow("Output", saliencyMap)
cv2.waitKey(0)

