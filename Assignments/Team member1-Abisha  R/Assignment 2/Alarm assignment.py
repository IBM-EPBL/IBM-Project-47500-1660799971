import time
from random import uniform
def Weather():
    while True:
        temperature = uniform(1,100)
        humidity=uniform(1,3)
        if temperature>57.0 and humidity<2.24:
            print(" The alram detecting this is high temprature",temperature,"and",humidity)
            time.sleep(1)
        else:
            print()
Weather()