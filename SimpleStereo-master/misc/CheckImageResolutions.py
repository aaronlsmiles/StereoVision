import numpy as np
import cv2

import simplestereo as ss
"""
Rectify a couple of images starting from a calibrated stereo rig
"""

# Load stereo rig from file
rig = ss.StereoRig.fromFile("stereoRig.json")

# Rectify and obtain rectified stereo rig
rigRect = ss.rectification.directRectify(rig)

# Optionally save it to file, so you can load it directly as rectified.

# Read right and left image (please ensure the order!!!)
img1 = cv2.imread('left.png')
img2 = cv2.imread('right.png')

# ERROR # Image size is different from the one resulting from calibration
print(f"Expected image 1 resolution is {rigRect.res1}")
print(f"Input image 1 resolution is {img1.shape[:2][::-1]}")

print(f"Expected image 2 resolution is {rigRect.res2}")
print(f"Input image 2 resolution is {img2.shape[:2][::-1]}")

#rigRect.computeRectificationMaps(zoom=1.5) # May help removing unwanted border

# Simply rectify two images (it takes care of distortion too)
img1_rect, img2_rect = rigRect.rectifyImages(img1, img2)

# Show images together
visImg = np.hstack((img1_rect, img2_rect))

# Draw some horizontal lines as reference
# (after rectification all horizontal lines are epipolar lines)
for y in [289, 332, 362]:
    cv2.line(visImg, (0,y), (visImg.shape[1],y), color=(0,0,255), thickness=2)

cv2.imshow('Rectified images', visImg)
cv2.waitKey(0)
cv2.destroyAllWindows()