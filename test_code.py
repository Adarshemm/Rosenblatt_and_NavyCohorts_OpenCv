#import dependencies
#pip install opencv-python //on the terminal
#improt opencv for computer vision 
import cv2
#import for visualization of image
from matplotlib import pyplot as plt

capture = cv2.VideoCapture(0)
#read the captured image. returns true if the webcam is active and responds. frame gives vector representation of the image
ret, frame = capture.read()

#prints either true or false with respect to the device feedback
print(ret)

print(frame)

#shows the frame in a image representation 
plt.imshow(frame)

#releases the device from the use
capture.release()