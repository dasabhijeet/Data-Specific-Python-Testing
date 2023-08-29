
# coding: utf-8

# In[1]:


# Here we will use scientific computation libraries and frameworks for image manipulation, including tensor calculations #


# In[12]:


# 1. Image reading and basic manipulation

import matplotlib.image as mpimg
import os
# First, load the image
#dir_path = os.path.dirname(os.path.realpath(__file__))
#filename = dir_path + "/Sweet Girl.jpg"

filename = "Sweet Girl.jpg"

# Load the image
image = mpimg.imread(filename)

# Print out its shape
print(image.shape)

# Print out the image22
import matplotlib.pyplot as plt
imgplot = plt.imshow(image)
print(imgplot)


# In[3]:


# 2. Image reading & V2 advance manipulation (MATRIX TRANSPOSE)

import tensorflow as tf
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# First, load the image again
image = mpimg.imread("Sweet Girl.jpg")

# Create a TensorFlow Variable
x = tf.Variable(image, name='x')

model = tf.global_variables_initializer()

with tf.Session() as session:
    x = tf.transpose(x, perm=[1, 0, 2])
    session.run(model)
    result = session.run(x)


plt.imshow(result)
plt.show()


# In[8]:


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cute-sweet-baby-girl.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
img = ""


# In[5]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img2 = cv2.imread("cute-sweet-baby-girl.jpg")

print("Image 1-\n",cv2.imshow('image',img2))      # 
cv2.waitKey(8000)
cv2.destroyAllWindows()


#Seperate in 2x2 mat.
px = img2[100,100]
print("Data-",px)


ball = img2[280:340, 330:390]
img2[273:333, 100:160] = ball


img3 = mpimg.imread("Sweet Girl.jpg")
print("Image 2-\n",plt.imshow(img3))


# In[2]:


from PIL import Image
img = Image.open('Sweet Girl.jpg')    # Open image as Pillow image object
rsize = img.resize((img.size[0]/10,img.size[1]/10)) # Use Pillow to resize
rsizeArr = np.asarray(rsize)  # Get array back
imgplot = plt.imshow(rsizeArr)
print(imgplot)


# In[33]:


from PIL import Image as imgx
import numpy as np
import matplotlib.pyplot as plt

img = imgx.open("Sweet Girl.jpg")

#print(plt.imshow(img))


rsize = img.resize((np.array(img.size)/10).astype(int)) # Use PIL to resize

#print(rsize)

rsizeArr = np.asarray(rsize)  # Get array back
print(rsizeArr.shape)

#imgplot = plt.imshow(rsizeArr, interpolation='bilinear')

imgplot.set_interpolation('nearest')
imgplot.figure

#print(imgplot)


# In[53]:


# 6. Image reading and advanced v3 manipulation
from PIL import Image as imgx
import matplotlib.image as mpimg
import numpy as array
import matplotlib.pyplot as plt

# First, load the image
filename = "Sweet Girl.jpg"

# Load the image
image = mpimg.imread(filename)

# Convert Image into calculatable numpy array
inarray = np.asarray(image)
   #inarray = np.asarray(image, dtype="float")

# Printing the array to identify image sturcture
print(inarray,"\n\n")

#Converting numpy mathematical array into image in RGB(RedGreenBlue) mode
newimg = imgx.fromarray(inarray, mode='RGB')

#Displaying the image in 2D matrix form
plt.imshow(newimg)
print("Image from matrix data- ",newimg)
plt.show()

#CODE SNIPPET__1#
# Print out its shape
#print(image.shape)
# Print out the image22
#import matplotlib.pyplot as plt
#imgplot = plt.imshow(image)
#print(imgplot)
#CODE SNIPPET__2#


# In[35]:


import numpy as np


# In[54]:


# Numpy Array to image #
from PIL import Image
import numpy as np

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[256, 256] = [255, 0, 0]
#print(data)
img = Image.fromarray(data, 'RGB')
#img.save('my.jpg')
img.show()


# In[64]:


# 7- Image Manipulation Advanced Stage V4
from PIL import Image
import numpy

# Opening image
im = Image.open("Sweet Girl.jpg")

# Image to array
np_im = numpy.array(im)
print(np_im.shape)
#print(np_im)

# Subtracting 180 from each 3x3 matrix as displayed by "print(np_im)" execution.
np_im = np_im - 180

# Converting Array to Image
new_im = Image.fromarray(np_im)
print("After calculation- ",new_im.size)

# Saving the Image, so formed
new_im.save("numpy_altered_sample2.jpg")

