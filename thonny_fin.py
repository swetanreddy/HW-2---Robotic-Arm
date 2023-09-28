import math
from machine import Pin
import time

letters_map = {
    "A": [(0.5, 0.5), ("D", "D"), (0.69, 0.97), (0.85, 1.36), (1.03, 1.82), (1.17, 2.17), (1.3, 2.5), (1.47, 2.93), (1.64, 3.35), (1.8, 3.74), (1.98, 4.21), (2.15, 4.61), (2.31, 5.02), (2.5, 5.5), (2.7, 4.99), (2.85, 4.63), (3.01, 4.23), (3.17, 3.83), (3.3, 3.49), (3.43, 3.18), (3.58, 2.81), (3.7, 2.51), (3.81, 2.21), (3.97, 1.82), (4.14, 1.41), (4.31, 0.96), (4.5, 0.5), ("L", "L"),(3.7, 2.51), ("D", "D"), (3.26, 2.5), (2.75, 2.5), (2.25, 2.5), (1.72, 2.5), (1.3, 2.5), ("L", "L")],
#     "B": [(4.19, 7.83), (0.92, 8.23), (8.47, 4.67), (4.05, 6.69), (2.36, 8.84), (6.42, 5.07), (2.61, 3.16), (7.43, 4.55), (8.46, 0.82), (9.32, 4.98), (3.59, 8.48), (8.13, 7.4), (9.73, 0.56), (2.17, 4.4), (9.83, 3.81)],
#     "C": [(5.45, 1.08), (3.51, 4.27), (6.81, 0.38), (9.64, 8.69), (0.4, 6.39), (6.95, 9.19), (3.99, 3.83), (2.04, 6.53), (3.96, 6.17), (1.82, 9.2), (0.42, 5.92), (9.25, 6.2), (1.45, 4.29), (6.78, 5.44), (2.48, 6.62)],
#     "D": [(5.62, 9.69), (7.04, 9.17), (1.26, 9.99), (8.99, 2.04), (1.54, 7.26), (1.73, 2.5), (8.7, 0.65), (8.61, 2.4), (9.25, 1.24), (7.44, 9.64), (5.75, 2.95), (7.97, 4.18), (4.21, 0.44), (6.63, 3.04), (3.56, 0.56)],
#     "E": [(2.93, 2.48), (7.75, 8.71), (3.34, 6.93), (6.18, 7.58), (7.62, 7.75), (5.99, 4.42), (1.81, 6.16), (8.49, 7.07), (0.89, 7.72), (6.46, 2.56), (8.98, 3.65), (1.46, 8.7), (2.45, 7.28), (6.3, 2.61), (4.89, 3.07)],
#     "F": [(6.01, 2.04), (0.75, 8.47), (1.8, 2.64), (2.71, 7.24), (1.03, 9.98), (6.7, 1.46), (7.39, 4.51), (3.29, 6.76), (6.69, 9.85), (2.95, 4.73), (9.5, 9.84), (5.42, 8.21), (3.7, 2.12), (4.08, 5.42), (2.26, 8.08)],
#     "G": [(4.06, 8.76), (5.4, 4.5), (0.27, 3.44), (4.99, 9.46), (3.84, 9.03), (7.87, 1.48), (5.35, 9.11), (5.97, 6.26), (3.83, 2.71), (8.47, 8.66), (1.99, 4.06), (6.88, 3.25), (0.25, 0.01), (4.26, 1.03), (8.64, 5.62)],
#     "H": [(7.49, 3.31), (0.39, 6.02), (9.68, 5.87), (6.59, 5.76), (4.82, 4.11), (2.94, 4.8), (2.29, 8.6), (5.46, 1.72), (6.32, 0.72), (6.61, 8.95), (7.54, 7.46), (1.08, 6.56), (5.96, 5.85), (1.96, 2.21), (9.84, 5.11)],
#     "I": [(2.45, 7.0), (0.62, 8.17), (2.05, 0.98), (5.97, 0.85), (1.67, 9.34), (4.09, 6.74), (2.3, 8.18), (5.85, 3.77), (3.25, 3.86), (5.32, 8.13), (5.44, 2.68), (7.01, 1.91), (5.75, 9.95), (1.14, 6.87), (1.71, 3.68)],
#     "J": [(6.13, 5.35), (9.19, 7.45), (9.96, 3.92), (1.62, 5.04), (2.9, 0.43), (3.72, 1.66), (5.63, 1.81), (9.66, 0.92), (4.3, 6.94), (7.48, 6.58), (0.26, 4.28), (3.29, 0.82), (1.21, 7.19), (1.52, 4.54), (0.85, 5.35)],
#     "K": [(4.25, 3.57), (6.81, 8.49), (2.1, 2.87), (9.29, 0.98), (7.07, 9.12), (4.43, 2.32), (7.59, 7.03), (3.41, 4.13), (3.56, 6.2), (1.51, 1.57), (9.02, 6.11), (2.81, 2.87), (9.41, 2.0), (1.12, 3.65), (3.18, 0.51)],
#     "L": [(9.54, 8.47), (8.37, 7.39), (7.68, 3.21), (1.19, 6.58), (5.49, 5.81), (4.18, 7.15), (3.18, 1.84), (5.42, 8.66), (8.84, 9.68), (0.19, 2.42), (7.05, 7.5), (0.28, 6.66), (5.97, 0.9), (0.1, 2.9), (9.97, 6.2)],
#     "M": [(3.0, 0.53), (2.83, 5.27), (0.2, 6.91), (9.92, 6.19), (6.79, 1.16), (9.7, 9.76), (8.62, 6.45), (6.7, 8.95), (3.34, 9.75), (4.75, 8.26), (2.26, 0.27), (3.57, 3.19), (4.38, 2.02), (7.45, 3.26), (2.97, 6.48)],
    "N": [(0.5, 0.5), ("D", "D"), (0.5, 1), (0.5, 1.5), (0.5, 2), (0.5, 2.5), (0.5, 3), (0.5, 3.5), (0.5, 4), (0.5, 4.5), (0.5, 5), (0.5, 5.5), (0.89, 5.02), (1.24, 4.57), (1.52, 4.22), (1.84, 3.83), (2.13, 3.46), (2.43, 3.09), (2.76, 2.68), (3.06, 2.29), (3.36, 1.92), (3.75, 1.44), (4.09, 1.01), (4.5, 0.5), (4.5, 1), (4.5, 1.5), (4.5, 2), (4.5, 2.5), (4.5, 3), (4.5, 3.5), (4.5, 4), (4.5, 4.5), (4.5, 5), (4.5, 5.5), ("L", "L")],
#     "O": [(3.4, 0.94), (8.5, 2.69), (9.25, 0.95), (9.99, 7.68), (1.31, 0.48), (2.33, 8.07), (7.59, 5.1), (8.27, 6.41), (8.36, 8.72), (8.73, 2.67), (6.38, 6.09), (9.99, 1.66), (8.21, 1.45), (1.44, 1.62), (5.9, 7.18)],
#     "P": [(3.15, 9.29), (8.96, 4.18), (0.95, 0.05), (6.53, 9.21), (4.46, 8.86), (7.64, 2.66), (7.45, 3.71), (5.45, 1.93), (9.68, 0.89), (6.82, 0.02), (9.47, 3.44), (5.43, 5.66), (9.75, 1.76), (9.78, 3.17), (4.9, 2.62)],
#     "Q": [(3.25, 6.98), (0.52, 2.13), (5.11, 1.88), (3.58, 9.94), (3.31, 9.84), (2.23, 6.29), (4.1, 5.77), (6.19, 3.29), (6.94, 6.85), (2.37, 8.14), (0.61, 5.93), (3.2, 9.93), (0.17, 9.57), (3.56, 3.42), (5.87, 7.01)],
#     "R": [(8.97, 9.15), (5.69, 8.85), (6.28, 2.71), (2.05, 6.76), (7.12, 6.99), (6.78, 0.58), (4.08, 9.35), (0.56, 9.48), (0.79, 6.36), (7.34, 1.53), (7.38, 5.29), (5.29, 9.75), (2.48, 3.11), (1.45, 2.92), (5.56, 0.19)],
    "S": [(0.5, 0.5), ("D", "D"), (1, 0.5), (1.5, 0.5), (2, 0.5), (2.5, 0.5), (3, 0.5), (3.5, 0.5), (4, 0.5), (4.5, 0.5), (4.5, 1), (4.5, 1.5), (4.5, 2), (4.5, 2.5), (4.5, 3),(4, 3), (3.5, 3), (3, 3), (2.5, 3), (2, 3), (1.5, 3), (1, 3), (0.5, 3), (0.5, 3.5), (0.5, 4), (0.5, 4.5), (0.5, 5), (0.5, 5.5), (1, 5.5),   (1.5, 5.5), (2, 5.5), (2.5, 5.5), (3, 5.5), (3.5, 5.5), (4, 5.5), (4.5, 5.5), ("L", "L")],
#     "T": [(7.9, 8.3), (0.93, 7.89), (8.71, 5.71), (7.37, 3.3), (7.05, 7.02), (9.05, 9.9), (7.76, 4.62), (0.52, 1.38), (1.83, 0.14), (6.5, 5.47), (0.13, 6.62), (2.5, 6.75), (1.05, 5.47), (6.61, 8.16), (0.91, 9.4)],
#     "U": [(3.42, 5.63), (3.13, 3.47), (2.31, 2.73), (0.38, 9.77), (9.74, 2.79), (3.43, 4.96), (3.97, 9.5), (9.52, 5.06), (4.27, 8.19), (4.13, 9.26), (7.44, 6.18), (2.53, 4.17), (4.4, 6.82), (9.55, 9.14), (2.12, 6.82)],
#     "V": [(9.59, 4.03), (2.4, 0.87), (8.31, 3.81), (6.12, 9.97), (6.63, 6.82), (1.57, 9.7), (9.04, 1.59), (2.7, 9.26), (6.46, 8.26), (9.0, 7.34), (0.82, 1.03), (9.14, 7.35), (4.36, 3.33), (0.14, 7.07), (3.93, 9.87)],
#     "W": [(9.45, 4.24), (0.3, 7.28), (2.49, 7.21), (3.42, 6.06), (5.6, 3.45), (8.34, 1.15), (0.72, 8.43), (7.01, 2.53), (9.16, 5.6), (1.79, 3.01), (5.74, 2.56), (1.18, 4.99), (1.95, 6.94), (9.42, 9.68), (7.98, 3.94)],
#     "X": [(2.65, 3.49), (4.96, 9.19), (5.78, 9.83), (1.02, 7.69), (7.5, 4.89), (8.18, 5.02), (0.69, 1.96), (4.74, 9.7), (5.14, 5.66), (3.76, 9.52), (0.62, 3.68), (2.56, 6.53), (5.04, 4.52), (6.44, 1.21), (9.95, 8.61)],
#     "Y": [(3.34, 4.02), (8.38, 0.4), (5.4, 8.56), (9.3, 4.51), (9.02, 5.36), (7.6, 2.3), (9.1, 0.19), (5.56, 2.24), (6.28, 1.4), (0.89, 7.91), (8.99, 5.18), (1.35, 8.94), (4.17, 8.42), (8.15, 6.36), (7.71, 6.12)],
#     "Z": [(6.45, 9.23), (2.16, 8.42), (0.97, 0.4), (1.63, 1.2), (2.17, 4.33), (2.62, 7.18), (4.76, 2.21), (1.06, 1.94), (5.9, 6.29), (7.49, 0.24), (8.34, 8.61), (1.88, 8.81), (7.7, 7.8), (5.09, 0.22), (8.0, 1.72)],
}

