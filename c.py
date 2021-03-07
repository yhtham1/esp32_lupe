
from machine import Pin,PWM

p2 = Pin(2,Pin.OUT)
p2.off()
pwm = PWM(Pin(27))
pwm.duty(300)



