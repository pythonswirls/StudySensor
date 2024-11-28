# StudySensor
![image](background_image.png)
### CSC 132 Final Pi Project
### Louisiana Tech University

For our design project, we needed to come up with a producted that used the Le Potato, it's GPIO output/input, and an Intuitive GUI. We decided to go with a "StudySensor", which utilizes two HR-SC04 Sonic Sensors to detect someone entering a study room. The information is passed from the sensor setup, managed by two instantiations of a single python class, to the "Main" portion of the program, then to the "GUI" portion.
The entirety of the program is written in python, and uses modules Pygame, Pygame-menu, time, and and the Pineworkslabs.RPi GPIO scheme.

#### Design
In the design of our project, we thought of campus-wide implementation from the get-go. We modeled our project just with one "room", but it could be easily be replicated with many more rooms, a larger computational hub, and cheaper microcontrollers. To scale up a "StudySensor" system would ultimately be inexpensive.

#### Lessons Learned
Here are some lessons learned from our develeopment of the project;
* Having a low-perfomance micontroller, such as the Le Potato, manage an entirety of the GUI, the class system, and the entirety of the computation can result is a low perfomance program. Our 
  microcontroller was getting noticely warm, and our program was noticeibly lagging. A higher performance microcontroller is to be desired.
* The HC-SR04 Sonic Sensor is incredibly unreliable. It is a sensor that returns the time it takes for a pulse to be received back from being bouced off a surface, but the time returned can be varied heavily, leading to inaccurate measurements. A compatible IR (Infared) distance sensor could be a more reliable but equally cost-effective alternative.

