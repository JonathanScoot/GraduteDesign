import cv2

number = None

for number in range(10):
    im = cv2.imread('C:/Users/Jonathan/Desktop/number/{}.png'.format(number))
    im = cv2.resize(im, (28, 28))
    cv2.imwrite('C:/Users/Jonathan/Desktop/num/{}.png'.format(number), im)

