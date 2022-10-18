from gpiozero import Button, LED

button = Button(21)

led = LED(25)

while True:

   led.on()

   button.wait_for_press()

   led.off()

   button.wait_for_release()