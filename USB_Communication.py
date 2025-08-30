import serial
import time


port = '/dev/ttyACM1'  # Update this to your USB port
def read_usb_data(port):
    ser = serial.Serial(port, 1152000, timeout=1)
    #time.sleep(0.1)  # Wait for the connection to be established
    data = ser.read(20)  # Read up to 58 bytes
    ser.close()
    return data

def write_usb_data(port, data):
    ser = serial.Serial(port, 9600, timeout=1)
    time.sleep(0.1)  # Wait for the connection to be established
    ser.write(data)
    ser.close()

while True:
    data_rx = read_usb_data(port)
    if data_rx:
        lines = data_rx.decode(errors='ignore').splitlines()
        for line in lines:
            if line.strip():
                print("Received message:", line)
    #time.sleep(1)  # Adjust the sleep time as needed
    MSG = "Hello STM32 FROM USB\r\n".encode()
    data_tx = write_usb_data(port, MSG)
    if data_tx:
        print("Sent data:", MSG)
    time.sleep(1)

