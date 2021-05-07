import pygame
import time
'''
0 = SQUARE
1 = X
2 = CIRCLE
3 = TRIANGLE
4 = L1
5 = R1
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
screen=pygame.display.set_mode((640,480))
j.init()
pygame.display.set_caption("MGV2 status")
oldtime = time.time()
try:
    while True:
        now=time.time()
        stamp = now - oldtime
        oldtime = now
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
        

            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")
            
        screen.fill((0,0,0))
        forward_joystickL = int(j.get_axis(1)*100) # left forward/back
        font = pygame.font.SysFont("hg明朝ehgp明朝ehgs明朝e", 36)
        strings=font.render(str(forward_joystickL),True, (255,255,255))
        screen.blit(strings,(10,40))
        forward_joystickR = int(j.get_axis(5)*100)
        side_joystickL    = int(j.get_axis(0)*100)
        side_joystickR    = int(j.get_axis(2)*100) #Right side by side
        print(side_joystickL,' ',side_joystickR,' ', forward_joystickL, ' ' , forward_joystickR)
        strings=font.render(str(stamp),True, (255,255,255))
        screen.blit(strings,(10,120))
        pygame.display.update() 
            

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()