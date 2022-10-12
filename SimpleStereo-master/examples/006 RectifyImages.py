import sys
import os

import cv2

import simplestereo as ss
"""
Rectify a couple of images using a RectifiedStereoRig
"""

# Paths
curPath = os.path.dirname(os.path.realpath(__file__))
imgPath = os.path.join(curPath,"res","scenes","3")
loadFile = os.path.join(curPath,"res","5","rigRect.json")      # StereoRigRect file

# Load stereo rig from file
rigRect = ss.RectifiedStereoRig.fromFile(loadFile)

# Read right and left image (please ensure the order!!!)
img1 = cv2.imread(os.path.join(imgPath,'1_L.png')) #left
img2 = cv2.imread(os.path.join(imgPath,'1_R.png')) #right

# CHECK # If image size is different from the one resulting from calibration
print(f"Expected image 1 resolution is {rigRect.res1}")
print(f"Input image 1 resolution is {img1.shape[:2][::-1]}")
print(f"Expected image 2 resolution is {rigRect.res2}")
print(f"Input image 2 resolution is {img2.shape[:2][::-1]}")

#rigRect.computeRectificationMaps(zoom=1.5) # May help removing unwanted border

# Simply rectify two images (it takes care of distortion too)
img1_rect, img2_rect = rigRect.rectifyImages(img1, img2)

# Draw some horizontal lines as reference (after rectification all horizontal lines are epipolar lines)
for y in [289,332, 362, 500, 700]:
    cv2.line(img1_rect, (0,y), (3840,y), color=(0,0,255), thickness=3)
    cv2.line(img2_rect, (0,y), (3840,y), color=(0,0,255), thickness=3)

# Show images
cv2.imshow('img1 Rectified', img1_rect)
cv2.imshow('img2 Rectified', img2_rect)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done!")
