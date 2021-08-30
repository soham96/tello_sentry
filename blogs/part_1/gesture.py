from djitellopy import Tello
import time
import serial

ser = serial.Serial('/dev/cu.usbmodem142401')
ser_bytes = ser.readline()
ser.flushInput()

tello=Tello()

tello.connect()
print(tello.get_current_state())
print('Starting')

flying=False

start=time.time()
while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        if 'UP' in decoded_bytes and not flying:
            tello.takeoff()
            print('Takeoff Done')
            flying=True
        elif 'DOWN' in decoded_bytes and flying:
            tello.land()
            print('Landing Done')
        elif 'LEFT' in decoded_bytes and flying:
            tello.move_left(50)
            print('Moved Left')
        elif 'RIGHT' in decoded_bytes and flying:
            tello.move_right(50)
            print('Moved Right')
        if time.time()-start>20:
            tello.land()
            print('Landing Done')
            flying=False
    except:
        print("Keyboard Interrupt")
        tello.land()
        print('Landing Done')
        break
