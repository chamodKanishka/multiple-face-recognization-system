
import cv2
import os
import sys
from imutils.video import VideoStream
import time 
import imutils
import sqlite3
import argparse

# usage
# python get_img.py -db=D:/myprojects/opencv-face-recognition/data/log.db

# vs = VideoStream(src=0).start()
# time.sleep(2.0)
parser = argparse.ArgumentParser(description='Get commnd line argument')
parser.add_argument("-db",
                    "--DB_path",
                    help='Enter the Data base path',
                    required=True)
 
args = parser.parse_args()
db_path = args.DB_path
conn = sqlite3.connect(db_path)
    

camera = cv2.VideoCapture(0)
i = 0

data_path = "D:/myprojects/opencv-face-recognition/dataset"  
username = input("enter the name :")

cursor = conn.cursor()


cursor.execute("Insert into emp_data(U_name)values(?)", (username,))
conn.commit()
conn.close()
if not os.path.exists(os.path.join(data_path, username)):
    os.makedirs(os.path.join(data_path, username))  

# vs = VideoStream(src=0).start()
# time.sleep(2.0)
while i < 10:

    # frame = vs.read()
    
    input('Press Enter to capture')
    
    return_value, image = camera.read()
    cv2.imwrite(os.path.join(data_path, username,'Train'+str(i)+'.png'), image)
    i += 1
    # cv2.imshow("Frame", frame)
    # key = cv2.waitKey(1) & 0xFF
# cv2.imshow(image)
del(camera)
# cv2.destroyAllWindows()
# vs.stop()
