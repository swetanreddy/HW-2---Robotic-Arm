import math

def calculate_values(x, y, m, n, L1_constant, L2_constant):
    R1 = math.sqrt(y**2 + (n - x)**2)
    R2 = math.sqrt(y**2 + (n + x)**2)
    
    a1 = math.acos((L1_constant**2 + R1**2 - L2_constant**2) / (2 * L1_constant * R1))
    a2 = math.acos((L1_constant**2 + R2**2 - L2_constant**2) / (2 * L1_constant * R2))
    
    b1 = math.acos((m**2 + R1**2 - R2**2) / (2 * m * R1))
    b2 = math.acos((m**2 + R2**2 - R1**2) / (2 * m * R2))
    
    L1 = math.sqrt(R1**2 + m**2)
    L2 = math.sqrt(R2**2 + m**2)
    
    theta1 = a1 + b1
    theta2 = a2 + b2
    
    return R1, R2, L1, L2, a1, a2, b1, b2, theta1, theta2

# Constants
m = 4
n = 5
L1_constant = 6
L2_constant = 7

# Example usage:
x = 60
y = 30

R1, R2, L1, L2, a1, a2, b1, b2, theta1, theta2 = calculate_values(x, y, m, n, L1_constant, L2_constant)

print(f"R1: {R1}, R2: {R2}, L1: {L1}, L2: {L2}")
print(f"a1: {math.degrees(a1)}, a2: {math.degrees(a2)}")
print(f"b1: {math.degrees(b1)}, b2: {math.degrees(b2)}")
print(f"theta1: {math.degrees(theta1)}, theta2: {math.degrees(theta2)}")
