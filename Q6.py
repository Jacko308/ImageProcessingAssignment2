import cv2 as cv
import numpy as np

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv.LUT(image, table)


def main():

    # ---------------- Load image ---------------------------------#
    img = cv.imread("images/Q6/Text2.jpg")
    if img is None:
        print("ERROR::CV::Could not read image.")
        return 1

    # ---------------- Resize image -------------------------------#
    rows, cols, channels = img.shape
    rows = rows // 4
    cols = cols // 4

    img = cv.resize(img, (cols, rows))

    cv.imshow("text", img)
    cv.waitKey(0)

    new_image = np.zeros(img.shape, img.dtype)
    alpha = 1.0 # Simple contrast control
    beta = 0    # Simple brightness control
    # Initialize values
    print(' Basic Linear Transforms ')
    print('-------------------------')
    try:
        alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
        beta = int(input('* Enter the beta value [0-100]: '))
    except ValueError:
        print('Error, not a number')
    # Do the operation new_image(i,j) = alpha*image(i,j) + beta
    # Instead of these 'for' loops we could have used simply:
    new_image = cv.convertScaleAbs(img, alpha=alpha, beta=beta)
    # but we wanted to show you how to access the pixels :)
    # for y in range(img.shape[0]):
    #     for x in range(img.shape[1]):
    #         for c in range(img.shape[2]):
    #             new_image[y,x,c] = np.clip(alpha*img[y,x,c] + beta, 0, 255)
    cv.imshow('Original Image', img)
    cv.imshow('New Image', new_image)
    # Wait until user press some key
    cv.waitKey()

    # loop over various values of gamma
    for gamma in np.arange(0.0, 1.5, 0.1):
	# ignore when gamma is 1 (there will be no change to the image)
        if gamma == 1:
            continue
        # apply gamma correction and show the images
        gamma = gamma if gamma > 0 else 0.1
        adjusted = adjust_gamma(img, gamma=gamma)
        cv.putText(adjusted, "g={}".format(gamma), (10, 30),
            cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        cv.imshow("Images", np.hstack([img, adjusted]))
        cv.waitKey(0)
    gamma = 0.6
    gadjust = adjust_gamma(img, gamma=gamma)
    cv.imshow('gamma adjusted', gadjust)
    thresh = cv.threshold(gadjust,127, 255, cv.THRESH_BINARY )
    cv.imshow('thresh', thresh)
    cv.waitKey(0)
    cv.destroyAllWindows()   

    return 0


if __name__ == "__main__":

    main()