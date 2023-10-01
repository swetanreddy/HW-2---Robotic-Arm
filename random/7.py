from machine import Pin
import time

step_pin_motor1 = Pin(18, Pin.OUT)
dir_pin_motor1 = Pin(19, Pin.OUT)

STEPS_PER_REVOLUTION = 200
SPEED = 0.01

angle = 45

dir_pin_motor1.value(1)

steps = int((angle/360) * STEPS_PER_REVOLUTION)
for _ in range(steps):
    step_pin_motor1.on()
    time.sleep(SPEED)
    step_pin_motor1.off()
    time.sleep(SPEED)
    

