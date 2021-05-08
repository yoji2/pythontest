import pygame

'''
0 = SQU ARE
1 = X
2 = CIRCLE
3 = TRIANGLE
4 = L1
5 = R1yoj
6 = L2
7 = R2
8 = SHARE
9 = OPTIONS
10 = LEFT ANALOG PRESS
11 = RIGHT ANALOG PRESS
12 = PS4 ON BUTTON
13 = TOUCHPAD PRESS
'''

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

try:
    while True:
        events = pygame.event.get()
        for event in events:
            
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(0):
                    print('SQUAE')
                elif j.get_button(1):
                    print('X')
                elif j.get_button(2):
                    print('Circl')
                elif j.get_button(3):
                    print('Triagnel')
                elif j.get_button(4):
                    print('L1')
                else:
                    print('other')
                forward_joystickL = int(j.get_axis(1)*100) # left forward/back
                forward_joystickR = int(j.get_axis(5)*100)
                side_joystickL    = int(j.get_axis(0)*100)
                side_joystickR    = int(j.get_axis(2)*100) #Right side by side
                print(side_joystickL,' ',side_joystickR,' ', forward_joystickL, ' ' , forward_joystickR)
            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")
            

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
