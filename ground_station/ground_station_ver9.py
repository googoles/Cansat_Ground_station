from digi.xbee.devices import *
import numpy as np
import folium
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
import tkinter as Tk
from tkinter import PhotoImage
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Xbee Integration
port = 'COM6'  # Serial Port
baud = 9600  # Serial Baudrate

# Instantiate an Xbee Device object
device = XBeeDevice(port, 9600)
device.open()

# Instantiate a specific remote Xbee device object
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040CA0444"))
device.set_sync_ops_timeout(10000)


explanation = """
This is a ground station for team PBD in Cansat Competition
"""


def data_gen():
    t = data_gen.t

    while True:
        xbee_message = device.read_data()
        if xbee_message is not None:
            data = xbee_message.data.decode()
            parsed_data = data.split(',')
            # t = dt.datetime.now().strftime('%H%M%S')
            t += 1
            time_passed = dt.datetime.now().strftime('%H%M%S')
            Ax = float(parsed_data[1])
            Ay = float(parsed_data[2])
            Az = float(parsed_data[3])
            Gx = float(parsed_data[4])
            Gy = float(parsed_data[5])
            Gz = float(parsed_data[6]) + 1
            lon = float(parsed_data[7])
            lat = float(parsed_data[8])
            detected = float(parsed_data[9])
            # print(time_passed,Ax,Ay,Az,Gx,Gy,Gz,lon,lat,detected)
            yield t, time_passed,Ax, Ay, Az, Gx, Gy, Gz, lon, lat, detected



data_gen.t = 0

# create a figure with two subplots
fig = plt.figure(figsize=(16,12))

ax1 = fig.add_subplot(3,4,1)
ax2 = fig.add_subplot(3,4,2)
ax3 = fig.add_subplot(3,4,3)
ax4 = fig.add_subplot(3,4,5)
ax5 = fig.add_subplot(3,4,6)
ax6 = fig.add_subplot(3,4,7)
ax7 = fig.add_subplot(3,4,8)
ax8 = fig.add_subplot(3,4,4)
    # , (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(3,3)
# fig.set_size

# intialize two line objects (one in each axes)
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2)
line3, = ax3.plot([], [], lw=2)
line4, = ax4.plot([], [], lw=2, color='r')
line5, = ax5.plot([], [], lw=2, color='r')
line6, = ax6.plot([], [], lw=2, color='r')
line7, = ax7.plot([],[],lw=2, color='b')
line8, = ax7.plot([],[],lw=2, color='r')
line = [line1, line2, line3, line4, line5, line6, line7, line8]

# the same axes initalizations as before (just now we do it for both of them)
ax1.set_ylim(-30,30)
ax1.set_xlim(0,50)
ax1.grid()
ax1.set_title('X Axis Acc')
# ax1.set_xlabel('Time spent')
ax1.set_ylabel('m/s^2')

ax2.set_ylim(-30,30)
ax2.set_xlim(0,50)
ax2.grid()
ax2.set_title('Y Axis Acc')
# ax2.set_xlabel('Time spent')
ax2.set_ylabel('m/s^2')

ax3.set_ylim(-30,30)
ax3.set_xlim(0,50)
ax3.grid()
ax3.set_title('Z Axis Acc')
# ax3.set_xlabel('Time spent')
ax3.set_ylabel('m/s^2')

ax4.set_ylim(-10,10)
ax4.set_xlim(0,50)
ax4.grid()
ax4.set_title('X Axis Gyro')
ax4.set_xlabel('Time spent')
ax4.set_ylabel('Deg/s')

ax5.set_ylim(-10,10)
ax5.set_xlim(0,50)
ax5.grid()
ax5.set_title('X Axis Gyro')
ax5.set_xlabel('Time spent')
ax5.set_ylabel('Deg/s')

ax6.set_ylim(-10,10)
ax6.set_xlim(0,50)
ax6.grid()
ax6.set_title('X Axis Gyro')
ax6.set_xlabel('Time spent')
ax6.set_ylabel('Deg/s')

ax7.set_ylim(127.204,127.207)
ax7.set_xlim(34.510,34.710)
ax7.set_title('Location')

ax8.set_ylim(-2,2)
ax8.set_xlim(0,50)
ax8.grid()
ax8.set_title('Detection')
ax8.set_xlabel('Time Spent')
ax8.set_ylabel('Detected if Number is 1')
# for ax in [ax4,ax5,ax6]:
#     ax.set_ylim(-10, 10)
#     ax.set_xlim(0,50)
#     ax.grid()

# for ax in [ax7]:
    # ax.set_xlim(34.510,34.71)
    # ax.set_ylim(127.204,127.207)

# initialize the data arrays
xdata, time_data, axdata, aydata, azdata, gxdata, gydata, gzdata, londata, latdata, detected_data = [], [], [], [], [], [], [], [],[],[],[]

# def animate_gps(data):
#     lon, lat = data
#     old_y = line.get_ydata()
#     new_y = np.r_[old_y[1:],y]


def run(data):
    # update the data
    t, time_passed, Ax, Ay, Az, Gx, Gy, Gz, lon, lat, detected = data
    xdata.append(t)
    time_data.append(time_passed)
    axdata.append(Ax)
    aydata.append(Ay)
    azdata.append(Az)
    gxdata.append(Gx)
    gydata.append(Gy)
    gzdata.append(Gz)
    londata.append(lon)
    latdata.append(lat)
    detected_data.append(detected)

    # axis limits checking. Same as before, just for both axes
    for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()

        if t >= xmax:
            ax.set_xlim(xmin, 2 * xmax)
            # ax.set_ylim(ymin, ymax)
            ax.figure.canvas.draw()

    # update the data of both line objects
    line[0].set_data(xdata, axdata)
    line[1].set_data(xdata, aydata)
    line[2].set_data(xdata, azdata)
    line[3].set_data(xdata, gxdata)
    line[4].set_data(xdata, gydata)
    line[5].set_data(xdata, gzdata)
    line[6].set_data(londata,latdata)
    line[7].set_data(xdata,detected_data)

    return line



root = Tk.Tk()
# Tkinter setup
root.iconbitmap('logo.ico')
logo = PhotoImage(file="logo.gif")
root.geometry("2800x1600+100+100")
root.title("PBD Ground Station")
# w1 = Tk.Label(root,image=logo).pack(side="right")
# w2 = Tk.Label(root,justify=Tk.LEFT,padx=10,text=explanation).pack(side='left')

label=Tk.Label(root, image=logo, text='Ground Station for PBD', compound = 'left',fg = 'black', bg = 'white',font=('times',28), width = 1400)
label.place(x=0,y=0)




# msg = Tk.Message(root,text="GYROSCOPE")
# msg.config(bg='white',font=('times',12,'italic'))
# msg.place(x=0,y=369,width = 1200, height = 200)

label_mpu = Tk.Label(root,text=explanation, width = 1600, height = 100, fg = 'black', bg = 'white',font=('times',14))
# label_mpu.insert(Tk.CURRENT, "MPU6050 Data")
label_mpu.place(x=1400,y=0,width = 1200, height = 400)
canvas = FigureCanvasTkAgg(fig,master=root)
# canvas.set_window_title(title="MPU6050 Data")
canvas.get_tk_widget().place(x = 0, y = 350)

# frame1 = Tk.Frame(label_mpu,relief='solid',bd=2)
# frame1.pack(side='left',fill='both',expand=True)
# frame2 = Tk.Frame(root,relief='solid',bd=2)
# frame2.pack(side='right',fill='both',expand=True)


ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,
                              repeat=False)
# plt.show()
plt.tight_layout()

Tk.mainloop()
