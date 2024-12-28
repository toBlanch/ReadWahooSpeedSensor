import wahooCore
import os
import asyncio

count = 0

def CountDown():
    global count
    
    if(wahooCore.MPH > 0):
        count += 1
    else:
        count = 0
    
    os.system('cls')
    print(count)

asyncio.run(wahooCore.run(CountDown))