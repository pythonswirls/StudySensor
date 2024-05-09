
import pineworkslabs.RPi as GPIO
import time
from time import sleep
TRIG = 6
ECHO = 5


GPIO.setmode(GPIO.LE_POTATO_LOOKUP)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


while True:
    GPIO.output(TRIG, GPIO.LOW)
    sleep(2)


    GPIO.output(TRIG, GPIO.HIGH)
    sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    #note the start pule of echo
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    #note the end of the pule of echo
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = (pulse_end - pulse_start)

    distance = pulse_duration * 17150

    #round to two decimal
    distance = round(distance, 2)

    print(f"Distance: {distance} cm")

    
    