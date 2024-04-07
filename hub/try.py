import serial
import time

def read():
    ser = serial.Serial(
        port='/dev/cu.usbmodem2101',
        baudrate=9600,
        timeout=1
    )
    time.sleep(2)  # Wait for the connection to initialize

    while True:
        if ser.in_waiting > 0:  # Check if data is available
            line = ser.readline()
            print(line)
            line = line.strip()  # Strip newline characters
            print(line)

if __name__ == "__main__":
    read()