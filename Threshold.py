import cv2 as cv
import numpy as np
import imutils

def main():

    # ---------------- Load image ----------------- #

    img = cv.imread("data/Wire_Straight.jpg")

    # Resize image
    rows, cols, channels = img.shape
    rows = rows // 3
    cols = cols // 3
    img = cv.resize(img, (cols, rows))
    print('h, w col: ', img.shape)
    print('width:', sum((img > 60).any(axis=0)))
    print('height:', sum((img > 60).any(axis=1)))

    cv.imshow("Straight Wire", img)
   
    # ---- Convert image from BGR to grayscale
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel = np.ones((5,5),np.uint8)
    blurred = cv.GaussianBlur(gray_img, (5,5), 0)

    #-------------- Thresholding -----------#
    thresh = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY)[1]
    cv.imshow('Binary Threshold', thresh)

    num = 0
    contours,h  = cv.findContours(thresh.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE) #2
    # contours = contours[0] if len(contours) == 2 else contours[1]
    # contours = imutils.grab_contours(contours) 

    # for cnt in contours:
    #     area = cv.contourArea(cnt)
    #     M = cv.moments(cnt)
    #     cX = int(M["m10"] / M["m00"])
    #     cY = int(M["m01"] / M["m00"])
    #     # if ((area >= 270) & (area <= 1000)):
    #     # print("contour num = {}\ncontour area = {}".format(cnt,area))
    #     cv.drawContours(img,[cnt],0,(0,0,255),1)
    #     cv.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    #     cv.putText(img, "center", (cX - 20, cY - 20),
    #     cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    #     num += 1
    #     cv.imshow("contour num = {}".format(num), img)
    #     cv.waitKey(0)
    # # cv.line(img, cnt[2], cnt[3], (0,255,0), 1)
    # cv.imshow('line added to image', img)
    # cv.waitKey(0)
    # cv.putText(img, "Length of wire = " + "{}".format(num), (30, 700), cv.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 0), 2)            
    cv.imshow('final image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()   

    return 0


if __name__ == "__main__":

    main()