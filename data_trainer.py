import numpy as np
import cv2
import os
from PIL import Image
import pickle


def train_data(dataset, label_id_all):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    recognizer.train(dataset,np.array(label_id_all))
    recognizer.save('solo.yml')



def create_training_array():
    pass
    #funtion for creating a numpy array from images

current_id = 0
label_ids = {}
x_train =[]
y_labels = []
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, 'image_dataset')

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith('jpg'):
            path = os.path.join(root,file)
            label = os.path.basename(os.path.dirname(path)).replace(' ', '_').lower()
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]

            pil_image = Image.open(path)
            face_detect = face_cascade.detectMultiScale(pil_image, scaleFactor = 1.1, minNeighbors = 5)
            for (x, y , w , h) in cascade_obj:
                roi_gray = gray[y:y+h, x:x+w]
                np_image_arr = np.array(roi_gray, 'uint8')
                x_train.append(np_image_arr)
                y_labels.append(id_)

with open('labels.pickle', 'wb') as f:
    pickle.dump(label_ids, f)

train_data(x_train,y_labels)


