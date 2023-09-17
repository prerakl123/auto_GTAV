# Import Modules
import time

import cv2
import numpy as np
from PIL import ImageGrab

last_time = time.time()
while True:
    # Capture the screen (800x640)
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))

    # Debugging line for execution time
    print('{} seconds'.format(time.time() - last_time))
    last_time = time.time()

    # Show the captured screen in the OpenCV window
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    # Exit config
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
