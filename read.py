import serial
import time

port = "/dev/ttyUSB0"  # Replace with your serial port
baudrate = 9600
try:
    ser = serial.Serial(port, baudrate)
    print(f"Connected to {port} at {baudrate} baud")
except serial.SerialException as e:
    print(f"Error: Could not open serial port: {e}")
    exit()

try:
    while True:
        command = ser.read_until()
        print(command.decode().strip())

except serial.SerialException as e:
    print(f"Error: Serial communication error: {e}")

finally:
    ser.close()
    print("Serial port closed")
