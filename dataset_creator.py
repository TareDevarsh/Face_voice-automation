import numpy as np
import cv2
from time import sleep
import os


def image_preprocessing(frame):
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray
    
def initialze_folder():

    def make_dir(name):
        if not os.path.exists(name):
            os.makedirs(name)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_folder = 'image_dataset'
    make_dir(os.path.join(BASE_DIR,image_folder))
    name_dataset = input("Enter name of dataset:")
    make_dir(os.path.join(BASE_DIR,image_folder,name_dataset))
    final_dir = os.path.join(BASE_DIR, image_folder, name_dataset)
    return final_dir

def write_images(cascade_obj, path, count, f):
    for (x, y , w , h) in cascade_obj:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        write_img = 'test_image_' + str(count) + '.jpg'
        cv2.imwrite(os.path.join(final_dir, "image_{}.jpg".format(count)),roi_gray)
        f.write(str(count))
        sleep(0.5)


count = 0
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
f = open("demofile2.txt", "w")
final_dir = initialze_folder()

while(True):
    ret, frame = cap.read()
    gray = image_preprocessing(frame)
    face_detect = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
    write_images(face_detect, final_dir, count, f)
    count += 1
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        f.close()
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




