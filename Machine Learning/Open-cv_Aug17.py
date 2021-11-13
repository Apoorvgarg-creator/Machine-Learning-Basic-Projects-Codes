# Open cv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


# Read an image
img = cv2.imread('/Users/apoorvgarg/Documents/GitHub/machine-learning-online-2018/6. Project - Face Recognition/OpenCV Basics/dog.png')
# An image is 3D matrix, 100*100*3, # represent the 3 RGB channel
# In opencv, by default its reads the image as BGR

newimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# matplotlib reads and BGR image but displays RGB image
plt.imshow(newimg)

plt.show()

# print(img)

# pic = img.reshape(img[0]*img[1], 3)
# print(pic)
gray = cv2.imread('/Users/apoorvgarg/Documents/GitHub/machine-learning-online-2018/6. Project - Face Recognition/OpenCV Basics/dog.png', cv2.IMREAD_GRAYSCALE)
# To read and show an image
# if we use imshow of cv2 it reads a BGR image and display BGR image
# cv2.imshow('DOG', gray)

# cv2.waitKey(0) # program will stop when any key is pressed
# cv2.destroyAllWindows()

# # Working with Video stream from webcam
# # Video is a series of frame
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     if ret == False: continue
#
#     cv2.imshow('Video Frame',frame)
#     cv2.imshow('Gray Frame', gray_frame)
#
#     # wait for user input - q then you will stop the loop
#
#     key_pressed = cv2.waitKey(1) & 0xFF
#     #  with the help of & 0xFF, we will get a 8-bit number as cv2.waitkey returns 32 bit  32 bit & 8 bit --> 8 bit
#     if key_pressed == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# # Face detection using HaarCascades (Opencv)
#
# cap = cv2.VideoCapture(0)
# path = "/Users/apoorvgarg/Documents/GitHub/opencv/data/haarcascades/haarcascade_frontalface_alt.xml"
# face_cascade = cv2.CascadeClassifier("/Users/apoorvgarg/Documents/GitHub/machine-learning-online-2018/6. Project - Face Recognition/Face Recognition Project/haarcascade_frontalface_alt.xml")
#
#
# while True:
#     ret, frame = cap.read()
#     gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     if ret == False: continue
#
#     faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     cv2.imshow('Video Frame', frame)
#     # cv2.imshow('Gray Frame', gray_frame)
#
#     # wait for user input - q then you will stop the loop
#
#     key_pressed = cv2.waitKey(1) & 0xFF
#     #  with the help of & 0xFF, we will get a 8-bit number as cv2.waitkey returns 32 bit  32 bit & 8 bit --> 8 bit
#     if key_pressed == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#

# Generating selfie training data using webcam

# Initialize the camera
cap = cv2.VideoCapture(0)

# Face detection
face_cascade = cv2.CascadeClassifier("/Users/apoorvgarg/Documents/GitHub/machine-learning-online-2018/6. Project - "
                                     "Face Recognition/Face Recognition Project/haarcascade_frontalface_alt.xml")
skip = 0

face_data = []
dataset_path = '/Users/apoorvgarg/PycharmProjects/CB_lecture/data/'
filename = input("Enter the person whose face is scanning")
while True:

    ret, frame = cap.read()

    if not ret:
        continue

    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    if len(faces) == 0:
        continue

    faces = sorted(faces, key=lambda f: f[2]*f[3])

    # print(faces)
    # Pick the last face because it is the largest face acc to area
    for face in faces[-1:]:

        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

        # Extract (Crop out the required face) : Region of Interest
        offset = 10
        face_section = frame[y-offset:y+h+offset, x-offset:x+w+offset]
        face_section = cv2.resize(face_section, (100, 100))

        skip += 1
        if skip % 10 == 0:
            face_data.append(face_section)
            print(len(face_data))

    cv2.imshow("Frame", frame)
    cv2.imshow("Face section", face_section)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
# Convert our face list array into numpy array
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)
# save the data into file system
np.save(dataset_path+filename+'.npy', face_data)
print("Success !")

cap.release()
cv2.destroyAllWindows()


# # building Face classifier
#
# ########## KNN CODE ############
#
# def distance(v1, v2):
#     # Eucledian
#     return np.sqrt(((v1 - v2) ** 2).sum())
#
#
# def knn(train, test, k=5):
#     dist = []
#
#     for i in range(train.shape[0]):
#         # Get the vector and label
#         ix = train[i, :-1]
#         iy = train[i, -1]
#         # Compute the distance from test point
#         d = distance(test, ix)
#         dist.append([d, iy])
#     # Sort based on distance and get top k
#     dk = sorted(dist, key=lambda x: x[0])[:k]
#     # Retrieve only the labels
#     labels = np.array(dk)[:, -1]
#
#     # Get frequencies of each label
#     output = np.unique(labels, return_counts=True)
#     # Find max frequency and corresponding label
#     index = np.argmax(output[1])
#     return output[0][index]
# ################################
#
# # Init camera
#
#
# cap = cv2.VideoCapture(0)
#
# # Face detection
# face_cascade = cv2.CascadeClassifier("/Users/apoorvgarg/Documents/GitHub/machine-learning-online-2018/6. Project - "
#                                      "Face Recognition/Face Recognition Project/haarcascade_frontalface_alt.xml")
#
# skip = 0
# dataset_path = '/Users/apoorvgarg/PycharmProjects/CB_lecture/data/'
#
# face_data = []  #
# labels = []    #
#
# class_id = 0  # Label for the given file
# names = {}   # Mapping btw id - name
#
# # data preparation
# for fx in os.listdir(dataset_path):
#     if fx.endswith('.npy'):
#         names[class_id] = fx[:-4]
#         data_item = np.load(dataset_path+fx)
#         face_data.append(data_item)
#
#         # create Labels foe the class
#         target = class_id*np.ones((data_item.shape[0],))
#         class_id += 1
#         labels.append(target)
#
# face_dataset = np.concatenate(face_data, axis=0)
# face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))
#
# print(face_dataset.shape)
# print(face_labels.shape)
#
# trainset = np.concatenate((face_dataset, face_labels), axis=1)
# print(trainset.shape)
#
# # Testing
#
# while True:
#     ret, frame = cap.read()
#
#     if not ret:
#         continue
#     faces = face_cascade.detectMultiScale(frame, 1.3, 5)
#
#     for face in faces:
#         x,y,w,h = face
#         offset =10
#         face_section =frame[y-offset:y+h+offset, x-offset:x+w+offset]
#         face_section = cv2.resize(face_section,(100,100))
#
#         out = knn(trainset,face_section.flatten())
#         pred_name = names[int(out)]
#         cv2.putText(frame.pred_name,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2,cv2.LINE_AA)
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
#
#     cv2.imshow("Faces",frame)
#     key =cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
