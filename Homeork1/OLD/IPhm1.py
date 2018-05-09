import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

g1=0.4
g2=1.7

IMG=cv2.imread('photo.jpg',cv2.IMREAD_GRAYSCALE)

##Find width and height of Image
height,width = IMG.shape[:2]

##Declare histogram data structure type for the original and 2 transform image
IMG_H=[0 for x in range(256)]
I=[0 for x in range(256)]
PT1_H=[0 for x in range(256)]
P1=[0 for x in range(256)]
PT2_H=[0 for x in range(256)]
P2=[0 for x in range(256)]

##Convert 2D array to 1D
IMG_F=IMG.flatten()
##Declare PT1 nad PT2 array
PT1_F=np.arange(width*height)
PT2_F=np.arange(width*height)



##Power Transformation
for j in range (0,height*width):
    if((IMG_F[j]*g1)>255):
        PT1_F[j]=255
    else:
        PT1_F[j]=IMG_F[j]*g1
    if((IMG_F[j]*g2)>255):
        PT2_F[j]=255
    else:
        PT2_F[j]=IMG_F[j]*g2

##Histogram graypixel Frquency
for i in range(0,width*height):
    IMG_H[round(IMG_F[i])]+=1
    PT1_H[round(PT1_F[i])]+=1
    PT2_H[round(PT2_F[i])]+=1

##Accumulative Frequency
I[0]=IMG_H[0]
P1[0]=PT1_H[0]
P2[0]=PT2_H[0]
for i in range (1,256):
    I[i]=I[i-1]+IMG_H[i]
    P1[i]=P1[i-1]+PT1_H[i]
    P2[i]=P2[i-1]+PT2_H[i]


bins=np.linspace(0,255,256)
bar_width=0.35
f,ax=plt.subplots(1)
plt.xlabel('Levels')
plt.ylabel('Acumulative Frequency')
ax.plot(bins,I,color='red',label='Original')
ax.plot(bins,P1,color='blue',label='Darker')
ax.plot(bins,P2,color='green',label='Lighter')
plt.legend(loc='upper right')
plt.title('Accumulative frequency')
ax.set_ylim(ymin=0)
plt.show(f)

cv2.imwrite('o.png',IMG)
cv2.imwrite('gray.png',np.reshape(PT1_F,(-1,width)))
cv2.imwrite('light.png',np.reshape(PT2_F,(-1,width)))
print("Complete")