# Import Modules
import os
import time

import cv2
import numpy as np

from getkeys import key_check
# from directkeys import press_key, release_key, WINKEY_W, WINKEY_A, WINKEY_D
# from draw_lanes import draw_lanes
from grabscreen import grab_screen


def keys_to_output(keys):
    output = [0, 0, 0]  # [WINKEY_A, WINKEY_W, WINKEY_D]
    if 'WINKEY_A' in keys:
        output[0] = 1
    elif 'WINKEY_D' in keys:
        output[2] = 1
    else:
        output[1] = 1

    return output


file_name = 'training_data.npy'
if os.path.isfile(file_name):
    print("Loading previous data...")
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print("File does not exist. Starting Afresh...")
    training_data = []


# def draw_lines(img, lines):
#     try:
#         for line in lines:
#             coords = line[0]
#             cv2.line(
#                 img,
#                 pt1=(coords[0], coords[1]),
#                 pt2=(coords[2], coords[3]),
#                 color=[255, 255, 255],
#                 thickness=3
#             )
#     except TypeError:
#         pass
#
#
# def roi(img, vertices):
#     """
#     Region of interest for the image for lanes
#
#     :param img: input frame
#     :param vertices: a tuple of desired vertices
#     :return: masked roi image
#     """
#     # blank mask
#     mask = np.zeros_like(img)
#     # filling pixels inside the polygon
#     cv2.fillPoly(mask, vertices, 255)
#     # image where mask pixels are non-zero
#     masked = cv2.bitwise_and(img, mask)
#     return masked
#
#
# def process_img(image):
#     """
#     Grayscaling the image and detecting edges.
#
#     :param image: input image
#     :returns: processed image, original image and m1 & m2
#     """
#     orig_image = image
#     # convert to gray
#     processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # edge detection
#     processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
#     # add blur
#     processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)
#
#     vertices = np.array(
#         [[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]],
#         np.int32
#     )
#
#     processed_img = roi(processed_img, [vertices])
#
#     lines = cv2.HoughLinesP(
#         processed_img,
#         rho=1,
#         theta=np.pi / 180,
#         threshold=180,
#         minLineLength=20,
#         maxLineGap=15
#     )
#     _m1 = 0
#     _m2 = 0
#
#     try:
#         l1, l2, _m1, _m2 = draw_lanes(lines)
#         cv2.line(
#             orig_image,
#             pt1=(l1[0], l1[1]),
#             pt2=(l1[2], l1[3]),
#             color=[0, 255, 0],
#             thickness=30
#         )
#         cv2.line(
#             orig_image,
#             pt1=(l2[0], l2[1]),
#             pt2=(l2[2], l2[3]),
#             color=[0, 255, 0],
#             thickness=30
#         )
#     except Exception as e:
#         print(str(e))
#
#     try:
#         for coords in lines:
#             coords = coords[0]
#             try:
#                 cv2.line(
#                     processed_img,
#                     pt1=(coords[0], coords[1]),
#                     pt2=(coords[2], coords[3]),
#                     color=[255, 0, 0],
#                     thickness=3
#                 )
#             except Exception as e:
#                 print(str(e))
#
#     except Exception as e:
#         pass
#
#     return processed_img, orig_image, _m1, _m2
#
#
# def straight():
#     press_key(WINKEY_W)
#     release_key(WINKEY_A)
#     release_key(WINKEY_D)
#
#
# def left():
#     press_key(WINKEY_A)
#     release_key(WINKEY_W)
#     release_key(WINKEY_D)
#     release_key(WINKEY_A)
#
#
# def right():
#     press_key(WINKEY_D)
#     release_key(WINKEY_A)
#     release_key(WINKEY_W)
#     release_key(WINKEY_D)
#
#
# def slow():
#     release_key(WINKEY_A)
#     release_key(WINKEY_A)
#     release_key(WINKEY_D)

for i in range(4, 0, -1):
    print(i)
    time.sleep(1)

last_time = time.time()
while True:
    # Capture the screen (0, 40, 800, 640)
    screen = grab_screen(region=(0, 40, 800, 630))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen = cv2.resize(screen, (400, 315))
    keys = key_check()
    output = keys_to_output(keys)
    training_data.append([screen, output])

    # Debugging line for execution time
    # print('{} seconds'.format(time.time() - last_time))
    last_time = time.time()

    if len(training_data) % 500 == 0:
        print(len(training_data))
        np.save(file_name, np.array(training_data, dtype=object), allow_pickle=True)

    # # Processing the input image
    # new_screen, original_image, m1, m2 = process_img(screen)
    #
    # # Show the captured screen in the OpenCV window
    # cv2.imshow('window2', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    #
    # # Auto-Driving
    # if m1 < 0 and m2 < 0:
    #     right()
    # elif m1 > 0 and m2 > 0:
    #     left()
    # else:
    #     straight()

    # Exit config
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
