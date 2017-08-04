#-------------------SHT31-------------------------------
#|     Time  | Version | Contribution | Comment
#| 2017.6.22|  0       |  fork form http://www.pibits.net/code/raspberry-pi-sht31-sensor-example.php
#| 2017.6.24 | 1     | H.F.         | Work :)
#| 2017.8.1  | 2     | H.F.         | change to SHT31 Class
#---------------------------------------------------------------

import smbus
import time

class SHT31(object):
    def __init__(self, box, place, rh):
	self.box = box
	self.place = place
	self.rh = rh

    # Get I2C bus
    def record(self):
	bus = smbus.SMBus(self.box)
	if(self.place=='Top'):
 	    addr=0x44
	else:
	    addr=0x45

	time0=time.strftime("%Y%m%d%H%M",time.localtime())
	datestore='/home/pi/Desktop/SHT/'+time0+self.rh+self.place+'.txt'
	ticks0=time.time()
	while True:
  	    # SHT31 address, 0x44(68) or 0x45(68)
	    bus.write_i2c_block_data(addr, 0x2C, [0x06])

            # Simple rate: 1time in 1 second
            time.sleep(1)

	    # Read data back from 0x00(00), 6 bytes
	    # Temp MSB,Temp LSB,Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
	    data = bus.read_i2c_block_data(addr, 0x00, 6)

 	    # Convert the data
	    temp = data[0] * 256 + data[1]
	    cTemp = -45 + (175 * temp / 65535.0)
	    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
	    ticks = time.time()

	    # Output data to screen
	    print("%.2f "%(ticks-ticks0)+"Temp%.2f "%cTemp+"RH%.2f"%humidity)

	    try:
		record = open(datestore, 'a')
		record.write(str(ticks)+",")
		record.write(str(cTemp)+",")
		record.write(str(humidity)+","+"\n")
	    finally:
		if record:
		    record.close()
	     # http://www.pibits.net/wp-content/uploads/2016/11/pi-and-sht31_bb.png
