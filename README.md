# Remote distance meter

This is a remote distance meter built during "Let's build a device
together using Python!" workshop in PyCon Israel 2017. See
http://il.pycon.org/wwwpyconIL/agenda/97.

The device is collecting distance measurements from a VL53L0X sensor,
and sending reports to the server over WIFI. It is rather useless but
can be a start point for making something more interesting.

## Requirements

- ESP8266 board with micropython installed
- VL53L0X sensor, see
  http://www.st.com/en/imaging-and-photonics-solutions/vl53l0x.html
- WIFI access point for communicating with the board
- breadboard and wires for connecting stuff
- vl53l0x.py module, available at
  https://bitbucket.org/thesheep/micropython-vl53l0x/src
- ampy package for uploading files to the board

## How to build

### Connected these pins:
   - ESP8266/3v3 - VL53L0X/vcc
   - ESP8266/gnd - VL53L0X/gnd
   - ESP8266/io2 - VL53L0X/scl
   - ESP8266/io4 - VL53L0X/sda

### Connect the ESP8266 board to your PC using USB cable

The board will be connected to /dev/ttyUSB0. Use dmesg -w to watch the
messages about new USB device connected.

### Add yourself to the dialout group

To use /dev/ttyUSB0, you need to be ```root```, or be in the
```dialout``` group.

To add yourself to the dialout group:

    sudo usermod -a -G dialout username

Log out and log in again to apply this change.

### Configuration

You need to set these variables in main.py to match your network:

    SSID = "Wify-Name"
    PASSWORD = "wify-password"
    SERVER_ADDRESS = ("192.168.0.1", 8000)

### Upload software to the board

    ampy -p /dev/ttyUSB0 put main.py
    ampy -p /dev/ttyUSB0 put vl53l0x.py

### Start the server on the PC

    python server.py

### Reset the board

Use the reset button on the board.

### You are done!

You can move your hand before the VL53L0X sensor and watch the messages
printed to the server standard output.

This is an example output:

    got '{"seqnum": 235, "value": 133, "ticks_cpu": 467554807}' from ('172.19.3.240', 49153)
    got '{"seqnum": 236, "value": 96, "ticks_cpu": 503409982}' from ('172.19.3.240', 49153)
    got '{"seqnum": 237, "value": 88, "ticks_cpu": 538762126}' from ('172.19.3.240', 49153)
    got '{"seqnum": 238, "value": 84, "ticks_cpu": 574035697}' from ('172.19.3.240', 49153)
    got '{"seqnum": 239, "value": 82, "ticks_cpu": 609314179}' from ('172.19.3.240', 49153)
    got '{"seqnum": 240, "value": 90, "ticks_cpu": 644585239}' from ('172.19.3.240', 49153)
    got '{"seqnum": 241, "value": 101, "ticks_cpu": 679756012}' from ('172.19.3.240', 49153)
    got '{"seqnum": 242, "value": 115, "ticks_cpu": 715164238}' from ('172.19.3.240', 49153)
    got '{"seqnum": 243, "value": 130, "ticks_cpu": 750661627}' from ('172.19.3.240', 49153)
    got '{"seqnum": 244, "value": 149, "ticks_cpu": 786271759}' from ('172.19.3.240', 49153)
    got '{"seqnum": 245, "value": 145, "ticks_cpu": 821750476}' from ('172.19.3.240', 49153)
    got '{"seqnum": 246, "value": 115, "ticks_cpu": 857262205}' from ('172.19.3.240', 49153)

The values seems to be in millimeters, and it works up to about 50
centimeters.

## Known issues

- Board does not get IP - seems to happen when there are too many users
  connected to the access point. Resetting the board few times fixes
  this.

- TimeoutError from vl53l0x - may happen in the wires are not connected
  properly, reconnect the wires to fix.
