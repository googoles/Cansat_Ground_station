from digi.xbee.devices import *
import re
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

Gx = 0.
Gy = 0.
Gz = 0.
Ax = 0.
Ay = 0.
Az = 0.

port = 'COM6'  # Serial Port
baud = 9600  # Serial Baudrate

# Instantiate an Xbee Device object
device = XBeeDevice(port, baud)
device.open()

device.set_sync_ops_timeout(10)

def get_data():
    global Gx,Gy,Gz, Ax, Ay, Az
    xbee_message = device.read_data()
    if xbee_message is not None:
        decoded_data = xbee_message.data.decode()
        turn_to_list = re.findall(r"[-+]?\d*\.\d+|\d+", decoded_data)  # Using Regax to create list
        Gx = float(turn_to_list[0])
        Gy = float(turn_to_list[1])
        Gz = float(turn_to_list[2])
        Ax = float(turn_to_list[3])
        Ay = float(turn_to_list[4])
        Az = float(turn_to_list[5])

def init():
    return (line1,line2,line3,line4,line5,line6)

def animate(i):
    old_gx = line1.get_ydata()
    new_gx = np.r_[old_gx[1:], Gx]
    line1.set_ydata(new_gx)

    old_gy = line2.get_ydata()
    new_gy = np.r_[old_gy[1:], Gy]
    line2.set_ydata(new_gy)

    old_gz = line3.get_ydata()
    new_gz = np.r_[old_gz[1:], Gz]
    line3.set_ydata(new_gz)

    old_Ax = line4.get_ydata()
    new_Ax = np.r_[old_Ax[1:], Ax]
    line4.set_ydata(new_Ax)

    old_Ay = line5.get_ydata()
    new_Ay = np.r_[old_Ay[1:], Ay]
    line5.set_ydata(new_Ay)

    old_Az = line6.get_ydata()
    new_Az = np.r_[old_Az[1:], Az]
    line6.set_ydata(new_Az)

    return (line1,line2,line3,line4,line5,line6)

fig = plt.figure(figsize=(12, 6))
ax = plt.axes(xlim=(0, 100), ylim=(-90, 90))
plt.legend()
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
line3, = ax.plot([], [], lw=2)
line4, = ax.plot([], [], lw=2)
line5, = ax.plot([], [], lw=2)
line6, = ax.plot([], [], lw=2)

max_points = 100
line1, = ax.plot(np.arange(max_points), np.ones(max_points, dtype=np.float)*np.nan, lw=2, label='Gx')
line2, = ax.plot(np.arange(max_points), np.ones(max_points, dtype=np.float)*np.nan, lw=2, label='Gy')
line3, = ax.plot(np.arange(max_points), np.ones(max_points, dtype=np.float)*np.nan, lw=2, label='Gz')
line4, = ax.plot(np.arange(max_points), np.ones(max_points, dtype=np.float)*np.nan, lw=2, label='Ax')
line5, = ax.plot(np.arange(max_points), np.ones(max_points, dtype=np.float)*np.nan, lw=2, label='Ay')
line6, = ax.plot(np.arange(max_points), np.ones(max_points, dtype=np.float)*np.nan, lw=2, label='Az')

anim = animation.FuncAnimation(
                                fig,
                                animate,
                                init_func=init,
                                frames=200,
                                interval=100,
                                blit=False
                            )

plt.show()
device.close()
print('All done')