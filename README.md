# Sandcrawler Invention Overview

### Summary:
A Raspberry Pi-powered sandcrawler robot controlled via a wired NES controller. The robot uses motors for movement, and its can be turned via the left and right arrow keys, while the a and b buttons control the speed of the motors.

### How the Project Works:
This project uses a Raspberry Pi to control a sandcrawler robot, which is driven by two motors (one for each wheel). The robot is powered by a Qwiic SCMD motor driver, and the movement is controlled using a wired NES controller via Pygame. The program listens for button presses and joystick movements from the controller to control the speed and direction of the robot.

### The system consists of:
- Two motors connected to the motor driver which is connected to a pihat ontop of a Rasberry Pi.
- A wired NES controller connected to the Raspberry Pi.
- A Python program that reads inputs from the controller and adjusts the motors' speeds accordingly.

### Components Needed:
- **Raspberry Pi** (with Raspbian OS installed)
- **Qwiic SCMD Motor Driver** (for controlling motors)
- **Two DC motors** (to drive the sandcrawler wheels)
- **NES controller** (wired or using an adapter for Raspberry Pi)
- **Jumper wires**
- **Battery** for the Raspberry Pi power source
- **Python 3** installed on Raspberry Pi
- **Pygame library** (for joystick handling)

### Plan:
1. **Setup Raspberry Pi:**
   - Install the Raspbian OS on the Raspberry Pi.
   - Install Pygame and Qwiic SCMD libraries on the Raspberry Pi.

2. **Wire the Motors:**
   - Connect the two DC motors to the Qwiic SCMD motor driver.
   - Ensure proper wiring for motor power and direction control.

3. **Connect NES Controller:**
   - Use an NES-to-USB adapter or connect a direct wired NES controller to the Raspberry Pi.

4. **Write Python Code:**
   - Import required libraries (`time`, `sys`, `qwiic_scmd`, and `pygame`).
   - Set up motor control using the Qwiic SCMD library, and define motor movement functions (`runLeft`, `runRight`).
   - Implement the `controller` function to process NES controller inputs for movement and speed adjustments.

5. **Test Motors and Controller:**
   - Test motor control by using the NES controller buttons to increase/decrease speed and change direction.
   - Adjust motor speeds based on horizontal joystick movements.

6. **Final Integration:**
   - Assemble the hardware onto a frame to resemble the "sandcrawler" robot.
   - Test the robot for smooth movement, response to button presses, and turning via joystick inputs.

7. **Debug and Refine:**
   - Fix any issues in responsiveness or behavior.
   - Fine-tune motor control for more precise movement.

## Explanation of the Code

### Motor Setup:
The code initializes the motor driver using the `qwiic_scmd` library. It sets up the motors by calling `motorDriver.set_drive()` to control the motor speed and direction. If no connection to the motor driver is found, the program will exit with an error message.

### Motor Control Functions:
- The functions `runLeft(speed_left)` and `runRight(speed_right)` control the left and right motors based on input speed values. Depending on whether the speed is positive or negative, the motors will rotate forward or backward.
- `motorDriver.set_drive()` is called within these functions to change the motor states.

### Controller Setup:
The `controller()` function initializes Pygame for joystick handling. It listens for joystick movements (horizontal and vertical) and button presses (A, B, Start, Select) from the NES controller. The movement is processed as follows:
- **Horizontal movement** (left/right) adjusts the motor speeds to turn the robot.
- **Vertical movement** can be further developed
- **Button A** increases the speed of both motors, while **Button B** decreases it **Menu Buttons** could be used for extra functionality 

### Turning Logic:
The left and right turns are controlled by horizontal joystick movements. When the joystick is pushed to the right or left, the motors are set to different speeds to make a turn. The robot turns left by reducing the speed of the left motor or by reducing the right motor speed for a right turn.

### Program Termination:
The program will clean up when exited (by a keyboard interrupt) by setting the motor speeds to zero, disabling the motor driver, and disabling pygame.


