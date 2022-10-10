import numpy as np
import cv2
import glob

CHESSBOARDSIZE = (7,6)

if __name__ == "__main__":
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-6)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((CHESSBOARDSIZE[0]*CHESSBOARDSIZE[1], 3), np.float32)
    objp[:,:2] = np.mgrid[0:CHESSBOARDSIZE[0],0:CHESSBOARDSIZE[1]].T.reshape(-1,2)

    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.

    images = glob.glob('./res/4/calib-10/*.png')

    i=0
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, CHESSBOARDSIZE)

        # If found, add object points, image points (after refining them)
        if ret == True:
            i+=1
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            imgpoints.append(corners2)
            print(i,'...')
            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, CHESSBOARDSIZE, corners2,ret)
            cv2.imshow('img',img)
            cv2.waitKey(0)

    cv2.destroyAllWindows()