import time

import cv2

from alexnet import alexnet
from directkeys import WINKEY_W, press_key, release_key, WINKEY_A, WINKEY_D, WINKEY_S
from getkeys import key_check
from grabscreen import grab_screen

WIDTH = 400
HEIGHT = 315
EPOCHS = 10
LR = 1e-3
MODEL_NAME = "autogta5-car-{}-{}-{}-epochs.model".format(LR, 'alexnetv2', EPOCHS)
t_time = 0.09

TUPLEKEY_W = [1, 0, 0, 0, 0, 0, 0, 0, 0]
TUPLEKEY_S = [0, 1, 0, 0, 0, 0, 0, 0, 0]
TUPLEKEY_A = [0, 0, 1, 0, 0, 0, 0, 0, 0]
TUPLEKEY_D = [0, 0, 0, 1, 0, 0, 0, 0, 0]
TUPLEKEY_WA = [0, 0, 0, 0, 1, 0, 0, 0, 0]
TUPLEKEY_WD = [0, 0, 0, 0, 0, 1, 0, 0, 0]
TUPLEKEY_SA = [0, 0, 0, 0, 0, 0, 1, 0, 0]
TUPLEKEY_SD = [0, 0, 0, 0, 0, 0, 0, 1, 0]
TUPLEKEY_NK = [0, 0, 0, 0, 0, 0, 0, 0, 1]


def straight():
    press_key(WINKEY_W)
    release_key(WINKEY_A)
    release_key(WINKEY_D)
    release_key(WINKEY_S)


def left():
    press_key(WINKEY_A)
    release_key(WINKEY_W)
    release_key(WINKEY_D)
    release_key(WINKEY_S)


def right():
    press_key(WINKEY_D)
    release_key(WINKEY_A)
    release_key(WINKEY_W)
    release_key(WINKEY_S)


def reverse():
    press_key(WINKEY_S)
    release_key(WINKEY_A)
    release_key(WINKEY_W)
    release_key(WINKEY_S)


def forward_left():
    press_key(WINKEY_W)
    press_key(WINKEY_A)
    release_key(WINKEY_D)
    release_key(WINKEY_S)


def forward_right():
    press_key(WINKEY_W)
    press_key(WINKEY_D)
    release_key(WINKEY_A)
    release_key(WINKEY_S)


def reverse_left():
    press_key(WINKEY_S)
    press_key(WINKEY_A)
    release_key(WINKEY_W)
    release_key(WINKEY_D)


def reverse_right():
    press_key(WINKEY_S)
    press_key(WINKEY_D)
    release_key(WINKEY_W)
    release_key(WINKEY_A)


def no_keys():
    release_key(WINKEY_W)
    release_key(WINKEY_A)
    release_key(WINKEY_S)
    release_key(WINKEY_D)


model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)


def main():
    for i in range(4, 0, -1):
        print(i)
        time.sleep(1)

    paused = False
    # last_time = time.time()
    while True:
        if not paused:
            screen = grab_screen(region=(0, 40, 800, 630))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (400, 315))

            # print("{} seconds".format(time.time() - last_time))
            last_time = time.time()

            predictions = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]
            turn_thresh = .75
            fwd_thresh = .7
            # print("Moves:", moves, type(moves), "Predictions:", *predictions)

            if predictions[0] > turn_thresh:
                left()
            elif predictions[1] > fwd_thresh:
                straight()
            elif predictions[2] > turn_thresh:
                right()
            else:
                straight()

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                release_key(WINKEY_A)
                release_key(WINKEY_W)
                release_key(WINKEY_D)
                time.sleep(1)


main()
