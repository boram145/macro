"""
Author:양보람
2021.06.16.
고양시 사진 다운받는 프로그램
"""

import time
import pywinmacro as pw

location=(568, 255)
location2=(709, 299)
location3=(726, 484)
location4=(879, 177)

def scrap():
    pw.click(location)
    pw.key_press_once("tab")
    pw.type_in("고양이")
    time.sleep(0.1)
    pw.key_press_once("enter")
    time.sleep(2)
    for i in range(12):
        pw.key_press_once("tab")
        time.sleep(0.1)
    pw.key_press_once("enter")
    time.sleep(3)
    for i in range(30):
        pw.key_press_once("tab")
    time.sleep(0.1)
    pw.key_press_once("enter")
    time.sleep(3)
    downloads()


def downloads():
 while True:
     pw.right_click(location2)
     time.sleep(0.5)
     pw.click(location3)
     time.sleep(1)
     pw.key_press_once("enter")
     time.sleep(3)
     pw.click(location4)
     time.sleep(3)


