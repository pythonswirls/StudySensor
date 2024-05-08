from Sensor import *

sonic1 = Sensor("sonic1", [19,18])
sonic2 = Sensor("sonic2", [5,6])
sonic1.calibrate
sonic2.calibrate

print(sonic1.gap)
print(sonic2.gap)