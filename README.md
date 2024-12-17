# Sandcrawler Invention Overview

## Summary
A Raspberry Pi-powered sandcrawler robot controlled via a wired NES controller. The robot uses motors for movement, and its behavior can be customized by pressing buttons and using the directional pad of the NES controller. The project leverages both hardware and software components to create a fun and interactive robot.

## How the Project Works

This project uses a Raspberry Pi to control a sandcrawler robot, which is driven by two motors (one for each wheel). The robot is powered by a Qwiic SCMD motor driver, and the movement is controlled using a wired NES controller via Pygame. The program listens for button presses and joystick movements from the controller to control the speed and direction of the robot.

### The system consists of:
- Two motors (left and right) connected to the motor driver.
- A wired NES controller connected to the Raspberry Pi.
- A Python program that reads inputs from the controller and adjusts the motors' speeds accordingly.

## Components Needed
- **Raspberry Pi** (with Raspbian OS installed)
- **Qwiic SCMD Motor Driver** (for controlling motors)
- **Two DC motors** (to drive the sandcrawler wheels)
- **NES controller** (wired or using an adapter for Raspberry Pi)
- **Jumper wires**
- **Breadboard** (optional, for testing connections)
- **Power supply** for the Raspberry Pi and motors
- **Motor connectors**
- **Python 3** installed on Raspberry Pi
- **Pygame library** (for joystick handling)

## Plan

### Concrete Steps:
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
   - Adjust motor speeds based on vertical and horizontal joystick movements.

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
- **Vertical movement** can be further developed to adjust the speed forward or backward.
- **Button A** increases the speed of both motors, while **Button B** decreases it.

### Turning Logic:
The left and right turns are controlled by horizontal joystick movements. When the joystick is pushed to the right or left, the corresponding motor speed is adjusted to simulate a turn. The robot turns left by reducing the speed of the left motor or by reducing the right motor speed for a right turn.

### Program Termination:
The program will clean up when exited (either manually or by a keyboard interrupt) by setting the motor speeds to zero and disabling the motor driver.

## Example Test Cases:

1. **Test Motor Movement:**
   - Press the **A** button: The robot should increase its speed by 75 units, and move forward.
   - Press the **B** button: The robot should decrease its speed by 75 units, and move backward.

2. **Test Turning:**
   - Push the joystick **right**: The robot should start turning right (left motor slows down or stops, right motor speeds up).
   - Push the joystick **left**: The robot should start turning left (right motor slows down or stops, left motor speeds up).

3. **Test Joystick Dead Zones:**
   - Ensure that small joystick movements do not cause unintended behavior. Movements should only register if the joystick is pushed beyond a threshold (±0.05).

4. **Test System Shutdown:**
   - Press the **Start** or **Select** button to verify that no unintended changes happen during a pause in controller input.

## Resources:
- [Qwiic SCMD Motor Driver](https://www.sparkfun.com/products/15187)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Raspberry Pi Setup Guide](https://www.raspberrypi.org/documentation/)
- [NES Controller to USB Adapter](https://www.amazon.com/USB-Controller-NES-Adapter-Classic/dp/B00AQM2TO6)
