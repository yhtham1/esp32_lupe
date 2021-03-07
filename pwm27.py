
import time
from machine import Pin,PWM
import _thread


p1 = Pin(16,Pin.OUT)
p1.off()
p2 = Pin(2,Pin.OUT)
p2.on()

RED   = Pin(32, Pin.IN, Pin.PULL_UP)
WHITE = Pin(12, Pin.IN, Pin.PULL_UP)

pwm1 = PWM(Pin(17))
pwm1.freq(4000)
pwm1.duty(0)

def isRED():
	if RED.value():
		return False
	else:
		return True


def blink():
	ct = 0
	while True:
		if isRED():
			pwm1.duty(500)
		else:
			pwm1.duty(0)
		p2.off()
		if 0==(ct&0x1f):
			p2.on()
		time.sleep(0.01)
		ct += 1


_thread.start_new_thread(blink,())

