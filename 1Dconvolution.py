#1D CONVOLUTION

import cv2
import numpy as np

imge = cv2.imread('lena_gray.jpg').astype(float)/255.0
print(imge.shape) #(512, 512, 3)
img = cv2.copyMakeBorder(imge,1,1,1,1,cv2.BORDER_REFLECT)
print(img.shape)  #(514, 514, 3)


rows = img.shape[0]
cols = img.shape[1]
x_h = np.array([[-1,0,1]])
x_v = np.array([[1],[2],[1]])    
y_h = np.array([[1,2,1]])
y_v = np.array([[-1],[0],[1]])
Gx = np.zeros((rows-2, cols-2,3))
Gy = np.zeros((rows-2, cols-2,3))
G = np.zeros((rows-2, cols-2,3))


for m in range(1,rows-1):
    for n in range(1,cols-1):
        gx = x_v[0][0] * img[m-1][n] + x_v[1][0] * img[m][n] + x_v[2][0] * img[m+1][n]
        Gx[m-1][n-1] = gx
        gy = y_v[0][0] * img[m-1][n] + y_v[1][0] * img[m][n] + y_v[2][0] * img[m+1][n] 
        Gy[m-1][n-1] = gy

Gx = cv2.copyMakeBorder(Gx,1,1,1,1,cv2.BORDER_REFLECT)
Gy = cv2.copyMakeBorder(Gy,1,1,1,1,cv2.BORDER_REFLECT)

for m in range(1,rows-1):
    for n in range(1,cols-1):
        gx = x_h[0][0] * Gx[m][n-1] + x_h[0][1] * Gx[m][n] + x_h[0][2] * Gx[m][n+1]
        Gx[m-1][n-1] = gx
        gy = y_h[0][0] * Gy[m][n-1] + y_h[0][1] * Gy[m][n] + y_h[0][2] * Gy[m][n+1]     
        Gy[m-1][n-1] = gy

        g =  ((gx ** 2) + (gy ** 2)) ** 0.5
        G[m-1][n-1] = g
        

cv2.imshow('Gx-1D',Gx)
cv2.imshow('Gy-1D',Gy)
cv2.imshow('G-1D',G)
print(G.shape)  #(512, 512, 3)
cv2.waitKey(0) 
cv2.destroyAllWindows()
