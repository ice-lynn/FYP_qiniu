import time
from imutils import paths
import numpy as np
import imutils
import cv2


# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--images", type=str, required=True,
# 	help="path to input directory of images to stitch")
# ap.add_argument("-o", "--output", type=str, required=True,
# 	help="path to the output image")
# ap.add_argument("-c", "--crop", type=int, default=0,
# 	help="whether to crop out largest rectangular region")
# args = vars(ap.parse_args())

def stitch(images, crop, output):
    print("[INFO] loading images...")
    imagePaths = sorted(list(paths.list_images(images)))
    imagePaths.reverse()
    images = []

    # loop over the image paths, load each one, and add them to our
    # images to stich list
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        images.append(image)
        time.sleep(0.2)

    print(len(images))

    image_list = []
    a = 0

    while a < len(images):
        list1 = []
        for i in range(3):
            if a + i < len(images): list1.append(images[a + i])
        a = a + 2
        image_list.append(list1)

    # initialize OpenCV's image sticher object and then perform the image
    # stitching
    print("[INFO] stitching images...")
    stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()

    print(len(image_list))
    stitching = []
    for i in range(len(image_list)):
        print(i)
        (status, stitched1) = stitcher.stitch(image_list[i])
        if (status != 0):
            print('error')

        else:
            stitching.append(stitched1)

    print(len(stitching))

    (status, stitched) = stitcher.stitch(stitching)

    print('finish')

    if status == 0:
        # check to see if we supposed to crop out the largest rectangular
        # region from the stitched image
        if crop > 0:
            # create a 10 pixel border surrounding the stitched image
            print("[INFO] cropping...")
            stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10,
                                          cv2.BORDER_CONSTANT, (0, 0, 0))

            # convert the stitched image to grayscale and threshold it
            # such that all pixels greater than zero are set to 255
            # (foreground) while all others remain 0 (background)
            gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
            cv2.imshow("Stitched", thresh)
            cv2.imwrite('grey.png', thresh)

            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            c = max(cnts, key=cv2.contourArea)

            # allocate memory for the mask which will contain the
            # rectangular bounding box of the stitched image region
            mask = np.zeros(thresh.shape, dtype="uint8")
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

            minRect = mask.copy()
            sub = mask.copy()
            #
            # # keep looping until there are no non-zero pixels left in the
            # # subtracted image
            while cv2.countNonZero(sub) > 1000:
                # erode the minimum rectangular mask and then subtract
                # the thresholded image from the minimum rectangular mask
                # so we can count if there are any non-zero pixels left
                minRect = cv2.erode(minRect, None)
                sub = cv2.subtract(minRect, thresh)
            #
            cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            c = max(cnts, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(c)

            # use the bounding box coordinates to extract the our final
            # stitched image
            stitched = stitched[y:y + h, x:x + w]
        cv2.imwrite(output, stitched)

        # display the output stitched image to our screen
        cv2.imshow("Stitched", stitched)


    else:
        print("[INFO] image stitching failed ({})".format(status))
