from djitellopy import Tello
import time
import serial

ser = serial.Serial('/dev/cu.usbmodem141401')
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
            print("Takeoff Done")
            flying=True
        elif 'DOWN' in decoded_bytes and flying:
            tello.land()
            flying=False
            print("Drone Landed")
        elif 'left' in decoded_bytes and flying:
            tello.move_left(10)
            print("Moved Left")
        elif 'right' in decoded_bytes and flying:
            tello.move_right(10)
            print("Moved Right")
        elif 'front' in decoded_bytes and flying:
            tello.move_forward(10)
            print("Moved Front")
        elif 'back' in decoded_bytes and flying:
            tello.move_back(10)
            print("Moved Back")
        if time.time()-start>30:
            tello.land()
            flying=False
            print("Landing Drone")
    except:
        print("Keyboard Interrupt")
        tello.land()
        break
