from bleak import BleakScanner, BleakClient
import asyncio
import os

wahooSpeedSensor = None
SPEED_UUID = "00002a5b-0000-1000-8000-00805f9b34fb"
MPH = 0
previousDistance = 0
previousTime = None
functionToRunOnNotify = None

WHEEL_CIRCUMFERENCE = 1

async def run(rFunctionToRunOnNotify = None):
    global functionToRunOnNotify
    if rFunctionToRunOnNotify is not None:
        functionToRunOnNotify = rFunctionToRunOnNotify

    await DiscoverWahooSpeedSensor()
    await wahooSpeedSensor.start_notify(SPEED_UUID, ConvertSpeedDataToMPH)
    asyncio.create_task(RemainConnected())

async def DiscoverWahooSpeedSensor():
    global wahooSpeedSensor

    failedAttempts = 0
    while wahooSpeedSensor is None:
        os.system('cls')
        print("Discovering devices")
        print(f"Failed attempts: {failedAttempts}" if failedAttempts > 0 else "", end="\n")

        for device in await BleakScanner.discover():
            if device.name and "Wahoo SPEED" in device.name: 
                wahooSpeedSensor = BleakClient(device)
                await wahooSpeedSensor.connect()
                print(f"Connected to {device.name} - {device.address}")
        
        failedAttempts += 1

async def ConvertSpeedDataToMPH(sender, speedData):
    global MPH
    global previousDistance
    global previousTime
    global WHEEL_CIRCUMFERENCE

    currentTime = asyncio.get_event_loop().time()
    distance = int.from_bytes(speedData, byteorder='little')

    if previousTime is not None:
        timeElapsed = currentTime - previousTime
        if timeElapsed == 0:
            return
        
        distanceTraveled = (distance - previousDistance) * WHEEL_CIRCUMFERENCE
        speed_mps = distanceTraveled / timeElapsed
        MPH = speed_mps * 2.23694 / (10 ** 15)  # convert m/s to mph
    previousDistance = distance
    previousTime = currentTime

    if functionToRunOnNotify is not None:
        functionToRunOnNotify()

async def RemainConnected():
    global wahooSpeedSensor

    while True:
        if not wahooSpeedSensor.is_connected:
            wahooSpeedSensor = None
            await run()
            break
        await asyncio.sleep(1)

async def ListAllUUIDs():
    global wahooSpeedSensor
    print("Services and Characteristics:")
    for service in wahooSpeedSensor.services:
        print(f"Service: {service.uuid}")
        for characteristic in service.characteristics:
            print(f"  Characteristic: {characteristic.uuid} - Properties: {characteristic.properties} - Description: {characteristic.description}")