# Import Modules
import time

import cv2
import numpy as np
from PIL import ImageGrab


def roi(img, vertices):
    """
    Region of interest for the image for lanes

    :param img: input frame
    :param vertices: a tuple of desired vertices
    :return: masked roi image
    """
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(original_image):
    """
    Grayscaling the image and detecting edges.

    :param original_image: original RGB image
    :return: greyscaled edge detected image
    """
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)

    vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]])
    processed_img = roi(processed_img, [vertices])
    return processed_img


last_time = time.time()
while True:
    # Capture the screen (0, 40, 800, 640)
    screen = np.array(ImageGrab.grab(bbox=(0, 177, 941, 708)))
    new_screen = process_img(original_image=screen)

    # Debugging line for execution time
    print('{} seconds'.format(time.time() - last_time))
    last_time = time.time()

    # Show the captured screen in the OpenCV window
    cv2.imshow('window', new_screen)
    # cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    # Exit config
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
