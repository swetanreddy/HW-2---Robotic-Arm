from machine import Pin, I2C
import time

#motor-1 
step_pin_motor1 = Pin(25, Pin.OUT)
dir_pin_motor1 = Pin(26, Pin.OUT)

#motor-2
step_pin_motor2 = Pin(27, Pin.OUT)
dir_pin_motor2 = Pin(14, Pin.OUT)

steps_per_revolution = 200
speed = 0.01


direction_motor1 = 1
degrees_to_rotate_motor1 = 90
steps_to_rotate_motor1 = int((degrees_to_rotate_motor1 / 360) * steps_per_revolution)

dir_pin_motor1.value(direction_motor1)


direction_motor2 = 0
degrees_to_rotate_motor2 = 45
steps_to_rotate_motor2 = int((degrees_to_rotate_motor2 / 360) * steps_per_revolution)

dir_pin_motor2.value(direction_motor2)


if steps_to_rotate_motor1 > steps_to_rotate_motor2:
    for i in range(steps_to_rotate_motor1):
        step_pin_motor1.on()
        time.sleep(speed)
        step_pin_motor1.off()
        time.sleep(speed)
        if(i <= steps_to_rotate_motor2):
            step_pin_motor2.on()
            time.sleep(speed)
            step_pin_motor2.off()
            time.sleep(speed)
        else:
            step_pin_motor2.off()
            time.sleep(speed)

else:
    for i in range(steps_to_rotate_motor2):
        step_pin_motor2.on()
        time.sleep(speed)
        step_pin_motor2.off()
        time.sleep(speed)
        if(i <= steps_to_rotate_motor1):
            step_pin_motor1.on()
            time.sleep(speed)
            step_pin_motor1.off()
            time.sleep(speed)
        else:
            step_pin_motor1.off()
            time.sleep(speed)


step_pin_motor1.off()
dir_pin_motor1.off()
step_pin_motor2.off()
dir_pin_motor2.off()