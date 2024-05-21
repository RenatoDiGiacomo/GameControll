import cv2
import numpy as np
import matplotlib.pyplot as plt

  
# path to input image specified and   
# image is loaded with imread command 
img = cv2.imread('screenshot.png') 
  
# convert image to grayscale 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Shi-Tomasi corner detection function 
# We are detecting only 100 best corners here 
# You can change the number to get desired result. 
corners = cv2.goodFeaturesToTrack(gray_img, 20, 0.01, 10) 
  
# convert corners values to integer 
# So that we will be able to draw circles on them 
corners = np.int0(corners) 
  
# draw red color circles on all corners 
for i in corners: 
    x, y = i.ravel() 
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1) 
  
# resulting image 
plt.imshow(img) 
  
# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows() 



# img=cv2.imread("screenshot.png")
 
# # Converting BGR color to RGB color format
# RGB_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 
# #Displaying image using plt.imshow() method
# plt.imshow(RGB_img)
 
# # hold the window
# plt.waitforbuttonpress()
# plt.close('all')


# img = cv2.imread("screenshot.png",cv2.IMREAD_COLOR)

# plt.imshow(img)

# plt.waitforbuttonpress()
# plt.close('all')

#SHOW
# cv2 .waitKey(0)
# cv2.destroyAllWindows()