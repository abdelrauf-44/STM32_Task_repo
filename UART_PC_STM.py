import serial
import time


# Open serial port (adjust to your STM32 port and baudrate!)
ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=1)

print("Connected to STM32. Type messages to send (type 'exit' to quit).")

try:
    while True:
        # Get user input
        msg = input("You: ")
        if msg.lower() == "exit":
            break

        # Send message (append newline so STM32 knows end of message)
        ser.write((msg + "\n").encode('utf-8'))

        # Read response
        response = ser.readline().decode('utf-8').strip()
        if response:
            print(f"STM32: {response}")

except KeyboardInterrupt:
    pass

finally:
    ser.close()
    print("Connection closed.")
