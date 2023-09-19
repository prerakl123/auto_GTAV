import time

import cv2
import numpy as np

from alexnet import alexnet
from directkeys import W, press_key, release_key, A, D
from getkeys import key_check
from grabscreen import grab_screen

WIDTH = 80
HEIGHT = 60
EPOCHS = 8
LR = 1e-3
MODEL_NAME = "autogta5-car-{}-{}-{}-epochs.model".format(LR, 'alexnetv2', EPOCHS)


def straight():
    press_key(W)
    release_key(A)
    release_key(D)


def left():
    press_key(A)
    press_key(W)
    release_key(D)


def right():
    press_key(D)
    press_key(W)
    release_key(A)


model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)


def main():
    for i in range(4, 0, -1):
        print(i)
        time.sleep(1)

    paused = False
    last_time = time.time()
    while True:
        if not paused:
            screen = grab_screen(region=(0, 40, 800, 630))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (80, 60))

            print("{} seconds".format(time.time() - last_time))
            last_time = time.time()

            predictions = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])
            moves = list(np.around(predictions))
            print(moves, predictions)

            if moves == [1, 0, 0]:
                left()
            elif moves == [0, 1, 0]:
                straight()
            elif moves == [0, 0, 1]:
                right()

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                release_key(A)
                release_key(W)
                release_key(D)
                time.sleep(1)


main()
