from digi.xbee.devices import *
import datetime as dt
import matplotlib.pyplot as plt
import re
import numpy as np
import matplotlib.animation as animation

port = 'COM6' # Serial Port
baud = 9600 # Serial Baudrate

#Instantiate an Xbee Device object
device = XBeeDevice(port,9600)
device.open()

#Instantiate a remote Xbee device object
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040CA0444"))
device.set_sync_ops_timeout(100)

# Receiving Data
while True:
    xbee_message = device.read_data()
    if xbee_message is not None:
        decoded_data = xbee_message.data.decode()
        turn_to_list = re.findall(r"[-+]?\d*\.\d+|\d+", decoded_data)  # Using Regax to create list
        print(turn_to_list)


# Figure
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
line, = ax.plot([],[],lw=2)

max_points = 50
line, ax.plot(np.arange(max_points),np.ones(max_points,dtype=np.float)*np.nan,lw=2)
def init():
    return line,

def animate(i):
    y = turn_to_list[0]
    y = float(y)

    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:],y]
    line.set_ydata(new_y)
    return line,

anim = animation.FuncAnimation(fig,animate,init_func=init,frames=200,interval=20, blit = False)

plt.show()

# i = 0
# xar = []
# Gx, Gy, Gz, Ax, Ay, Az = [], [], [], [], [], []



# def animate_ax(i,xs1,ys1):
#
#     xs1.append(dt.datetime.now().strftime('%H%M%S'))
#     ys1.append()
#
#     xs1 = xs1[-40:]
#     ys1 = ys1[-40:]
#
#     ax1.clear()
#     ax1.plot(xs1, ys1)
#
#     # Format plot
#     print("Format plot")
#     plt.xticks(rotation=45, ha='right')
#     plt.subplots_adjust(bottom=0.20)
#
#     plt.title('acceleration data over Time')
#     plt.ylabel('m/s')
#
# try:
#     while True:
#         xbee_message = device.read_data()
#         if xbee_message is not None:
#             decoded_data = xbee_message.data.decode()
#             turn_to_list = re.findall(r"[-+]?\d*\.\d+|\d+", decoded_data)  # Using Regax to create list
#             Gx_1 = float(turn_to_list[0])
#             Gy_1 = float(turn_to_list[1])
#             Gz_1 = float(turn_to_list[2])
#             Ax_1 = float(turn_to_list[3])
#             Ay_1 = float(turn_to_list[4])
#             Az_1 = float(turn_to_list[5])
#             long = float(turn_to_list[6])
#             lat = float(turn_to_list[7])
#             xar.append(int(i))
#             print(xar,Ax, Ay, Az, Gx, Gy, Gz)
#
#             i = i + 1
#
#             Gx.append(Gx_1)
#             Gy.append(Gy_1)
#             Gz.append(Gz_1)
#             Ax.append(Ax_1)
#             Ay.append(Ay_1)
#             Az.append(Az_1)
#
# except Exception as e:
#     print('Error Occured: %s' % str(e))
#     device.close()
#
#