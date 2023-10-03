import time
import math
from machine import Pin

# letter_coordinates = {
#     'A' : [(1, 1), (3, 6), (5, 11), (7, 6), (9, 1), (7, 6), ((3, 6))],
#     'B' : [(1,1), (1,3.5), (1,6), (1,8.5), (1,11), (4,11), (7,11), (9,8.5), (9,6), (9,3.5), (7,1), (4,1), (1,1)],
#     'C' : [(9,3), (6.5,1), (3.5,1), (1,3), (1,6), (1,9), (3.5,11), (6.5,11), (9,9)],
#     'D' : [(1,1), (1,3.5), (1,6), (1,8.5), (1,11), (4,11), (7,11), (9,8.5), (9,6), (9,3.5), (7,1), (4,1), (1,1)],
#     'E' : [(9,1), (6.2,1),(3.6,1),(1,1),(1,3.5),(1,6),(3.6,6),(6,6),(3.6,6),(1,6),(1,8.5),(1,11),(3.6,11),(6.2,11),(9,11)],
#     'F' : [(1,1),(1,3.5),(1,6),(3.6,6),(6,6),(3.6,6),(1,6),(1,8.5),(1,11),(3.6,11),(6.2,11),(9,11)],
#     'G' : [],  # Fill in the coordinates for 'G'
#     'H' : [(1,1), (1,3.5), (1,6), (1,8.5),(1,11),(1,1), (1,1), (1,6),(3.6,6),(6,6),(9,6),(1,1),(1,1),(9,11),(9,8.5),(9,6),(9,3.5),(9,1)],
#     'I' : [(1,1),(5,1),(9,1),(5,1),(5,3.5),(5,6),(5,8.5),(5,11),(1,11),(5,11),(9,11)],
#     'J' : [(1,11),(5,11),(9,11),(5,11),(5,8.5),(5,6),(5,3.5),(5,1),(1,3.5)],
#     'K' : [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(1,1),(1,1),(1,6),(1,6),(5,8.5),(9,11),(1,1),(1,1),(9,1),(9,1),(5,3.5),(9,1)],
#     'L' : [(1,11),(1,8.5),(1,6),(1,3.5),(1,1),(5,1),(9,1)],
#     'M' : [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(3,8.5),(5,6),(7,8.5),(9,11),(9,8.5),(9,6),(9,3.5),(9,1)],
#     'N' : [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(3,8.5),(5,6),(7,3.5),(9,1),(9,3.5),(9,6),(9,8.5),(9,11)],
#     'O' : [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(3,11),(5,11),(7,11),(9,11),(9,8.5),(9,6),(9,3.5),(9,1),(7,1),(5,1),(3,1),(1,1)],
#     'P' : [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(3,11),(5,11),(7,11),(9,11),(9,8.5),(9,6),(7,6),(5,6),(3,6),(1,6)],
#     'Q' : [],  # Fill in the coordinates for 'Q'
#     'R' : [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(3,11),(5,11),(7,11),(9,11),(9,8.5),(9,6),(7,6),(5,6),(3,6),(1,6),(3,6),(5,6),(7,3.5),(9,1)],
#     'S' : [(1,1),(3,1),(5,1),(7,1),(9,1),(9,3.5),(9,6),(7,6),(5,6),(3,6),(1,6),(1,8.5),(1,11),(3,11),(5,11),(7,11),(9,11)],
#     'T' : [(1,11),(3,11),(5,11),(7,11),(9,11),(7,11),(5,11),(5,8.5),(5,6),(5,3.5),(5,1)],
#     'U' : [(1,11),(1,8.5),(1,6),(1,3.5),(1,1),(3,1),(5,1),(7,1),(9,1),(9,3.5),(9,6),(9,8.5),(9,11)],
#     'V' : [(1,11),(1,8.5),(1,6),(3,3.5),(5,1),(7,3.5),(9,6),(9,8.5),(9,11)],
#     'W' : [(1,11),(1,8.5),(1,6),(1,3.5),(1,1),(3,3.5),(5,6),(7,3.5),(9,1),(9,3.5),(9,6),(9,8.5),(9,11)],
#     'X' : [(1,11),(3,8.5),(5,6),(7,3.5),(9,1),(1,1),(9,11),(1,1),(9,11),(1,11),(9,1)],
#     'Y' : [(1,1),(3,8.5),(5,6),(7,8.5),(9,11),(1,1),(9,11),(1,1),(5,3.5),(9,1)],
#     'Z' : [(1,11),(3,11),(5,11),(7,11),(9,11),(7,8.5),(5,6),(3,3.5),(1,1),(3,1),(5,1),(7,1),(9,1)]
# }


