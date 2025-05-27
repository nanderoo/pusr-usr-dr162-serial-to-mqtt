import sys
import serial
import time

if(len(sys.argv) > 1):
   data_to_send = sys.argv[1] # send in the payload in "quotes" as an argument
else:
   data_to_send = "mqtt payload goes here"

port = "/dev/ttyUSB0"  # Replace with your serial port
baudrate = 9600
try:
    ser = serial.Serial(port, baudrate)
    print(f"Connected to {port} at {baudrate} baud")
except serial.SerialException as e:
    print(f"Error: Could not open serial port: {e}")
    exit()

time.sleep(2)

try:
    ser.write(data_to_send.encode('UTF-8'))
    print(f"Sent: {data_to_send}")
    time.sleep(2)

except serial.SerialException as e:
    print(f"Error: Serial communication error: {e}")

finally:
    ser.close()
    print("Serial port closed")
