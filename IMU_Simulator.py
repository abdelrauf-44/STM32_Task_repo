import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(1)
print("STM Communication Established")


Header = bytes([0xAA, 0x00])
Index = bytes([0x05])
DATA = bytes([0x01, 0x00, 0x02, 0x00, 0x03, 0x00, 0x04, 0x00, 0x05, 0x00])
Turn_count = bytes([0x22])
Checksum = bytes([0x15])


while True:
    ser.write(Header + Index + DATA + Turn_count + Checksum)
    time.sleep(1)

    print("")
    print("Data Sent:")
    print("Header:", Header.hex())
    print("Index:", Index.hex())
    print("DATA:", DATA.hex())
    print("Turn_count:", Turn_count.hex())
    print("Checksum:", Checksum.hex())
    print("")



    if ser.in_waiting > 0:
        echo = ser.read(ser.in_waiting)
        try:
            text = echo.decode('utf-8').strip()
            print("Received text from STM32:", text)
        except UnicodeDecodeError:
            print("Received non-text data:", echo.hex())
