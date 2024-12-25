import wahooCore

videoRunning = False

async def PressMediaKeys():
    global videoRunning

    if wahooCore.mph > 1:
        if not videoRunning:
            pyautogui.press('playpause')
            videoRunning = True

        if wahooCore.mph < 2:
            #0.25x
            pyautogui.hotkey('ctrl', 'shift', 'h')
        elif wahooCore.mph < 3:
            #0.5x
            pyautogui.hotkey('ctrl', 'shift', 'j')
        elif wahooCore.mph < 4:
            #1x
            pyautogui.hotkey('ctrl', 'shift', 'k')
        else:
            #2x
            pyautogui.hotkey('ctrl', 'shift', 'l')

    elif videoRunning:
        pyautogui.press('playpause') 
        videoRunning = False

asyncio.run(wahooCore.run(PressMediaKeys))