m = 8
n = 4
L1 = 12
L2 = 16

def inverse_kinematics(x, y):

    R1 = round(math.sqrt(y**2 + (n - x)**2), 2)
    R2 = round(math.sqrt(y**2 + (n + x)**2), 2)
    
    a1 = round(math.degrees(math.acos((L1**2 + R1**2 - L2**2) / (2 * L1 * R1))), 2) 
    a2 = round(math.degrees(math.acos((L1**2 + R2**2 - L2**2) / (2 * L1 * R2))), 2)
    
    b1 = round(math.degrees(math.acos((m**2 + R1**2 - R2**2) / (2 * m * R1))), 2)
    b2 = round(math.degrees(math.acos((m**2 + R2**2 - R1**2) / (2 * m * R2))), 2)
        
    theta1 = round(a1 + b1, 2)
    theta2 = round(a2 + b2, 2)
    
    return theta1, theta2

def find_angle(character, n):
    values = letters_map[character]
    angle_values = []
    for i in range(len(values)):
        if str(values[i][0]) and str(values[i][1]) == "D":
            #servo  drop function
            pass
        elif str(values[i][0]) and str(values[i][1]) == "L":
            #servo lift function
            pass
        else:
            #shifting the origin
            changed_x = values[i][0] - 10 + (n*5)
            changed_y = values[i][1] + 9
            print("changed_x, changed_y", (changed_x, changed_y))
            theta1, theta2 = inverse_kinematics(changed_x, changed_y)
            angle_values.append((theta1, theta2))

    return angle_values

