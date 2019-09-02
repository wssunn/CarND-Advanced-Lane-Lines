**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: ./output_images/im0_test.jpg "Origin"
[image2]: ./output_images/im1_undist.jpg "Undistorted"
[image3]: ./output_images/im2_colorChannel.jpg "Binary"
[image4]: ./output_images/im3_perspecTrans.jpg "Warp Example"
[image5]: ./output_images/im5_effi.jpg "Fit Visual"
[image6]: ./output_images/im7_final.jpg "Output"
[video1]: ./output_images/project_video.mp4 "Video"


### Camera Calibration

Here is the original picture:

![alt text][image1]

#### 1. Computed the camera matrix and distortion coefficients

The code for this step is contained in the 4-9 code cell of the IPython notebook located in "./code.ipynb" (or in lines # through # of the file called `utils_calibration.py`).  

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

I then used the output `objpoints` and `imgpoints` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function.  I applied this distortion correction to the test image using the `cv2.undistort()` function

### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

I applied distortion coefficients and obtained the following picture:
![alt text][image2]

#### 2. Use color transforms, gradients or other methods to create a thresholded binary image.

I used a combination of color and gradient thresholds to generate a binary image (thresholding steps at lines # through # in `utils_threshold.py`).  Here's an example of my output for this step. 

![alt text][image3]

#### 3. Pperformed a perspective transform

The code for my perspective transform includes a function called `perspec_trans()`, which appears in lines 6 through 33 in the file `utils_transform.py`.  The `perspec_trans()` function takes as inputs an image (`img`).  I chose the hardcode the source and destination points in the following manner:

```python
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
```

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image4]

#### 4. Identified lane-line pixels and fit their positions with a polynomial

Then I did some other stuff and fit my lane lines with a 2nd order polynomial. The function is called `fit_polynomial` (line 87 to 111) and `search_around_poly` (line 125 to 168) in file `utils_lane.py`.

![alt text][image5]

#### 5. Calculated the radius of curvature of the lane and the position of the vehicle with respect to center

I did this with function `measure_curvature_real` in lines 201 through 222 in my code in `utils_lane.py` and `calc_deviation` in lines 224 through 234.

#### 6. Final output

I implemented this step in lines # through # in my codecell 21 and 22 in `code.ipynb`.  Here is an example of my result on a test image:

![alt text][image6]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.

Here's a [link to my video result](./project_video.mp4)

---

### Discussion

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  

During step 2, I coverted the picture into HLS channel and used L and S channel. `S channel` is very effective in detecting yellow lines, which `L channel` helps to detect white line. However, `S channel` also includes the shadow of the ground. To slove this problem, I have used `L channel` with threshold 0 to 50 to filter out the dark bit.

My pipeline did not work on the challenge video however. In fact in failed badly on it. 
