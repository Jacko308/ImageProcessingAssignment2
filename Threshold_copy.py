import cv2 as cv
import numpy as np


def main():

    # ---------------- Load image

    img = cv.imread("data/cocopops.jpg")

    # if img is None:
    #     print("ERROR::CV::Could not read image.")
    #     return 1

    # Resize image

    rows, cols, channels = img.shape
    
    rows = rows // 4
    cols = cols // 4

    img = cv.resize(img, (cols, rows))

    cv.imshow("cocopops", img)
    cv.imwrite('../images/01/01.PNG', img)

    # Convert image from BGR to grayscale

    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

#-------------- Create masks from HSV values
    lower_1 = np.array([0,99,40])
    upper_1 = np.array([179,255,255])
    mask1 = cv.inRange(hsv, lower_1, upper_1)
    cv.imshow('mask1', mask1)
    kernel = np.ones((3,3),np.uint8)

    #--------------- Morphological Transforms ----------------------#
    erodeCocopops = cv.erode(mask1,kernel,iterations = 1)
    cv.imshow('erodeCocopops', erodeCocopops)
    dilateCocopops = cv.dilate(erodeCocopops, kernel, iterations = 3)
    # blurred = cv.GaussianBlur(img, (7, 7), 0)

    # background = dilateCocopops

    # # #-------------- Operations -------------#
    # cocopopsleft = img - background
    # cv.imshow('cocopopsleft', cocopopsleft)
    # cv.waitKey(0)
    #-------------- Thresholding -----------#
    # ret1, thresh = cv.threshold(cocopopsleft, 240, 255, 1)

    contours,h  = cv.findContours(dilateCocopops,1,2)
    for cnt in contours:
            area = cv.contourArea(cnt)
            if ((area > 200) & (area <= 8000)):
            
                print("contour num = ")
                print(cnt)
                print("contour area = ")
                print(area)
                cv.drawContours(img,[cnt],0,(0,0,255),3)
    
    cv.imshow('img001', img)

    cv.waitKey(0)

    # Generate histogram
    # plt.hist(img.ravel(), 256, [0, 256])
    # plt.savefig("data/threshold_histogram.png")
    # plt.savefig("02.PNG")
    # plt.show()
    cv.waitKey(1)
    cv.destroyAllWindows()   

    return 0


if __name__ == "__main__":

    main()