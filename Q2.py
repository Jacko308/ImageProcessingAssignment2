import cv2 as cv
import numpy as np


def main():

    # ---------------- Load image
    img = cv.imread("images/Q2/mandarine.jpg")
    if img is None:
        print("ERROR::CV::Could not read image.")
        return 1

    # Resize image
    rows, cols, channels = img.shape
    rows = rows // 4
    cols = cols // 4

    img = cv.resize(img, (cols, rows))

    cv.imshow("mandarine", img)
    # Convert image from BGR to HSV
    blurred = cv.GaussianBlur(img, (7, 7), 0)
    hsv = cv.cvtColor(blurred,cv.COLOR_BGR2HSV)

#-------------- Create masks from HSV values
    lower_1 = np.array([0,99,0])
    upper_1 = np.array([179,255,255])
    mask1 = cv.inRange(hsv, lower_1, upper_1)
    # mask1 = ~mask1
    cv.imshow('mask1', mask1)
    kernel = np.ones((2,2),np.uint8)

    #--------------- Morphological Transforms ----------------------#
    closing = cv.morphologyEx(mask1, cv.MORPH_CLOSE, kernel)
    # erodeCocopops = cv.erode(mask1,kernel,iterations = 4)
    # cv.imshow('erodeCocopops', erodeCocopops)
    # dilateCocopops = cv.dilate(erodeCocopops, kernel, iterations = 3)
    # cv.imshow('dilateCocopops', dilateCocopops)

    #-------------- Thresholding -----------#
    # ret1, thresh = cv.threshold(cocopopsleft, 240, 255, 1)
    num = 0
    contours,h  = cv.findContours(closing,1,2)
    for cnt in contours:
            area = cv.contourArea(cnt)
            # if ((area >= 270) & (area <= 1000)):
            print("contour num = {}\ncontour area = {}".format(cnt,area))
            cv.drawContours(img,[cnt],0,(0,0,255),2)
            num += 1
            cv.imshow("contour num = {}".format(num), img)
            cv.waitKey(0)
    cv.putText(img, "surface area of mandarine = " + "{}".format(area), (30, 900), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)            
    cv.imshow('Q2_result', img)
    # cv.imwrite('images/Q2/Q2_result.png', img)
    cv.waitKey(0)
    cv.destroyAllWindows()   

    return 0


if __name__ == "__main__":

    main()