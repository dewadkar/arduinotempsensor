"""
Serial port connection
"""
import serial
import time

print("Start")
# Select the port
port = "/dev/ttyACM0"

# Connection with serial port
bluetooth = serial.Serial(port, 9600)
print("Connected")

# Flush the data collected from bluetooth
bluetooth.flushInput()
i = 0

while(1): # Infinitely  check the bluetooth port 
	print("Ping:")
	bluetooth.write(b"BOOP " + str.encode(str(i))) # Conversion of data into byte from Unicoe, plus a number

	# Read the data from bluetooth object
	input_data = bluetooth.readline()
	# Display data
	print(input_data.decode())
	time.sleep(0.1)
	i += 1

# Close bluetooth connection
bluetooth.close()
print("Done")