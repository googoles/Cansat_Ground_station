from time import sleep  # import
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# from digi.xbee.devices import XBeeDevice
# from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.devices import *
import serial

port = 'COM6' # Serial Port
baud = 9600 # Serial Baudrate

#Instantiate an Xbee Device object
device = XBeeDevice(port,9600)
device.open()

#Instantiate a remote Xbee device object
# remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040CA0444"))
device.set_sync_ops_timeout(10)

# Read data
# print(device.get_sync_ops_timeout())
# xbee_message = device.read_data()

# while xbee_message is None:

while True:
    xbee_message = device.read_data()
    if xbee_message is not None:
        print(xbee_message.data.decode())
        # a = map(xbee_message,range(5))
        # print(list(a))
        # print(type(xbee_message))
        # print(xbee_message)

        # result = list(map(xbee_message,range(5)))
        # print(result)

device.close()
# def animate(i,xs,ys):
#     print("i: ",i)
#     # Add x and y to lists
#     ##    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
#     xs.append(dt.datetime.now().strftime('%H%M%S'))
#     data = device.read_data(remote_device)
#     ys.append(data)
#     sleep(1)
#
#     #Limit x and y components
#     xs = xs[-40:]
#     ys = ys[-40:]
#
#     print('ys: ', ys)
#     print('xs: ',xs)
#     #Draw x and y lists
#     ax.clear()
#     ax.plot(xs,ys)
#
#     print('Format plot')
#     plt.xticks(rotation=45, ha='right')
#     plt.subplots_adjust(bottom=0.20)
#
#     plt.title('acceleration data over Time')
#     plt.ylabel('m/s')
#
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# xs = []
# ys = []
#
# print('Reading Data of Gyroscope and Accelerometer')
# ani = animation.FuncAnimation(fig,animate,fargs=(xs,ys),interval=1)
# plt.show()