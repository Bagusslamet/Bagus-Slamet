from google.colab import drive
drive.mount('/content/drives/')

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from google.colab.patches import cv2_imshow
from skimage import io

#link image
url = ("/content/drives/MyDrive/Colab Notebooks/IMG_20231113_123521.jpg")

image = io.imread(url)
image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
final_frame = cv.hconcat((image, image_2))
cv2_imshow(final_frame)

print(image.size)
print(image.shape)
print(image.dtype)

import numpy as np
a = np.array([[1,2,2,2,10],[10,20,30,40,50]])
print(a)
print(a.ravel())
print(a.flatten())
plt.hist(a.ravel(),bins = 50, range = [0,50])
plt.show()

plt.hist(image.ravel(), bins = 256, range = [0,256])
plt.show()

color = ('b','g','r')
for i,col in enumerate(color):
  histogr = cv.calcHist([image], [i], None, [256], [0,256])
  plt.plot(histogr, color = col)
  plt.xlim([0,325])
plt.show()

color = ('b','g','r')
for i,col in enumerate(color):
  histogr = cv.calcHist([image], [i], None, [4], [0,256])
  plt.plot(histogr, color = col)
  plt.xlim([0,4])
plt.show()

color = ('b','g','r')
for i,col in enumerate(color):
  histogr = cv.calcHist([image], [i], None, [8], [0,256])
  plt.plot(histogr, color = col)
  plt.show()

color = ('b','g','r')
for i,col in enumerate(color):
  histogr = cv.calcHist([image], [i], None, [16], [0,256])
  plt.plot(histogr, color = col)
plt.show()

color = ('b','g','r')
for i,col in enumerate(color):
  histogr = cv.calcHist([image], [i], None, [32], [0,256])
  plt.plot (histogr, color = col)
  plt.show()

b,g,r = cv.split(image)
cv2_imshow(b)

image = io.imread(url)

#blue channel
bluech = image[:,:,0]
cv2_imshow(bluech)

plt.hist(bluech.ravel(), 16, [0, 256], color='blue')
plt.xlabel('Bins 16')
plt.ylabel('Num of Pixel')
plt.show()

plt.hist(bluech.ravel(), 8, [0, 256], color='blue')
plt.xlabel('Bins 32')
plt.ylabel('Num of Pixel')
plt.show()

plt.hist(bluech.ravel(), 32, [0, 256], color='blue')
plt.xlabel('Bins 8')
plt.ylabel('Num of Pixel')
plt.show()

plt.hist(bluech.ravel(), 4, [0, 256], color='blue')
plt.xlabel('Bins 4')
plt.ylabel('Num of Pixel')
plt.show()

#green channel
image = io.imread(url)

greench = image[:,:,1]
cv2_imshow(greench)

plt.hist(bluech.ravel(), 8, [0, 256], color='green')
plt.xlabel('Bins 32')
plt.ylabel('Num of Pixel')
plt.show()

plt.hist(bluech.ravel(), 4, [0, 256], color='green')
plt.xlabel('Bins 4')
plt.ylabel('Num of Pixel')
plt.show()

plt.hist(bluech.ravel(), 16, [0, 256], color='green')
plt.xlabel('Bins 16')
plt.ylabel('Num of Pixel')
plt.show()

plt.hist(bluech.ravel(), 32, [0, 256], color='green')
plt.xlabel('Bins 8')
plt.ylabel('Num of Pixel')
plt.show()

plt.hist(bluech.ravel(), 256, [0, 256], color='green')
plt.xlabel('Bins 256')
plt.ylabel('Num of Pixel')
plt.show()

#red channel

redch = image[:,:,2]
cv2_imshow(redch)

plt.hist(redch.ravel(), 256, [0, 256], color='red')
plt.xlabel('Bins 256')
plt.ylabel('Num of Pixel')
plt.show()

plt.hist(redch.ravel(), 32, [0, 256], color='red')
plt.xlabel('Bins 8')
plt.ylabel('Num of Pixel')
plt.show()

plt.hist(redch.ravel(), 16, [0, 256], color='red')
plt.xlabel('Bins 16')
plt.ylabel('Num of Pixel')

plt.hist(redch.ravel(), 8, [0, 256], color='red')
plt.xlabel('Bins 32')
plt.ylabel('Num of Pixel')

plt.hist(redch.ravel(), 4, [0, 256], color='red')
plt.xlabel('Bins 4')
plt.ylabel('Num of Pixel')

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv2_imshow(gray_image)

plt.hist(gray_image.ravel(), bins = 256, range = [0,256])
plt.show()


print(gray_image.size)
print(gray_image.shape)
print(gray_image.dtype)

plt.hist(gray_image.ravel(), bins = 4, range = [0,256])
plt.show()


print(gray_image.size)
print(gray_image.shape)
print(gray_image.dtype)

invert_gray = 255 - gray_image
cv2_imshow(invert_gray)

plt.hist(invert_gray.ravel(), bins = 256, range = [0,256])
plt.show()

bright_image = (100.0/255)*gray_image + 100
cv2_imshow(bright_image)

plt.hist(bright_image.ravel(), bins = 256, range = [0,256])
plt.show()

darken_image = 255.0*(gray_image/255.0)**2
cv2_imshow(darken_image)

plt.hist(darken_image.ravel(), bins = 256, range = [0,256])
plt.show()



"""progra, diatas adalah memproses dan menganalisis gambar, serta bagaimana melakukan visualisasi dengan histogram untuk memahami distribusi intensitas piksel dalam berbagai saluran warna dan jenis citra.*teks yang dimiringkan*"""
