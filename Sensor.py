#Group 2 -- GPIO code 
#Causey, Dalferes, Vaurigaud 


import pineworkslabs.RPi as GPIO
from time import sleep
import time
import datetime

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)



#Constants (some unused)
DEBUG = False
SETTLE_TIME = .2 #must be low to prevent slow down from real time measurment
                    #may have to change thi and other values to make program match up with
                    #walking speed
TRIGGER_TIME = 0.0001
SPEED_OF_TIME = 343 #m/s
DEFAULT_PINS = [1,2]
DISTANCE_DOOR = 2.5 #ft





#Since two untrasonic sensors are being used, there's benefit in a Sensor class

class Sensor():
    '''added self.TRIG and self.ECHO and getters/setters'''
    def __init__(self, name:str, pins:list):
        self.name = name
        #self.configure_pins(pins); not needed
        self.TRIG = pins[0]
        self.ECHO = pins[1]
        self.gap = 0.0  #to be used by sensor_tripped for range checking (being within door frame)

    @property                 
    def name(self):
        return self._name
    
    @name.setter                
    def name(self,value):
        self._name = value


    "TRIG/ECHO getters/setters"
    @property                   
    def TRIG(self):
        return self._TRIG
    @TRIG.setter
    def TRIG(self, value):
        self._TRIG = value

    @property                  
    def ECHO(self):
        return self._ECHO
    @ECHO.setter
    def ECHO(self, value):
        self._ECHO = value  

    @property                   
    def gap(self):
        return self._gap
    @gap.setter
    def gap(self, value):
        #shouldn't be negative, but range-checking not needed
        self._gap = value    
            

    def calibrate(self):
        """Regulates the distances and returns a correction factor to use for calculations"""
        
        #Notes for August: make is where we put in the measured distance from the sensor to the door,
        #then the sensor goes off and gets that value. You get: correction factor. 
        #If the correction factor is lower, than the sensor wont go off unless 
        #sensor_distance_reading > known_distance 
        #by greater than correction factor
        #vice versa
        "self.gap is modified"
        timeavg = 0
        denom = 0
        count = 0
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        while count <= 5:
            time_start = time.time()


            GPIO.output(self.TRIG, GPIO.LOW)
            sleep(TRIGGER_TIME)
            GPIO.output(self.TRIG, GPIO.HIGH)

            if GPIO.input(self.ECHO) == GPIO.HIGH:
                time_end = time.time()
                timeavg += (time_end - time_start)
                denom += 1
            count +=1

        if (timeavg == 0) or (denom == 0):
            #recursion allows function to rerun if self.ECHO was
                #never HIGH
                #if sensor broken recursion error will be returned
            self.calibrate()
            return
        
        timeavg = timeavg/denom
        self.gap = timeavg


    def sensor_tripped(self, my_list):
        """If there's movement of a person between a calculated distance of the doorways,
        the sensor records this distance for correction factor later. """
        
        GPIO.output(self.TRIG, GPIO.LOW)
        sleep(SETTLE_TIME) 

        GPIO.output(self.TRIG, GPIO.HIGH)
        sleep(TRIGGER_TIME)
        GPIO.output(self.TRIG, GPIO.LOW)

        #wait for ECHO pin to be high
        if (GPIO.input(self.ECHO) == 0):
                trip_time = time.time()
                rounded_time = round(trip_time, 5)
        if rounded_time <= self.gap:   #self.gap - .0006 to be more accurate?
            my_list.append(rounded_time)

        return my_list
        

    "won't work"
    def record_times(self):
        """THIS FUNCTION IS FOR TESTING PURPOSES. If the sensor_tripped function is initiated, a list starts appending
        a time stamp of the trips up to a certain set amount. In case there is an error, check the time stamps"""

        if self.sensor_tripped == True:
            result = datetime()

            return result

    
    def calculations(self, list):
        """Takes in the list of recorded times as a argument and calculates a average time that 
        the sensor was tripped and returns that value"""

        list_sum = sum(list)
        average = list_sum/len(list)

        #implement some way to limit the decimals
        return average

    def in_or_out(self, other:'Sensor', people):
        """Compares two sensors by taking their calculations and returning a positive or negative value"""
        #To label the sensors, self is considered closer to outside the room and other is closer to the inside.
        #if the time is smaller, got tripped first, someone went in, otherwise, someone left the room
        
        if self.calculations() <= other.calculations:
            people += 1

        elif other.calculations >= other.calculations:
            people -= 1

        else:
            raise ValueError("Wrong data type possibly.")
        
        return people

    def __str__(self):

        return f"{self.record_times}"


        
