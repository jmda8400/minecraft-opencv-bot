import pyautogui
import pydirectinput
import time
import keyboard
import cv2
import numpy as np
import random

path = r'D:\Juan Manuel\Documents\PycharmProjects\Face Recognition\main\pictures\raw_picture.jpg'

def looking_for_trees():
    terminated = False
    while not terminated:
        img = pyautogui.screenshot(path)
        final_img = cv2.imread(path)

            # Convert BGR to HSV
        hsv = cv2.cvtColor(final_img, cv2.COLOR_BGR2HSV)

            # define range of X color in HSV
        lower = np.array([16, 20, 20])
        upper = np.array([20, 255, 200])

            # Threshold the HSV image to get only X colors
        mask = cv2.inRange(hsv, lower, upper)

            # Create new res and mask for further investigacion
        cv2.imwrite('.\main\pictures\Mask.png', mask)

            # 'For' cycle
        contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 30000):
                print("Tree found")
                approach_tree(area)
            else:
                print("Nothing")
        if keyboard.is_pressed("u"):
            terminated = True
        print("Test trees")
        walk()

def walk():
    pydirectinput.keyDown("w")

def approach_tree(local_area):
    if (local_area > 40000):
        if (local_area > 70000):
            pydirectinput.keyUp("w")
            chop_down_tree(local_area)
    else:
        print("Nothing yet...")
        pyautogui.move(-60, 0, 0)
        time.sleep(1)
        if (local_area > 70000):
            pydirectinput.keyUp("w")
            chop_down_tree(local_area)
        else:
            pyautogui.move(120, 0, 0)

def chop_down_tree(local_area):
    if (local_area) > 100000:
        pydirectinput.mouseDown()
        time.sleep(2)
        pydirectinput.mouseUp()
        pyautogui.move(0, 180, 0)
        pydirectinput.mouseDown()
        time.sleep(2)
        pydirectinput.mouseUp()
        pyautogui.move(0, -320, 0)
        pydirectinput.mouseDown()
        time.sleep(2)
        pydirectinput.mouseUp()
        pyautogui.move(0, 180, 0)

    k = random.randint(0, 1)
    if (k == 1):
        pyautogui.move(60, 0, 0)
    else:
        pyautogui.move(-60, 0, 0)

looking_for_trees()
print("Goodbye =)")