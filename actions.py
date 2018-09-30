import os, sys
from wallaby import *
import constants as c
import utils as u


def driveSquare():
    print ("driving in a square")
    for x in range(0, 3):  # repeated 3 times
        u.drivetimed(95, 100, 1000)  #u. added because drivetimed and wait_for_button were moved to new file: utils
        u.drivetimed(100, 0, 1140)  # turn right   #1300 if running on carpet
        u.drivetimed(0, 0, 100)
        msleep(500)
    print ("waiting for button")
    u.drivetimed(95, 100, 1000)
    u.drivetimed(100, 0, 1050)  # end of square routine
    freeze(c.leftmotor)
    u.wait_for_button()


def grabSodaCan():
    print ("starting soda can routine")
    enable_servos()    #need parentheses to execute function
    set_servo_position(c.servo_claw, c.claw_open)
    msleep(500)
    set_servo_position(c.servo_clawarm, c.clawarm_sodagrab)
    msleep(500)
    u.drivetimed(92, 100, 1200)
    u.drivetimed(0, 0, 100)
    msleep(100)
    set_servo_position(c.servo_claw, c.claw_close)
    print ("soda can grabbed")
    msleep(500)
    set_servo_position(c.servo_clawarm, c.clawarm_up)
    msleep(1000)
    u.drivetimed(95, 100, 1000)
