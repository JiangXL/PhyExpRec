# What
Collect, Store, Upload date from device by Raspberry Pi during experiment.

Used Device:
* Temp and humidity :DTH11, STH31-DIS


# How
``` bash
python launch.py
```

# Reading List
## I2C ##
+ [1 to 8 IIC](https://learn.adafruit.com/adafruit-tca9548a-1-to-8-i2c-multiplexer-breakout/wiring-and-test)
+ [I2C mulitplexer support](https://www.raspberrypi.org/forums/viewtopic.php?f=44&t=141517)
 dtoverlay=i2c-mux,pca9548,addr=0x70

+ i2cdetect -y 1
  i2cdetect -l
  [I2C](https://coldnew.github.io/f0528f55/)
+ [Introduction](http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2)
# To do
+ 时间戳--> 当地时间
+ GUI实时预览
+ 数据备份

# License
GPL
