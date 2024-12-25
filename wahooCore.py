from bleak import BleakScanner, BleakClient
import asyncio

SPEED_UUID = "00002a5b-0000-1000-8000-00805f9b34fb"
videoRunning = False
MPH = 1 / 10**16
previousMPH = MPH

async def ConvertSpeedDataToMPH(sender, speedData):
    global MPH
    global previousMPH

    speed = int.from_bytes(speedData, byteorder='little')
    MPH = speed / 10**16

    if MPH == previousMPH:
        MPH = 0

    previousMPH = MPH

async def DiscoverWahooSpeedSensor():
    print("Discovering devices...")
    devices = await BleakScanner.discover()

    for d in devices:
        print(f"Found device: {d.name} - {d.address}")
        if d.name and "Wahoo SPEED" in d.name:
            return d
    print("No appropriate device found.")
    return None

async def GetWahooSpeedSensor():
    wahooSpeedSensor = None
    while wahooSpeedSensor is None:
        wahooSpeedSensor = await DiscoverWahooSpeedSensor()

    print(f"Connected to {wahooSpeedSensor.name} - {wahooSpeedSensor.address}")
    return wahooSpeedSensor

async def CaptureNotifications(wahooSpeedSensorClient, functionToRunOnNotification):
    await wahooSpeedSensorClient.start_notify(SPEED_UUID, ConvertSpeedDataToMPH)
    while True:
        functionToRunOnNotification()
        await asyncio.sleep(1)  


async def run(functionToRunOnNotification):
    wahooSpeedSensor = await GetWahooSpeedSensor()

    #The async with statement ensures that the BleakClient is properly closed after its use, even if an error occurs during the execution of the block. This is important for managing resources and preventing potential memory leaks or connection issues.
    async with BleakClient(wahooSpeedSensor) as wahooSpeedSensorClient:
        await CaptureNotifications(wahooSpeedSensorClient, functionToRunOnNotification)