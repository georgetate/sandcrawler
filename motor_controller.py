import time
import sys
import qwiic_scmd
import pygame



# setting up motors
motorDriver = qwiic_scmd.QwiicScmd()
R_MTR = 1
L_MTR = 0

# Zero Motor Speeds
motorDriver.set_drive(0,0,0)
motorDriver.set_drive(1,0,0)

# Check Motors
if motorDriver.connected == False:
    print("Motor Driver not connected. Check connections.", file=sys.stderr)
    sys.exit(1)

# Enable Motors
motorDriver.begin()
print("Motor initialized.")
time.sleep(.25)
motorDriver.enable()
print("Motor enabled")
time.sleep(.25)



def runLeft(speed_left):
    FWD = 1
    BWD = 0
    if speed_left < 0:
        motorDriver.set_drive(L_MTR, BWD, abs(speed_left))
    else:
        motorDriver.set_drive(L_MTR, FWD, speed_left)
    
    print(f"Left Motor: {speed_left}")



def runRight(speed_right):
    FWD = 0
    BWD = 1
    if speed_right < 0:
        motorDriver.set_drive(R_MTR, BWD, abs(speed_right))
    else:
        motorDriver.set_drive(R_MTR, FWD, speed_right)

    print(f"Right Motor: {speed_right}")



def controller():
    # Initialize Pygame
    pygame.init()

    # Joystick setup
    pygame.joystick.init()
    joysticks = []

    # Controller loop
    current_speed = 0
    run = True
    while run:
        time.sleep(.05)
        runRight(current_speed)
        runLeft(current_speed)
    # Event handler
        for event in pygame.event.get():
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joy.init()
                joysticks.append(joy)

            elif event.type == pygame.JOYDEVICEREMOVED:
                joy_id = event.device_index

                joysticks = [joy for joy in joysticks if joy.get_id() != joy_id]
            elif event.type == pygame.QUIT:
                run = False
        

    # Joystick input handling
        for joystick in joysticks:
            # Button setup
            button_start = joystick.get_button(9)
            button_select = joystick.get_button(8)
            button_b = joystick.get_button(2)
            button_a = joystick.get_button(1)

            # Arrowkey setup
            horiz_move = joystick.get_axis(0)
            vert_move = joystick.get_axis(1)


        # Changing motor speed with buttons
            if button_a and current_speed < 220:
                current_speed += 75
                runRight(current_speed)
                runLeft(current_speed)
                time.sleep(.2)

            elif button_b and current_speed > -220:
                current_speed -= 75
                runRight(current_speed)
                runLeft(current_speed)
                time.sleep(.2)

            elif button_start:
                pass

            elif button_select:
                pass
            
        # Turning with arrowkeys
            # Turn right
            if horiz_move > 0.05:
                if current_speed >= 0:
                    runRight(current_speed - 75)
                    runLeft(current_speed)
                    time.sleep(.05)
                elif current_speed < 0:
                    runRight(current_speed + 75)
                    runLeft(current_speed)

            # Turn left
            elif horiz_move < -0.05:
                if current_speed >= 0:
                    runRight(current_speed)
                    runLeft(current_speed - 75)
                    time.sleep(0.05)
                elif current_speed < 0:
                    runRight(current_speed)
                    runLeft(current_speed + 75)

            elif vert_move > 0.05:
                pass

            elif vert_move < -0.05:
                pass



if __name__ == '__main__':
    try:
        controller()
        sys.exit(0)
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nShutting down")
        # Zero Motor Speeds
        motorDriver.set_drive(0,0,0)
        motorDriver.set_drive(1,0,0)
        motorDriver.disable()
        pygame.quit()
        sys.exit(0)
