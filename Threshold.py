import cv2 as cv
import numpy as np


def main():

    # ---------------- Load image ----------------- #

    img = cv.imread("data/Wire_Straight.jpg")

    # Resize image
    rows, cols, channels = img.shape
    rows = rows // 4
    cols = cols // 4

    img = cv.resize(img, (cols, rows))

    cv.imshow("Straight Wire", img)
   
    # ---- Convert image from BGR to grayscale

    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel = np.ones((3,3),np.uint8)


    #-------------- Thresholding -----------#
    ret1, thresh = cv.threshold(gray_img, 80, 255, cv.THRESH_BINARY_INV)
    cv.imshow('Binary Threshold', thresh)

    num = 0
    contours,h  = cv.findContours(thresh.copy(),cv.RETR_EXTERNAL,2)
    for cnt in contours:
            area = cv.contourArea(cnt)
            # if ((area >= 270) & (area <= 1000)):
            print("contour num = {}\ncontour area = {}".format(cnt,area))
            cv.drawContours(img,[cnt],0,(0,0,255),1)
            num += 1
            cv.imshow("contour num = {}".format(num), img)
            cv.waitKey(0)
    # cv.putText(img, "Number of single Cocopops = " + "{}".format(num), (30, 700), cv.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 0), 2)            
    cv.imshow('img001', img)
    cv.waitKey(0)
    cv.destroyAllWindows()   

    return 0


if __name__ == "__main__":

    main()