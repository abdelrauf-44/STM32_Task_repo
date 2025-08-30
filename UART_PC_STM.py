import serial
import time


# Open serial port (adjust to your STM32 port and baudrate!)
ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=1)

print("Connected to STM32")

try:
    while True:
        # Read response
        MSG = ser.readline().decode('utf-8').strip()
        if MSG:
            print(f"STM32: {MSG}")
            time.sleep(1)


except KeyboardInterrupt:
    pass

finally:
    ser.close()
    print("Connection closed.")
