import wahooCore
import os
import asyncio

count = 0

async def CountDown():
    global count
    
    while True:
        countChanged = False
        if(wahooCore.MPH > 0):
            count += 1
            countChanged = True
        elif count != 0:
            count = 0
            countChanged = True
        
        if countChanged:
            os.system('cls')
            print(count)

        await asyncio.sleep(2)


async def main():
    await wahooCore.run()
    await CountDown()

asyncio.run(main())