import wahooCore
import os
import asyncio

count = 0

async def CountDown(sender, speedData):
    global count
    mph = await wahooCore.ConvertSpeedDataToMPH(sender, speedData)

    # if(count > 0):
    if(mph > 2):
        count += 1
    elif mph < 1:
        count = 0
    
    os.system('cls')
    print(count)
    # else:
    #     print("YOU WON!")
    #     await asyncio.sleep()

asyncio.run(wahooCore.run(CountDown))