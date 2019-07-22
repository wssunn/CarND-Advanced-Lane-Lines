import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle
import glob
import os

def cal_undistort(img, objpoints, imgpoints):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_shape = (img.shape[1], img.shape[0]) #img.shape[::-1]
    
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
                                    objpoints, imgpoints, img_shape,None,None)
    undist = cv2.undistort(img, mtx, dist, None, mtx)
    return undist

def corners_unwarp(filename, nx, ny, objpoints, imgpoints):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_size = (img.shape[1], img.shape[0]) #img.shape[::-1]
    
    objp = np.zeros((ny*nx,3), np.float32)
    objp[:,:2] = np.mgrid[0:nx, 0:ny].T.reshape(-1,2) # x, y coordinate

    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

    if ret == True:
        objpoints.append(objp); imgpoints.append(corners)
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
                                objpoints, imgpoints, img_size,None,None)
        undist = cv2.undistort(img, mtx, dist, None, mtx)
        
        offset = 100
        src = np.float32([corners[0], corners[nx-1], corners[-1], corners[-nx]])
        dst = np.float32([[offset, offset], 
                          [img_size[0]-offset, offset], 
                          [img_size[0]-offset, img_size[1]-offset], 
                          [offset,             img_size[1]-offset]])
        # Given src and dst points, calculate the perspective transform matrix
        M = cv2.getPerspectiveTransform(src, dst)
        warped = cv2.warpPerspective(undist, M, img_size)
        # cv2.imwrite('./output_images/warped_{}.jpg'.format(filename[-6:-4]), warped)
        
        # Save the camera calibration result for later use (we won't worry about rvecs / tvecs)
#         dist_pickle = {}
#         dist_pickle["mtx"] = mtx
#         dist_pickle["dist"] = dist
#         pickle.dump( dist_pickle, open( "./output_images/warped_{}.p".format(filename[-6:-4]), "wb" ) )

        # Return the resulting image and matrix
        print(filename, ' complete')
        return warped, M
    
    else:
        print('None founded', filename)
        return None, None
