#!/usr/bin/
#    PS4CONTROLLER PRGO
#       edited by yamauchi 
#       2021.5.10
import pygame
import time
'''
0 = SQUARE
1 = X
2 = CIRCLE
3 = TRIANG      LE
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
#define CONSTANT
ON = 1
OFF= 0
push_L1         = OFF
push_R1         = OFF
push_SQUARE     =OFF
push_CIRCLE     = OFF
push_TRIANGLE   = OFF
push_X          = OFF

speed_MAX_L =270  # 270/60/11.25 = 0.4 rps  24rpm
speed_MAX_M =540  #540/60/11.25 = 0.8 rps  48rpm
speed_MAX_H =1080 #108/60/11.25 = 1.6 rps  96rpm 

# define initial value
speed_Motor = speed_MAX_L
release_BTN = ON
count=0
stampsum = 0
stampsum2 = 0

pygame.init()

j = pygame.joystick.Joystick(0)
screen=pygame.display.set_mode((640,480))
j.init()
pygame.display.set_caption("MGV2 status")
oldtime = time.time()
try:
    while True:
        count += 1
        now=time.time()
        stamp = now - oldtime
        oldtime = now
        events = pygame.event.get()
        for event in events:
            # Set Button Status
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(0):
                    #print('SQUARE')
                    push_SQUARE = ON
                elif j.get_button(1):
                    #print('X')
                    push_X = ON
                elif j.get_button(2):
                    #print('Circl')
                    push_CIRCLE = ON
                elif j.get_button(3):
                    #print('Triagnel')
                    push_TRIANGLE = ON
                else:
                    #print("push other button")
                    pass
                if j.get_button(4) and push_R1 != ON:
                    #print('L1')
                    push_L1 = ON
                    push_R1 = OFF
                if j.get_button(5) and push_L1 != ON:
                    #print("R1")
                    push_L1 = OFF
                    push_R1 = ON
                else:
                    #print('other')
                    pass
            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")
                print(event.button)
                release_BTN         = ON
                if event.button == 0:
                    push_SQUARE     = OFF
                elif event.button == 1:
                    push_X          = OFF
                    speed_Motor     = speed_MAX_L
                elif event.button == 2:
                    push_CIRCLE     = OFF
                    speed_Motor     = speed_MAX_M
                elif event.button == 3:
                    push_TRIANGLE   = OFF
                    speed_Motor     = speed_MAX_H
                if event.button == 4:
                    push_L1         = OFF
                if event.button == 5:
                    push_R1         = OFF
            

        # set jostick valuse   

        forward_joystickL = int(j.get_axis(1)* -100)  # left forward/back
        forward_joystickR = int(j.get_axis(5)* -100)
        side_joystickL    = int(j.get_axis(0)*100) # left right/left
        side_joystickR    = int(j.get_axis(2)*100) #Right side by side
        ##print(side_joystickL,' ',side_joystickR,' ', forward_joystickL, ' ' , forward_joystickR)
        stampsum += stamp
        if not(count % 100):
            stampsum2  = stampsum
            stampsum2 /= 100
            stampsum = 0

        
        # Display
        screen.fill((0,0,0))
        font = pygame.font.SysFont("hg明朝ehgp明朝ehgs明朝e", 36)
        strings=font.render("GO/BACK: "+str(forward_joystickL),True, (255,255,255))
        screen.blit(strings,(10,40))
        strings=font.render("LEFT/RIGHT: "+str(side_joystickL),True, (255,255,255))
        screen.blit(strings,(300,40))
        strings=font.render(format(stampsum2,'.4f'),True, (255,255,255))
        screen.blit(strings,(10,100))
        if push_L1 == ON:
            strings=font.render("L1_BTN : ON",True,  (255,255,255))
        else:
            strings=font.render("L1_BTN : OFF",True, (255,255,255))
        screen.blit(strings,(10,140))
        if push_R1 == ON:
            strings=font.render("R1_BTN : ON",True,  (255,255,255))
        else:
            strings=font.render("R1_BTN : OFF",True, (255,255,255))
        screen.blit(strings,(300,140))
        strings=font.render("Speed  : "+str(speed_Motor),True, (255,255,255))
        screen.blit(strings,(10,180))        

        pygame.display.update()  

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()