def draw_motor_angle(angle_motor1, angle_motor2, direction_of_motor1, direction_of_motor2):

    #motor-1 
    step_pin_motor1 = Pin(17, Pin.OUT)
    dir_pin_motor1 = Pin(16, Pin.OUT)

    #motor-2
    step_pin_motor2 = Pin(18, Pin.OUT)
    dir_pin_motor2 = Pin(19, Pin.OUT)

    steps_per_revolution = 200
    speed = 0.01
    
    steps_to_rotate_motor1 = int((angle_motor1 / 360) * steps_per_revolution)
    steps_to_rotate_motor2 = int((angle_motor2 / 360) * steps_per_revolution)
    dir_pin_motor1.value(direction_of_motor1)
    dir_pin_motor2.value(direction_of_motor2)

    print("current position: ", (angle_motor1, angle_motor2))

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

char_input = input("enter intials : ")
input_initials = [char for char in char_input]
print(input_initials)

for i in range(len(input_initials)):
    angles = find_angle(input_initials[i], i)
    print(angles)

    new_angles = []
            
    for i in range(len(angles)):
        if i == 0:
            new_theta1 = angles[i][0] - 90
            new_theta2 = angles[i][1] - 90
            new_angles.append((new_theta1, new_theta2, 0, 1))

        new_theta1 = angles[i][0]- angles[i-1][0]
        new_theta2 = angles[i][1]- angles[i-1][1]

        if new_theta1 > new_angles[i-1][0]:
            direction1 = 0
        else:
            direction1 = 1

        if new_theta2 > new_angles[i-1][1]:
            direction2 = 1
        else:
            direction2 = 0

        if new_theta1 < 0 :
            new_theta1 = -(new_theta1)

        if new_theta2 < 0 :
            new_theta2 = -(new_theta2)
        
        new_angles.append((new_theta1, new_theta2, direction1, direction2))

    print("new angles", new_angles)

    for angle in new_angles:
        draw_motor_angle(angle[0], angle[1], angle[2], angle[3])
        time.sleep(0.5)
        