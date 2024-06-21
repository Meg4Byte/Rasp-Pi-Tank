import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)
fig, ax = plt.subplots()
x_data, y_data = [], []

def animate(i):
    accel_data = sensor.get_accel_data()
    x_data.append(time.time())
    y_data.append(accel_data['x'])
    ax.clear()
    ax.plot(x_data, y_data, label='Accelerometer X')
    ax.legend()

ani = FuncAnimation(fig, animate, interval=1000)
plt.show()
