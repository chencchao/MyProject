import serial
import time
data_into = "connect mi"
serialport = serial.Serial()
serialport.port = 'COM3'
serialport.baudrate = 921600
serialport.bytesize = 8
serialport.parity = serial.PARITY_NONE
serialport.stopbits = 1
serialport.timeout = 0.001
serialport.close()
if not serialport.is_open:
	serialport.open()
time.sleep(0.05) #时间设置参考串口传输速率
num = serialport.inWaiting()
serialport.write((data_into + '\r\n').encode('utf8'))
while num == 0:
	time.sleep(0.1) #时间设置参考串口传输速率
	num = serialport.inWaiting()
if num > 0:
	data = serialport.read(num)
	# bytes转str
	print(str(data))
