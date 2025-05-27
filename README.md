# pusr-usr-dr162-serial-to-mqtt
A quick playground of Python scripts to test the [PUSR USR-DR162 Serial to WiFi Bridge](https://www.pusr.com/support/download/User-Manual-USR-DR164-User-Manual-EN-V1.html).

I cobbled these sripts together from examples online for a quick product evaluation of the [PUSR](https://www.pusr.com/) [DR-162](https://www.pusr.com/products/Serial-to-Dual-Band-WiFi-Converter.html).

The exercise involved reading and writing MQTT payload messages to the pre-configured Pub/Sub Topics on a remote MQTT Broker.

Testing was done using a Raspberry Pi 2W and [Waveshare USB to RS232/485 serial converter](https://www.waveshare.com/usb-to-rs232-485.htm).

>[!NOTE]
>Per discussion with the manufactures technical support the DR162 does not suport TTL via STTY/UART 'serial' via the GPIO pins. I initally tried to get this to work by mapping pins 14 & 15 for RX/TX and reading and writing from something like`/dev/ttyS0`. You will need an actual RS232 device/interface in order to use the DR162 -- like the Waveshare converter mentioned above -- and access it via something like `/dev/ttyUSB0`. The +5 volts and ground pins from the Pi are sufficent to power the device.

![rs232 converter to dr162](https://raw.githubusercontent.com/nanderoo/pusr-usr-dr162-serial-to-mqtt/main/1000007893.jpg)
![power gpio pins on pi](https://raw.githubusercontent.com/nanderoo/pusr-usr-dr162-serial-to-mqtt/main/1000007894.jpg)
