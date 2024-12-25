import wahooCore
import os
import asyncio

count = 0

def CountDown():
    global count
    
    if(wahooCore.MPH > 1.7):
        count += 1
    elif wahooCore.MPH < 0.5:
        count = 0
    
    os.system('cls')
    print(count)

asyncio.run(wahooCore.run(CountDown))