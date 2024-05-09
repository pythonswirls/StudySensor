#new module imported gpiozero for sonic sensors

'''admin@raspberrypi:~/Desktop/StudySensor/StudySensor $ python test.py
/usr/lib/python3/dist-packages/gpiozero/devices.py:288: PinFactoryFallback: Falling back from rpigpio: This module can only be run on a Raspberry Pi!
  warnings.warn(
/usr/lib/python3/dist-packages/gpiozero/devices.py:288: PinFactoryFallback: Falling back from lgpio: module 'lgpio' has no attribute 'BOTH_EDGES'
  warnings.warn(
/usr/lib/python3/dist-packages/gpiozero/devices.py:288: PinFactoryFallback: Falling back from rpio: No module named 'RPIO'
  warnings.warn(
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Can't connect to pigpio at localhost(8888)

Did you start the pigpio daemon? E.g. sudo pigpiod

Did you specify the correct Pi host/port in the environment
variables PIGPIO_ADDR/PIGPIO_PORT?
E.g. export PIGPIO_ADDR=soft, export PIGPIO_PORT=8888

Did you specify the correct Pi host/port in the
pigpio.pi() function? E.g. pigpio.pi('soft', 8888)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
/usr/lib/python3/dist-packages/gpiozero/devices.py:288: PinFactoryFallback: Falling back from pigpio: failed to connect to localhost:8888
  warnings.warn(
/usr/lib/python3/dist-packages/gpiozero/devices.py:288: PinFactoryFallback: Falling back from native: unable to locate Pi revision in /proc/device-tree or /proc/cpuinfo
  warnings.warn(
Traceback (most recent call last):
  File "/home/admin/Desktop/StudySensor/StudySensor/test.py", line 5, in <module>
    us1 = DistanceSensor(17,27)
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 108, in __call__
    self = super(GPIOMeta, cls).__call__(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/gpiozero/input_devices.py", line 830, in __init__
    super(DistanceSensor, self).__init__(
  File "/usr/lib/python3/dist-packages/gpiozero/input_devices.py", line 260, in __init__
    super(SmoothedInputDevice, self).__init__(
  File "/usr/lib/python3/dist-packages/gpiozero/mixins.py", line 218, in __init__
    super(EventsMixin, self).__init__(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/gpiozero/input_devices.py", line 83, in __init__
    super(InputDevice, self).__init__(pin, pin_factory=pin_factory)
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 540, in __init__
    super(GPIODevice, self).__init__(**kwargs)
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 250, in __init__
    Device.pin_factory = Device._default_pin_factory()
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 291, in _default_pin_factory
    raise BadPinFactory('Unable to load any default pin factory!')
gpiozero.exc.BadPinFactory: Unable to load any default pin factory!
'''

from gpiozero import DistanceSensor
import pineworkslabs.RPi as GPIO
GPIO.setmode(GPIO.LE_POTATO_LOOKUP)
6
us1 = DistanceSensor(17,27)
#us2 = DistanceSensor(29,31)

while True:
    print(str(us1.distance()), 'Sensor1')
    #print(str(us2.distance()), 'Sensor2')