#!/usr/bin/python3

import random
#Condition to check continuously
while(True):
#Input Values
 T = random.randint(-20, 120)
 H = random.randint(20, 80)
 print("Temperature = ",T)
 print("Humidity = ",H)
#Condition for Alarm
if T>100:
 if H>500:
   print("Hazard... Alarm On ")
else:
 print("Normal... No Alarm")