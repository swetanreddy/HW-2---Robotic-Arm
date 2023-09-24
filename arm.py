import math

def calculate_values(x, y):

    m = 120
    n = 60
    L1_constant = 120
    L2_constant = 140

    R1 = round(math.sqrt(y**2 + (n - x)**2), 2)
    R2 = round(math.sqrt(y**2 + (n + x)**2), 2)
    
    a1 = round(math.degrees(math.acos((L1_constant**2 + R1**2 - L2_constant**2) / (2 * L1_constant * R1))), 2) 
    a2 = round(math.degrees(math.acos((L1_constant**2 + R2**2 - L2_constant**2) / (2 * L1_constant * R2))), 2)
    
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
