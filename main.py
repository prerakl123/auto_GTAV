# Import Modules
import time

import cv2
import numpy as np
from PIL import ImageGrab


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img


last_time = time.time()
while True:
    # Capture the screen (800x640)
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
