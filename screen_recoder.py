from turtle import width
import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dim = (width, height)

f = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("test.mp4", f, 20.0, dim)

now_time = time.time()

dur = 10

end_time = now_time + dur

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    if time.time() > end_time:
        break

out.release()
cv2.destroyAllWindows()
print("Done")    