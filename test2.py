from Sensor import *


sonic1 = Sensor("sonic1", [19,18])
sonic2 = Sensor("sonic2", [6,5])
sonic1.calibrate
sonic2.calibrate

print(sonic1.gap)
print(sonic2.gap)

list = []
list2 = []
list = sonic1.sensor_tripped(list)
list2 = sonic2.sensor_tripped(list2)

print(list)
print(list2)