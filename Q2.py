import cv2 as cv
import numpy as np


def main():

    # ---------------- Load image ---------------------------------#
    img = cv.imread("images/Q2/mandarin_calsq.jpg")
    if img is None:
        print("ERROR::CV::Could not read image.")
        return 1

    # ---------------- Resize image -------------------------------#
    rows, cols, channels = img.shape
    rows = rows // 4
    cols = cols // 4

    img = cv.resize(img, (cols, rows))

    cv.imshow("mandarine", img)
    # ---------------- Convert image from BGR to HSV --------------#
    blurred = cv.GaussianBlur(img, (3, 3), 0)
    hsv = cv.cvtColor(blurred,cv.COLOR_BGR2HSV)

    #---------------- Create masks from HSV values ----------------#
    cal_lower = np.array([0,0,59])
    cal_upper = np.array([180,255,255])
    cal_mask = cv.inRange(hsv, cal_lower, cal_upper)
    cal_mask = ~cal_mask
    cv.imshow('cal_mask1', cal_mask)


    lower_1 = np.array([0,106,0])
    upper_1 = np.array([179,255,255])
    mask1 = cv.inRange(hsv, lower_1, upper_1)
    # mask1 = ~mask1
    cv.imshow('mask1', mask1)
    kernel = np.ones((2,2),np.uint8)

    #--------------- Morphological Transforms ----------------------#
    cal_closing = cv.morphologyEx(cal_mask, cv.MORPH_CLOSE, kernel)
    closing = cv.morphologyEx(mask1, cv.MORPH_CLOSE, kernel)

    #--------------- Find Contours ---------------------------------#
    cal_num = 0 
    num = 0

    contours,h  = cv.findContours(closing,1,2)
    cal_contours,h  = cv.findContours(cal_closing,1,2)
    known_cal_square_size = 400 #20mm x 20mm

    for cal_cnt in cal_contours:
        cal_area = cv.contourArea(cal_cnt)
        if ((cal_area >= 400) & (cal_area <= 7000)): #get square
            print("cal_ contour area = {}".format(cal_area))
            cv.drawContours(img,[cal_cnt],0,(0,0,255),2)
            cal_num += 1
            # ----------------- pixel size calculation
            print('cal area = {}'.format(cal_area))
            cal_value = (cal_area / known_cal_square_size)
            print('cal value = {}'.format(cal_value))
            print('Area of square = {}'.format(cal_area/cal_value)) #pix area to mm2
            cv.imshow("contour num = {}".format(cal_num), img)
            cv.waitKey(0)
    
    
    for cnt in contours:
        area = cv.contourArea(cnt)
        # if ((area >= 270) & (area <= 1000)): 
        print("contour area = {}".format(area))
        cv.drawContours(img,[cnt],0,(0,0,255),2)
        num += 1
        mandarin_area = area / cal_value
        cv.imshow("contour num = {}".format(num), img)
        cv.waitKey(0)

    cv.putText(img, "surface area of mandarine = " + "{0:.1f}".format(mandarin_area), (30, 700), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)            
    cv.imshow('Q2_resultV2', img)
    cv.imwrite('images/Q2/Q2_result.png', img)

    cv.waitKey(0)
    cv.destroyAllWindows()   

    return 0


if __name__ == "__main__":

    main()