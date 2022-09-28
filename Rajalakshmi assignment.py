#!/usr/bin/python3

import time
from random import uniform
def Weather():
while True:
    temperature = uniform(1,120)
                      humidity=uniform(1,5)
                       if temperature>60.0 and humidity<3.34:
                               print(" The alram detecting this is high temprature",temperature,"and",humidity)
                                   time.sleep(1)
                       else:
                                       print()
                                       Weather()