import numpy as np
import cv2
from time import sleep
import os
import pickle


def frame_capture(labels):
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('solo.yml')


    while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_detect = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
    
        cv2.putText(frame, 'Smile for the Camera',(180,80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,225,40), 2, cv2.LINE_AA)

        for (x, y , w , h) in face_detect:
            roi_gray = gray[y:y+h, x:x+w]
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),3)
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 50 and conf <= 100:
                print(labels[id_])
                cv2.putText(frame, labels[id_],(x,y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,225,0), 2, cv2.LINE_AA)
        

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            sleep(1)
            break

    return labels[id_]


        

def label_read():
    labels = {}

    with open('labels.pickle', 'rb') as f:
        labels = pickle.load(f)
        labels = {v:k for k,v in labels.items()}

    return labels

if __name__ == "__main__":

    labels = label_read()
    frame_capture(labels)

        
            
    