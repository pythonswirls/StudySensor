#Group #2
#Causey, Dalferes, Vaurigaud


#RUN THIS PROGRAM on Le Potato
#pip install pygame && pygame-menu
#all other files imported/automatically run
#main.py is responsible for looping the sensor_tripped and data comparsion functions
#   and creating temporary lists/data to pass through to GUI.py 

#likely wont need to see if main_menu.add.button('Quit', pygame_menu.events.EXIT) = True
from Sensor import *
from GUI import *
import pygame

#Instantiate classes/ temp vars
#                         [trig, echo]
sonic1 = Sensor("sonic1", [19,18])
sonic2 = Sensor("sonic2", [5,6])
run = True
 
people = 0

RUNNING = True

while(RUNNING):
    count = 0
    list1 = []
    list2 = []
    timeavg1 = 0
    timeavg2 = 0
    val = 0

    if count <= 5:
        list1 = sonic1.sensor_tripped(list1)
        list2 = sonic2.sensor_tripped(list2)
        count += 1
    
    timeavg1 = sonic1.calculations(list1)
    timeavg2 = sonic2.calculations(list2)

    #oldval = main.capacity

    people = sonic1.in_or_out(sonic2, people)
    
    main.capacity += people
    '''
    if people <= oldval:
        main.capacity -= 1
    else:
        if people >= oldval:
            main.capacity += 1'''
    

    