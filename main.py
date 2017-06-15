import json
import network
import socket
import time

from machine import Pin, I2C
from vl53l0x import VL53L0X

SSID = "XXX"
PASSWORD = "XXX"
SERVER_ADDRESS = ("172.19.3.179", 8000)
DELAY = 0.1

def run():
    connect()
    loop()


def connect(ssid=SSID, password=PASSWORD):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while True:
        addr = wlan.ifconfig()[0]
        if addr != "0.0.0.0":
            break
        time.sleep(1)


def loop():
    i2c = I2C(scl=Pin(2), sda=Pin(4), freq=100000)
    vl = VL53L0X(i2c)
    vl.start()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    current = None
    seqnum = 0

    while True:
        val = vl.read()
        if val != current:
            current = val
            msg = {
                "value": val,
                "ticks_cpu": time.ticks_cpu(),
                "seqnum": seqnum,
            }
            data = json.dumps(msg).encode("ascii")
            s.sendto(data, SERVER_ADDRESS)
            time.sleep(DELAY)

        seqnum += 1


if __name__ == "__main__":
    run()
