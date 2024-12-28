import wahooCore
import os
import asyncio

count = 0

async def CountDown():
    global count
    
    while True:
        if(wahooCore.MPH > 0):
            count += 1
        else:
            count = 0
        
        os.system('cls')
        print(count)
        await asyncio.sleep(1)


async def main():
    await wahooCore.run()
    await CountDown()

asyncio.run(main())