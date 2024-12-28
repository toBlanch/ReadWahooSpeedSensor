import wahooCore
import asyncio
import pyautogui

videoRunning = False

def PressMediaKeys():
    global videoRunning

    if wahooCore.MPH > 1:
        if not videoRunning:
            pyautogui.press('playpause')
            videoRunning = True

        if wahooCore.MPH < 2:
            #0.25x
            pyautogui.hotkey('ctrl', 'shift', 'h')
        elif wahooCore.MPH < 3:
            #0.5x
            pyautogui.hotkey('ctrl', 'shift', 'j')
        elif wahooCore.MPH < 4:
            #1x
            pyautogui.hotkey('ctrl', 'shift', 'k')
        else:
            #2x
            pyautogui.hotkey('ctrl', 'shift', 'l')

    elif videoRunning:
        pyautogui.press('playpause') 
        videoRunning = False

async def main():
    await wahooCore.run(PressMediaKeys)
    while True:
        await asyncio.sleep(1)

asyncio.run(main())
    