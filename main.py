
import pyautogui
import pytesseract
import cv2
import mss
import mss.tools
import time
from fuzzywuzzy import fuzz

monWidth = 1280
monHeight = 800
x1 = monWidth - monWidth/4
y1 = monHeight - monHeight/4
width = monWidth/4
height = monHeight/4
monitor = {"top": int(y1), "left": int(x1), "width": int(width), "height": int(height)}

print("starting")

while True:
    with mss.mss() as sct:
        output = "subtitles.png"
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
       

    img = cv2.imread("subtitles.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    configf = r"--oem 3 --psm 6"
    text = pytesseract.image_to_string(img, config=configf)
    matching = fuzz.ratio(text, "Fishing Bobber splashes")
    print(text + matching)
    if matching > 50:
        print("something found")
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(2)
        

    time.sleep(0.2)