from PIL import  Image
import numpy as np
image=Image.open('Sample_image.jpg')
data=np.asarray(image)
print(data)
data_2d=np.reshape(data,(data.shape[0]*data.shape[1],data.shape[2]))
np.savetxt('data.csv', data_2d, delimiter=',')
