import wahooCore
import asyncio
import pyautogui

videoRunning = False


def MainLoop():
    if wahooCore.MPH > 0:
        Play()
        #ChangeSpeed()
    else:
        Pause()

def Play():
    global videoRunning
    if not videoRunning:
        pyautogui.press('playpause')
        videoRunning = True

def Pause():
    if videoRunning:
        pyautogui.press('playpause')
        videoRunning = False

def ChangeSpeed():
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

async def main():
    await wahooCore.run(MainLoop)
    while True:
        await asyncio.sleep(1)

asyncio.run(main())
    