letter_coordinates = {
    'A' : [(1, 1), (3, 6), (5, 11), (7, 6), (9, 1), (7, 6), (3, 6)],
    'B': [(1,1), (1,3.5), (1,6), (1,8.5), (1,11), (4,11), (7,11), (9,8.5), (9,6), (9,3.5), (7,1), (4,1), (1,1)],
    'C': [(9,3), (6.5,1), (3.5,1), (1,3), (1,6), (1,9), (3.5,11), (6.5,11), (9,9)],
    'D': [(1,1), (1,3.5), (1,6), (1,8.5), (1,11), (4,11), (7,11), (9,8.5), (9,6), (9,3.5), (7,1), (4,1), (1,1)],
    'E': [(9,1), (6.2,1),(3.6,1),(1,1),(1,3.5),(1,6),(3.6,6),(6,6),(3.6,6),(1,6),(1,8.5),(1,11),(3.6,11),(6.2,11),(9,11)],
    'F': [(1,1),(1,3.5),(1,6),(3.6,6),(6,6),(3.6,6),(1,6),(1,8.5),(1,11),(3.6,11),(6.2,11),(9,11)],
    'G': [],  # Fill in the coordinates for 'G', including (d,d) and (l,l)
    'H': [(1,1), (1,3.5), (1,6), (1,8.5),(1,11),(1,6),(3.6,6),(6,6),(9,6),(9,11),(9,8.5),(9,6),(9,3.5),(9,1)],
    'I': [(1,1),(5,1),(9,1),(5,1),(5,3.5),(5,6),(5,8.5),(5,11),(1,11),(5,11),(9,11)],
    'J': [(1,11),(5,11),(9,11),(5,11),(5,8.5),(5,6),(5,3.5),(5,1),(1,3.5)],
    'K': [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(1,6),(5,8.5),(9,11),(1,6),(5,3.5),(9,1)],
    'L': [(1,11),(1,8.5),(1,6),(1,3.5),(1,1),(5,1),(9,1)],
    'M': [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(3,8.5),(5,6),(7,8.5),(9,11),(9,8.5),(9,6),(9,3.5),(9,1)],
    'N': [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(3,8.5),(5,6),(7,3.5),(9,1),(9,3.5),(9,6),(9,8.5),(9,11)],
    'O': [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(3,11),(5,11),(7,11),(9,11),(9,8.5),(9,6),(9,3.5),(9,1),(7,1),(5,1),(3,1),(1,1)],
    'P': [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(3,11),(5,11),(7,11),(9,11),(9,8.5),(9,6),(7,6),(5,6),(3,6),(1,6)],
    'Q': [],  # Fill in the coordinates for 'Q', including (d,d) and (l,l)
    'R': [(1,1),(1,3.5),(1,6),(1,8.5),(1,11),(3,11),(5,11),(7,11),(9,11),(9,8.5),(9,6),(7,6),(5,6),(3,6),(1,6),(3,6),(5,6),(7,3.5),(9,1)],
    'S': [(1,1),(3,1),(5,1),(7,1),(9,1),(9,3.5),(9,6),(7,6),(5,6),(3,6),(1,6),(1,8.5),(1,11),(3,11),(5,11),(7,11),(9,11)],
    'T': [(1,11),(3,11),(5,11),(7,11),(9,11),(7,11),(5,11),(5,8.5),(5,6),(5,3.5),(5,1)],
    'U': [(1,11),(1,8.5),(1,6),(1,3.5),(1,1),(3,1),(5,1),(7,1),(9,1),(9,3.5),(9,6),(9,8.5),(9,11)],
    'V': [(1,11),(1,8.5),(1,6),(3,3.5),(5,1),(7,3.5),(9,6),(9,8.5),(9,11)],
    'W': [(1,11),(1,8.5),(1,6),(1,3.5),(1,1),(3,3.5),(5,6),(7,3.5),(9,1),(9,3.5),(9,6),(9,8.5),(9,11)],
    'X': [(1,11),(3,8.5),(5,6),(7,3.5),(9,1),(9,11),(7,8.5),(5,6),(3,3.5),(1,1)],
    'Y': [(1,1),(3,8.5),(5,6),(7,8.5),(9,11),(5,6),(5,3.5),(5,1)],
    'Z': [(1,11),(3,11),(5,11),(7,11),(9,11),(7,8.5),(5,6),(3,3.5),(1,1),(3,1),(5,1),(7,1),(9,1)]
}


