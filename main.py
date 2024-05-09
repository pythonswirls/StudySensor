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


#Instantiate classes/ temp vars
#                         [trig, echo]
sonic1 = Sensor("sonic1", [23,24])
sonic2 = Sensor("sonic2", [6,5])
sonic1.calibrate()
sonic2.calibrate()

print(f"sonic1 gap = {sonic1.gap}")
print(f"sonic2 gap = {sonic2.gap}")


 
people = 0

RUNNING = True

while(RUNNING):
    import Sensor

    count = 0
    list1 = []
    list2 = []
    timeavg1 = 0
    timeavg2 = 0
   

    while count <= 3:
        list1 = sonic1.sensor_tripped(list1)
        list2 = sonic2.sensor_tripped(list2)
        count += 1

    #oldval = main.capacity?

    if len(list1) != 0:
        people += sonic1.in_or_out(sonic2, people, list1, list2)
    
    
    print(people)
    #main.__init__((6-people), 0)
    
