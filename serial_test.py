import serial


ser = serial.Serial('COM6', 9600, timeout = 1)
while True:
    print('Insert op: ', end=' ')
    op = input()
    ser.write(op.encode())
    print('R: ',ser.readline())

    if op is 'q':
        ser.close()