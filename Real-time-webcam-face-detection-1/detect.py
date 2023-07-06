import cv2
import sys
import serial
import time
import math

#mapping func
def map_value(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

#sending serial
ser = serial.Serial('COM3', 115200)
  

#detecting faces
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

#getting the dimensions of the screen
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("width {} ".format(width))
print("height {} ".format(height))



while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    # Flip the frame horizontally
    flipped_frame = cv2.flip(frame, 1)


    gray = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30) 
    )
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(flipped_frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
    #getting coo of face center    
        posx=(x+w/2)
        posy=(y+h/2)

    #getting angel x
        Xrotate = map_value(posx, 0, width, 36, 97)
    
    #getting angel y (from up to down the screen)  
        Yrotate = map_value(posy, 0, height, 90, 130)

    # Limit the servo positions to prevent damage to the servos
        Xrotate = max(0, min(100, Xrotate))
        Yrotate = max(95, min(130, Yrotate))
   
        if 1>0:
            
            #sending values to Adruino
            data = str(Xrotate) + "," + str(Yrotate) + "\n" # create the data string
            ser.write(data.encode()) # send the data string to the Arduino

            #console values
            print("posX {} ".format(posx))
            print("posY {} ".format(posy))

            print("angelX {} ".format(Xrotate))   
            print("angelY {} ".format(Yrotate))

            
        

    # Display the resulting frame
    cv2.imshow('Video', flipped_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
video_capture.release()
ser.close()
cv2.destroyAllWindows()