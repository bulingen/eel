import time

import board
import busio
import adafruit_ads1x15.ads1015 as ADS

from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0, ADS.P1)

last_reading = time.time()

print("start getting values...")

while 1:
    now = time.time()
    if now - last_reading > 0.1:
        print(f"Value {chan.value}")
        last_reading = now
