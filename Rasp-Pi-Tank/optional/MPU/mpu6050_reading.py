#!/usr/bin/env python
 
from mpu6050 import mpu6050
from time import sleep



sensor = mpu6050(0x68)

while True:

    accel_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()
    temp = sensor.get_temp()

    print("Accelerometer data")
    print("x: " + str(accel_data['x'])[:4])
    print("y: " + str(accel_data['y'])[:4])
    print("z: " + str(accel_data['z'])[:4])

    print("Gyroscope data")
    print("x: " + str(gyro_data['x'])[:4])
    print("y: " + str(gyro_data['y'])[:4])
    print("z: " + str(gyro_data['z'])[:4])

    print("Temp: " + str(temp)[:4] + " C")
    sleep(1)