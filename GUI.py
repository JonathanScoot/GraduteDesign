import skimage
import cv2

'''

class CompareImage():

    def compare_image(self, path_image1, path_image2):

        imageA = cv2.imread(path_image1)
        imageB = cv2.imread(path_image2)

        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        (score, diff) =skimage.measure.compare_ssim (grayA, grayB, full=True)
        print("SSIM: {}".format(score))
        return score


compare_image = CompareImage()
compare_image.compare_image("C:/Users/Jonathan/Desktop/1.png", "C:/Users/Jonathan/Desktop/B.png")
'''

# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments


# load the two input images
imageA = cv2.imread("C:/Users/Jonathan/Desktop/A.png")
imageB = cv2.imread("C:/Users/Jonathan/Desktop/B.png")
imageC = cv2.imread("C:/Users/Jonathan/Desktop/C.png")
imageD = cv2.imread("C:/Users/Jonathan/Desktop/D.png")

# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
grayC = cv2.cvtColor(imageC, cv2.COLOR_BGR2GRAY)
grayD = cv2.cvtColor(imageD, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score1, diff1) = compare_ssim(grayA, grayB, full=True)
(score2, diff2) = compare_ssim(grayA, grayC, full=True)
(score3, diff3) = compare_ssim(grayA, grayD, full=True)

diff1 = (diff1 * 255).astype("uint8")
diff2 = (diff2 * 255).astype("uint8")
diff3 = (diff3 * 255).astype("uint8")

print("SSIM: {}".format(score1))
print("SSIM: {}".format(score2))
print("SSIM: {}".format(score3))