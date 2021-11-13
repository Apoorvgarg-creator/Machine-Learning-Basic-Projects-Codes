import numpy as np
import cv2

img=cv2.imread("Sample_image.jpg")
print(type(img))
print(img.shape)

img_f=np.reshape(img,(430*430,3))

np.savetxt('sol3.csv',img_f, delimiter=',',header="r,g,b", fmt='%s')