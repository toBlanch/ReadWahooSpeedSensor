import pytesseract
from PIL import Image
import pyautogui
from time import sleep
import pyautogui


region = (830, 840, 180, 100)
videoRunning = False
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

while True:
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("screenshot.png")

    text = 0
    print(pytesseract.image_to_string(screenshot))
    stringText = pytesseract.image_to_string(screenshot).replace("...", "").replace("MPH", "").strip()
    print(stringText)
    try:
        text = float(stringText)
        if text > 1:
            if not videoRunning:
                pyautogui.press('playpause')
                videoRunning = True

            if text < 4:
                pyautogui.hotkey('ctrl', 'shift', 'h')
            elif text < 5:
                pyautogui.hotkey('ctrl', 'shift', 'j')
            elif text < 6:
                pyautogui.hotkey('ctrl', 'shift', 'k')
            else:
                pyautogui.hotkey('ctrl', 'shift', 'l')
        elif videoRunning:
            pyautogui.press('playpause') 
            videoRunning = False
    except ValueError:
        print("Not a float")

    sleep(1)