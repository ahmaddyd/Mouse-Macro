author = "amad"

import pyautogui
import pydirectinput
import random
import time


def testing():
    return random.randint(1, 100)


def testing1():
    return random.randint(1, 75)


def testing2():
    return random.randint(1, 5)


def no_respond():
    return time.sleep(testing2())


def mm():
    pydirectinput.move(testing(), testing1(), duration=testing2())
    no_respond()


while True:
    mm()