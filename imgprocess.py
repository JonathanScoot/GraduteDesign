import cv2

number = None

im = cv2.imread('C:/Users/Jonathan/Desktop/number{}.png'.format(1))
im = cv2.resize(im, (28, 28))
cv2.imwrite('C:/Users/Jonathan/Desktop/num/{}.png'.format(1), im)


