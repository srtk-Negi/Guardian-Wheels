
import subprocess
import serial
arduino_port = 'COM3'  # Example: 'COM3' on Windows or '/dev/ttyUSB0' on Linux
baud_rate = 9600

try:
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    print(f"Connected to Arduino on {arduino_port}")

    while True:
        arduino_response = arduino.readline().decode("utf-8").strip()
        if arduino_response == "1":
            print("Car broken into!")
            subprocess.call(['python', 'master_python_script.py'])
        else:
            print("No break-in detected.")
except serial.SerialException:
    print(f"Failed to connect to Arduino on {arduino_port}")
except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    arduino.close()
    print("Serial connection closed")
