#Group 2 -- GPIO code 

import pineworklabs.RPi as GPIO
from time import sleep

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)



#Constants 
PINS = []
DEBUG = False
SETTLE_TIME = 2
TRIGGER_TIME = 0.0001
SPEED_OF_TIME = 343 #m/s
DEFAULT_PINS = [1,2]





#Since two untrasonic sensors are being used, there's benefit in a Sensor class

class Sensor():

    def __init__(self, name:str, pins:list):
        self.name = name
        self.pins = self.configure_pins(pins)

    @property                   #name getter/setter
    def name(self):
        return self._name
    
    @name.setter                
    def name(self,value):
        self._name = value

    @property                   #pins getter/setter
    def pins(self):
        return self._pins
    
    @pins.setter
    def pins(self, value):
        if len(value) == 2:
            self._pins = value
        else:
            self._pins = DEFAULT_PINS
            


    def configure_pins(self,pins:list):
        """Receives pins as a argument with two values. Assigns the trig and echo pins 
            and configures trig as a output and echo as a input"""
        TRIG = pins[0]
        ECHO = pins[1]

        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
            

    def calibrate(self):
        """Regulates the distances and returns a correction factor to use for calculations"""
        pass

    def sensor_tripped(self):
        """If there's movement of a person between a calculated distance of the doorways,
        the sensor records this distance for correction factor later. """
        

    def record_times(self):
        """If the sensor_tripped function is initiated, a list starts appending a time stamp of the 
        trips up to a certain set amount."""

        list= []
        #time stamp stuff
        return list
    
    def calculations(self, list):
        """Takes in the list of recorded times as a argument and calculates a average time that 
        the sensor was tripped and returns that value"""

    def in_or_out(self, other:'Sensor'):
        """Compares two sensors by taking their calculations and returning a positive or negative value"""
        
###MAIN###

