import math

def inverse_kinematics(x, y):

    m = 120
    n = 60
    L1 = 120
    L2 = 140

    R1 = round(math.sqrt(y**2 + (n - x)**2), 2)
    R2 = round(math.sqrt(y**2 + (n + x)**2), 2)
    
    a1 = round(math.degrees(math.acos((L1**2 + R1**2 - L2**2) / (2 * L1 * R1))), 2) 
    a2 = round(math.degrees(math.acos((L1t**2 + R2**2 - L2**2) / (2 * L1 * R2))), 2)
    
    b1 = round(math.degrees(math.acos((m**2 + R1**2 - R2**2) / (2 * m * R1))), 2)
    b2 = round(math.degrees(math.acos((m**2 + R2**2 - R1**2) / (2 * m * R2))), 2)
        
    theta1 = round(a1 + b1, 2)
    theta2 = round(a2 + b2, 2)
    
    return R1, R2, a1, a2, b1, b2, theta1, theta2

# Example usage:
x = 60
y = 30

R1, R2, a1, a2, b1, b2, theta1, theta2 = calculate_values(x, y)

# print(f"R1: {R1}, R2: {R2}")
# print(f"a1: {a1}, a2: {a2}")
# print(f"b1: {b1}, b2: {b2}")
print(f"theta1: {theta1}, theta2: {theta2}")


from machine import Pin
import time

step_pin = Pin(12, Pin.OUT)
dir_pin = Pin(13, Pin.OUT)

steps_per_revolution = 200
speed = 0.01
direction = 1
degrees_to_rotate = 90
steps_to_rotate = int((degrees_to_rotate / 360) * steps_per_revolution)

dir_pin.value(direction)

for _ in range(steps_to_rotate):
    step_pin.on()
    time.sleep(speed)
    step_pin.off()
    time.sleep(speed)

step_pin.off()
dir_pin.off()
