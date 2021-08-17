import cv2 as cv
import numpy as np


def main():

    # ---------------- Load image ---------------------------------#
    img = cv.imread("images/Q4/nut_bolt1.jpg")
    if img is None:
        print("ERROR::CV::Could not read image.")
        return 1

    # ---------------- Resize image -------------------------------#
    rows, cols, channels = img.shape
    rows = rows // 4
    cols = cols // 4

    img = cv.resize(img, (cols, rows))

    cv.imshow("nuts + bolts", img)
    # ---------------- Convert image from BGR to HSV --------------#
    blurred = cv.GaussianBlur(img, (3, 3), 0)
    hsv = cv.cvtColor(blurred,cv.COLOR_BGR2HSV)

    #---------------- Create masks from HSV values ----------------#
    bolt_lower = np.array([0,0,0])
    bolt_upper = np.array([180,255,42])
    bolt_mask = cv.inRange(hsv, bolt_lower, bolt_upper)
    cv.imshow('bolt_mask', bolt_mask)


    lower_1 = np.array([0,0,114])
    upper_1 = np.array([179,255,172])
    mask1 = cv.inRange(hsv, lower_1, upper_1)
    cv.imshow('mask1', mask1)
    kernel = np.ones((2,2),np.uint8)

    #--------------- Morphological Transforms ----------------------#
    cal_closing = cv.morphologyEx(bolt_mask, cv.MORPH_CLOSE, kernel)
    closing = cv.morphologyEx(mask1, cv.MORPH_CLOSE, kernel)

    #--------------- Find Contours ---------------------------------#
    bolt_num = 0 
    nut_num = 0

    contours,h  = cv.findContours(closing,1,2)
    cal_contours,h  = cv.findContours(cal_closing,1,2)

    for cal_cnt in cal_contours:
        cal_area = cv.contourArea(cal_cnt)
        if ((cal_area >= 300) & (cal_area <= 440)): #get bolts
            print("cal_ contour area = {}".format(cal_area))
            cv.drawContours(img,[cal_cnt],0,(0,0,255),2)
            bolt_num += 1
            cv.imshow("contour num = {}".format(bolt_num), img)
            cv.waitKey(0)
    
    cv.putText(img, "num of bolts = " + "{0:.1f}".format(bolt_num), (30, 800), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
    cv.imshow('num of bolts', img)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if ((area >= 1470) & (area <= 3000)): 
            # print("contour area = {}".format(area))
            cv.drawContours(img,[cnt],0,(255,0,10),2)
            nut_num += 1
            cv.imshow("contour num = {}".format(nut_num), img)
            cv.waitKey(0)

    cv.putText(img, "num of nuts = " + "{0:.1f}".format(nut_num), (30, 700), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)            

    cv.imshow('Q4_result', img)
    cv.imwrite('images/Q4/Q4_result.png', img)

    cv.waitKey(0)
    cv.destroyAllWindows()   

    return 0


if __name__ == "__main__":

    main()