#motor-1 
step_pin_motor1 = Pin(16, Pin.OUT)
dir_pin_motor1 = Pin(17, Pin.OUT)

motor1_ms1 = Pin(23, Pin.OUT)
motor1_ms2 = Pin(22, Pin.OUT)

motor2_ms1 = Pin(25, Pin.OUT)
motor2_ms2 = Pin(26, Pin.OUT)

# Initialize motor1 MS pins
motor1_ms1.value(1)
motor1_ms2.value(1)

# Initialize motor2 MS pins
motor2_ms1.value(1)
motor2_ms2.value(1)

#motor-2
step_pin_motor2 = Pin(18, Pin.OUT)
dir_pin_motor2 = Pin(19, Pin.OUT)


#solenoid
solenoid = Pin(4, Pin.OUT)

m = 8
n = m/2
L1 = 16
L2 = 20

STEPS_PER_REVOLUTION = 1600
SPEED = 0.01

def inverse_kinematics(x, y):
    R1 = math.sqrt(y**2 + (n - x)**2)
    R2 = math.sqrt(y**2 + (n + x)**2)
    
    a1 = math.degrees(math.acos((L1**2 + R1**2 - L2**2) / (2 * L1 * R1))) 
    a2 = math.degrees(math.acos((L1**2 + R2**2 - L2**2) / (2 * L1 * R2)))
    
    b1 = math.degrees(math.acos((m**2 + R1**2 - R2**2) / (2 * m * R1)))
    b2 = math.degrees(math.acos((m**2 + R2**2 - R1**2) / (2 * m * R2)))
        
    theta1 = a1 + b1
    theta2 = a2 + b2
    
    return theta1, theta2

def find_angle(character, n):
    
    values = letter_coordinates[character]
    angle_values = []
    for value in values:
        if str(value[0]) and str(value[1]) == "D":
            angle_values.append(("D","D"))
        elif str(value[0]) and str(value[1]) == "L":
            angle_values.append(("L","L"))
            pass
        else:
            angle_values.append(inverse_kinematics(value[0] - 10 + (n*5), value[1] + 12))
    
    return angle_values

   
def draw_motor_angle(angle_motor1, angle_motor2, direction1, direction2):
    steps_to_rotate_motor1 = int((angle_motor1 / 360) * STEPS_PER_REVOLUTION)
    steps_to_rotate_motor2 = int((angle_motor2 / 360) * STEPS_PER_REVOLUTION)
    dir_pin_motor1.value(direction1)
    dir_pin_motor2.value(direction2)

    print("current position: ", (angle_motor1, angle_motor2, direction1, direction2))
    max_steps = max(steps_to_rotate_motor1, steps_to_rotate_motor2)

    for i in range(max_steps):
        if i < steps_to_rotate_motor1:
            step_pin_motor1.on()
        if i < steps_to_rotate_motor2:
            step_pin_motor2.on()
        
        time.sleep(SPEED)
        step_pin_motor1.off()
        step_pin_motor2.off()
        time.sleep(SPEED)

char_input = input("enter initials: ")
input_initials = [char for char in char_input]
print(input_initials)

for i, initial in enumerate(input_initials):
    angles = find_angle(initial, i)
#     angles.append((90, 90))
    
    print(angles)

    new_angles = []
    for i, angle in enumerate(angles):
        if i == 0:
            new_theta1 = angle[0] - 90
            new_theta2 = angle[1] - 90
            direction1 = 0 if angle[0] > 90 else 1
            direction2 = 1 if angle[1] > 90 else 0
            new_angles.append((new_theta1, new_theta2, direction1, direction2))
        else:

                
            
            new_theta1 = angle[0] - angles[i-1][0]
            new_theta2 = angle[1] - angles[i-1][1]
            
            direction1 = 0 if new_theta1 > 0 else 1
            direction2 = 1 if new_theta2 > 0 else 0
            
            new_theta1 = abs(new_theta1)
            new_theta2 = abs(new_theta2)
            new_angles.append((new_theta1, new_theta2, direction1, direction2))

    print("new angles", new_angles)
    solenoid.value(1)
    for angle in new_angles:
        draw_motor_angle(*angle)
        time.sleep(0.1)
    solenoid.value(0)

step_pin_motor1.off()
dir_pin_motor1.off()
step_pin_motor2.off()
dir_pin_motor2.off()
