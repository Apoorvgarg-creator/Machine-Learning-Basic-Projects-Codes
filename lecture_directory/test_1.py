import cv2
import matplotlib.pyplot as plt
test=cv2.imread('Sample_image.jpg')
test_1=cv2.cvtColor(test,cv2.COLOR_BGR2RGB)
plt.imshow(test_1)
plt.show()
print(test_1)


