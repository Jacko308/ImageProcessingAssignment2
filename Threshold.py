import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():

    # Load image

    img = cv.imread("data/cocopops.jpg", 0)

    if img is None:
        print("ERROR::CV::Could not read image.")
        return 1

    # Resize image

    rows, cols = img.shape
    
    rows = rows // 2
    cols = cols // 2

    img = cv.resize(img, (cols, rows))

    cv.imshow("cocopops", img)
    cv.imwrite('../images/01/01.PNG', img)

    # Convert image from BGR to grayscale

    # gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #--------------- Morphological Transforms ----------------------#
    kernel = np.ones((5,5),np.uint8)
    erodeCocopops = cv.erode(img,kernel,iterations = 5)
    dilateCocopops = cv.dilate(erodeCocopops, kernel, iterations = 5)
    blurred = cv.GaussianBlur(img, (7, 7), 0)

    background = dilateCocopops

    #-------------- Operations -------------#
    cocopopsleft = img - background
    cv.imshow('cocopopsleft', cocopopsleft)
    cv.waitKey(0)
    #-------------- Thresholding -----------#
    ret1, th1 = cv.threshold(cocopopsleft,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    #thresh = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 21, 6)
    # cv.imshow("Thresh_cocopops", ret1)
    #cv.imshow("gaussian Adaptive Thresholding", thresh)

    ret1, contours = cv.findContours(ret1, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    maxS = -1
    for cnt in contours:
            tempS = cv.contourArea(cnt)
            if maxS < tempS:
                maxS = tempS
                maxC = tempC = cv.arcLength(cnt,True)
                contour = cnt
    
    cv.drawContours(img, [contour], -1, (0,0,255,),1)
    cv.imshow('cocopopsleft2', cocopopsleft)
    cv.imshow('img', img)
    print('Maximum area: ', maxS)
    print('Corresponding to the perimeter of the rice grain: ', maxC)



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