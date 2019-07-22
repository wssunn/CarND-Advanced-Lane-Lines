import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def perspec_trans(img):
    # Define calibration box in source (original) 
    # and destination (desired orwarped) coordinates
    
    img_size = (img.shape[1], img.shape[0])
    
    src = np.float32(
        [[200, 718], 
         [522, 500],
         [769, 500],
         [1100, 718]])
    
    dst = np.float32(
        [[362, 718],
         [362, 500],
         [934, 500],
         [934, 718]])
    
    # compute transformation
    M = cv2.getPerspectiveTransform(src, dst)
    
    # compute inverse transformation by swapping the input parameter
    # Minv = cv2.getPerspectiveTransform(dst, src)

    # create warped image - use linear interpolation
    warped = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_LINEAR)

    return warped

def inverse_trans(img):
    img_size = (img.shape[1], img.shape[0])
    
    src = np.float32(
        [[200, 718], 
         [522, 500],
         [769, 500],
         [1100, 718]])
    
    dst = np.float32(
        [[362, 718],
         [362, 500],
         [934, 500],
         [934, 718]])
    
    Minv = cv2.getPerspectiveTransform(dst, src)
    warped = cv2.warpPerspective(img, Minv, img_size, flags=cv2.INTER_LINEAR)
    
    return warped