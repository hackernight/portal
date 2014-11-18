import RPi.GPIO as gpio
from time import sleep

DOOR_1_PIN = 38 
DOOR_2_PIN = 40

class Door:
    ONE = (DOOR_1_PIN, 1)
    TWO = (DOOR_2_PIN, 2)
    def get_pin(self):
        

doors = dict(
    ONE = DOOR_1_PIN,
    TWO = DOOR_2_PIN
)


class PortalHW:
    def __init__(self):
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)
        gpio.setup(doors["ONE"], gpio.OUT)
        gpio.setup(doors["TWO"], gpio.OUT)

    def toggle_door(self, door):
        print door
        print type(door)
        gpio.output(doors[door], 1)
        sleep(1)
        gpio.output(doors[door], 0)    
    #def lights_on():
    #def lights_off():


if __name__ == "__main__":
    portal = PortalHW()
    portal.toggle_door("ONE")
    sleep(5)
    portal.toggle_door("ONE")
