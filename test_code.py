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

def click_photo():
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    cv2.imwrite('webcamphoto.jpg', frame)
    capture.release()

#To click just a picture use this function
#click_photo()

#To get the complete Webcam as Video like how a webcam works
capture = cv2.VideoCapture(0)

#in a loop of frames until we force quit
while capture.isOpened():
    ret, frame = capture.read()

    #show image
    cv2.imshow('WebCam', frame)

    #check whether the key q has been pressed for force quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release webcam
capture.release()
#close all windows that is the shown frame
cv2.destroyAllWindows()