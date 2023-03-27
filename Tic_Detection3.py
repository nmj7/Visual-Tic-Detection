# Importing the Pandas libraries  
import pandas as panda  

# Importing the OpenCV libraries  
import cv2  

# Importing the time module  
import time  

# Importing the datetime function of the datetime module  
from datetime import datetime 

# Assigning our initial state in the form of variable initialState as None for initial frames  
initialState = None   

# starting the webCam to capture the video using cv2 module  
video = cv2.VideoCapture(0)  

# initializing a variable for previous gray scale
prev_gray_frame=None

# using infinite loop to capture the frames from the video 
while True:  

   # Reading each image or frame from the video using read function 

   check, cur_frame = video.read()  

   

   # Defining 'tic' variable equal to zero as initial frame 

   tic = 0  

   

   # From colour images creating a gray frame 

   gray_image = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)  

   

   # To find the changes creating a GaussianBlur from the gray scale image  

   gray_frame = cv2.GaussianBlur(gray_image, (21, 21), 0)  

   

   # For the first iteration checking the condition we will assign grayFrame to initalState if is none  

   if initialState is None:  

       initialState = gray_frame  

       continue  

       

   # Calculation of difference between static or initial and gray frame we created  

   differ_frame = cv2.absdiff(initialState, gray_frame)  


   # Calculate the absolute difference between the current gray frame and the previous gray frame

   if prev_gray_frame is not None:
       abs_diff = cv2.absdiff(gray_frame, prev_gray_frame)
   else:
       abs_diff = differ_frame
    


   # Set the threshold value for detecting sudden movements

   threshold = 30

   # Check if the absolute difference is greater than the threshold

   if (abs_diff > threshold).any():
       tic = 1

   prev_gray_frame = gray_frame.copy()

   # the change between static or initial background and current gray frame are highlighted 

   thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]  
   thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)  

   

   # For the pateint in the frame finding the coutours 

   cont,_ = cv2.findContours(thresh_frame.copy(),   

                      cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  

   

   for cur in cont:  

     

       (cur_x, cur_y,cur_w, cur_h) = cv2.boundingRect(cur)    

       

       # To create a rectangle of green color if a Tic is present  

       cv2.rectangle(cur_frame, (cur_x, cur_y), (cur_x + cur_w, cur_y + cur_h), (0, 255, 0), 3) 
# In the gray scale displaying the captured image 

   cv2.imshow("The image captured in the Gray Frame is shown below: ", gray_frame)  

   

   # To display the difference between inital static frame and the current frame 

   cv2.imshow("Difference between the  inital static frame and the current frame: ", differ_frame)  

   

   # To display on the frame screen the black and white images from the video  

   cv2.imshow("Threshold Frame created from the PC or Laptop Webcam is: ", thresh_frame)  

   

   # Through the colour frame displaying the contour of the object

   cv2.imshow("From the PC or Laptop webcam, this is one example of the Colour Frame:", cur_frame)  


   # Creating a key to wait  

   wait_key = cv2.waitKey(1)  

   # With the help of the 'm' key ending the whole process of our system   

   if wait_key == ord('q'):  

       # adding the motion variable value to motiontime list when something is moving on the screen  

       if tic == 1:  

           print("Tic Detected") 

       else:
           print("Tic not Detected")

       break 


       

# Releasing the video   
video.release()  

# Now, Closing or destroying all the open windows with the help of openCV  
cv2.destroyAllWindows()