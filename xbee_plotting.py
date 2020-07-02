from digi.xbee.devices import *
import re
from time import sleep  # import
import datetime as dt
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.animation as animation

port = 'COM6' # Serial Port
baud = 9600 # Serial Baudrate

#Instantiate an Xbee Device object
device = XBeeDevice(port,baud)
device.open()

device.set_sync_ops_timeout(10)

#Figure
# fig = plt.figure()
# ax = plt.subplot(211, xlim=(0,50), ylim=(0,30))
# max_point = 50
# line, = ax.plot(np.arange(max_point),np.ones(max_point, dtype=np.float)*np.nan, lw=1, c='blue', ms=1)
i = 0
xar = []
Gx,Gy,Gz,Ax,Ay,Az = [],[],[],[],[],[]

while True:
    xbee_message = device.read_data()
    if xbee_message is not None:
        decoded_data = xbee_message.data.decode()
        turn_to_list = re.findall(r"[-+]?\d*\.\d+|\d+",decoded_data) # Using Regax to create list
        Gx_1 = float(turn_to_list[0])
        Gy_1 = float(turn_to_list[1])
        Gz_1 = float(turn_to_list[2])
        Ax_1 = float(turn_to_list[3])
        Ay_1 = float(turn_to_list[4])
        Az_1 = float(turn_to_list[5])
        print(Ax,Ay,Az,Gx,Gy,Gz)


def animate(yolo):
    global i, xar, Gx,Gy,Gz,Ax,Ay,Az
    Gx.append(Gx_1)
    Gy.append(Gy_1)
    Gz.append(Gz_1)
    Ax.append(Ax_1)
    Ay.append(Ay_1)
    Az.append(Az_1)
    i = i+1


# ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=False)
anim = animation.FuncAnimation(fig,animate,interval = 1000)
# print(" Reading Data of Gyroscope and Accelerometer")
plt.show()
device.close()