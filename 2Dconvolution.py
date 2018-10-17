#2D CONVOLUTION

import cv2
import numpy as np

imge = cv2.imread('lena_gray.jpg').astype(float)/255.0
print(imge.shape) #(512, 512, 3)
img = cv2.copyMakeBorder(imge,1,1,1,1,cv2.BORDER_REFLECT)
print(img.shape)  #(514, 514, 3)


rows = img.shape[0]
cols = img.shape[1]
x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
Gx = np.zeros((rows-2, cols-2,3))
Gy = np.zeros((rows-2, cols-2,3))
G = np.zeros((rows-2, cols-2,3))

timestart = time.clock()

for m in range(1, rows-1):
    for n in range(1, cols-1):
        gx = (x[0][0] * img[m-1][n-1]) + (x[0][1] * img[m-1][n]) + (x[0][2] * img[m-1][n+1]) +\
             (x[1][0] * img[m][n-1])   + (x[1][1] * img[m][n])   + (x[1][2] * img[m][n+1])   +\
             (x[2][0] * img[m+1][n-1]) + (x[2][1] * img[m+1][n]) + (x[2][2] * img[m+1][n+1])
        Gx[m-1][n-1] = gx
        gy = (y[0][0] * img[m-1][n-1]) + (y[0][1] * img[m-1][n]) + (y[0][2] * img[m-1][n+1]) +\
             (y[1][0] * img[m][n-1])   + (y[1][1] * img[m][n])   + (y[1][2] * img[m][n+1])   +\
             (y[2][0] * img[m+1][n-1]) + (y[2][1] * img[m+1][n]) + (y[2][2] * img[m+1][n+1])
        Gy[m-1][n-1] = gy
        g =  ((gx ** 2) + (gy ** 2)) ** 0.5
        G[m-1][n-1] = g 

cv2.imshow('Gx-2D',Gx)
cv2.imshow('Gy-2D',Gy)
cv2.imshow('G-2D',G)
print(G.shape)   #(512, 512, 3)
cv2.waitKey(0) 
cv2.destroyAllWindows()
