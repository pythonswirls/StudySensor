#RUN THIS PROGRAM on Le Potato
#all other files imported/automatically run
#main.py is responsible for looping the sensor_tripped and data comparsion functions
#   and creating temporary lists/data to pass through to GUI.py 

#likely wont need to see if main_menu.add.button('Quit', pygame_menu.events.EXIT) = True
import Sensor
import GUI
import pygame

#Instantiate classes/ temp vars
#                         [trig, echo]
sonic1 = Sensor("sonic1", [19,18])
sonic2 = Sensor("sonic2", [5,6])
run = True
list1 = []
list2 = []
timeavg1 = 0
timeavg2 = 0
RUNNING = True

while(RUNNING):
    