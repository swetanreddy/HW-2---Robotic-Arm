from machine import Pin
import time

step_pin = Pin(16, Pin.OUT)
dir_pin = Pin(17, Pin.OUT)

steps_per_revolution = 200
speed = 0.001
direction = 1
degrees_to_rotate = 45
steps_to_rotate = int((degrees_to_rotate / 360) * steps_per_revolution)

dir_pin.value(direction)

for _ in range(steps_to_rotate):
    step_pin.on()
    time.sleep(speed)
    step_pin.off()
    time.sleep(speed)

step_pin.off()
dir_pin.off()