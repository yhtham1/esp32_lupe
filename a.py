
import time
from machine import Pin,PWM

p2 = Pin(2,Pin.OUT)
p2.off()
pwm = PWM(Pin(27))
pwm.duty(300)


buzz0 = Pin(16,Pin.OUT)
buzz1 = PWM(Pin(17))


p2.on()
time.sleep(1)



