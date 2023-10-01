import machine
import time

# Define the GPIO pins connected to the stepper motor driver
step_pin = machine.Pin(16, machine.Pin.OUT)  # GPIO14 for STEP
dir_pin = machine.Pin(17, machine.Pin.OUT)   # GPIO15 for DIR

# Define the stepper motor parameters
steps_per_rev = 200  # Number of steps per revolution for your stepper motor
delay = 0.001         # Delay between steps (adjust as needed for your motor)

# Set the initial direction (0 for clockwise, 1 for counter-clockwise)
dir_pin.value(0)

# Function to move the stepper motor a specified number of steps
def move_stepper(steps, direction):
    dir_pin.value(direction)
    for _ in range(steps):
        step_pin.value(1)
        time.sleep(delay)
        step_pin.value(0)
        time.sleep(delay)

# Example usage
try:
    while True:
        # Rotate 360 degrees clockwise (one full revolution)
        move_stepper(steps_per_rev, direction=0)

        # Pause for a while
        time.sleep(1)

        # Rotate 360 degrees counter-clockwise
        move_stepper(steps_per_rev, direction=1)

        # Pause for a while
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Turn off the stepper motor
step_pin.value(0)
