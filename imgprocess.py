import cv2
import imutils
im = cv2.imread('C:/Users/Jonathan/Desktop/1.png')
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im = cv2.resize(im, (28, 28))

cv2.imwrite('C:/Users/Jonathan/Desktop/num/1.png', im)