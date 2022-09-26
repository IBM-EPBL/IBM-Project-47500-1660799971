import random
temperature = random.randint(100,150)
humidity = random.randint(100,130)
if temperature>150 and humidity>130:
    print ('Alarm is on')
temperature = random.randint(50,70)
humidity = random.randint(30,80)
if temperature<50 and humidity<30:
        print ('Alarm is off')
