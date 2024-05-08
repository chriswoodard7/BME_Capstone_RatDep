import serial
import time
import easygui

serial_port = 'COM7'
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
file_save = easygui.enterbox("Save file as:")
write_to_file_path = f"{file_save}.txt"

output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
n = 0
start_time = time.time()

while True:
    if n == 0:
        output = "Sample,Time,X,Y,PIR1,PIR2,PIR3,PIR4\n"
        output_file.write(output)
    else:
        line = ser.readline()
        line = line.decode("utf-8") #ser.readline returns a binary, convert to string
        curr_time = time.time() - start_time
        output = f"{n},{curr_time},{line}"
        print(output)
        output_file.write(output)
    n += 1