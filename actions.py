import os, sys
from wallaby import *
import constants as c
from utils import *
from drive import *


def driveSquare():
    print ("driving in a square")
    for x in range(0, 3):  # repeated 3 times
        drivetimed(95, 100, 1000)
        drivetimed(100, 0, 1140)  # turn right   #1300 if running on carpet
        drivetimed(0, 0, 100)
        msleep(500)
    print ("waiting for button")
    drivetimed(95, 100, 1000)
    drivetimed(100, 0, 1050)  # end of square routine
    freeze(c.leftmotor)
    wait_for_button()


def grabSodaCan():
    print ("starting soda can routine")
    enable_servos()    #need parentheses to execute function
    set_servo_position(c.servo_claw, c.claw_open)
    msleep(500)
    set_servo_position(c.servo_clawarm, c.clawarm_sodagrab)
    msleep(500)
    drivetimed(92, 100, 1200)
    drivetimed(0, 0, 100)
    msleep(100)
    set_servo_position(c.servo_claw, c.claw_sodagrab)
    print ("soda can grabbed")
    msleep(500)
    set_servo_position(c.servo_clawarm, c.clawarm_up)
    msleep(1000)
    drivetimed(95, 100, 1000)

def sensorCanGrab():
    print ("line following & grabbing can")
    set_servo_position(c.servo_clawarm, c.clawarm_straightup)
    msleep(1000)
    set_servo_position(c.servo_claw, c.claw_close)
    msleep(1000)
    lineFollowUntilCan()
    freeze(c.leftmotor)
    freeze(c.rightmotor)
    msleep(1000)
    print ("grabbing soda can")
    set_servo_position(c.servo_claw, c.claw_open)
    msleep(500)
    drivetimed(-50, -50, 1000)
    set_servo_position(c.servo_clawarm, c.clawarm_sodagrab)
    msleep(1000)
    drivetimed(20, 20, 1500)
    set_servo_position(c.servo_claw, c.claw_sodagrab)

def cameraCanGrab():
    print ("camera can grab code")
    while True:
        camera_update()
        #print (get_object_count(c.red))
        x = get_object_center_x(c.red, 0)
        print (x)
        if x >= 70 and x <= 90:
            print ("centered")