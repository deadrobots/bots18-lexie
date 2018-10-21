import os, sys
from wallaby import *
import constants as c

# Be consistent with your naming conventions. This name should be in camelCase -LMB
def drivetimed(lspeed, rspeed, time):
    motor(c.leftmotor, lspeed)
    motor(c.rightmotor, rspeed)
    msleep(time)
    ao()


def lineFollowUntilCan():
    print ("line following")
    while analog(c.ET) < 2000:
        if analog(c.tophat) < 1200:  # on white
            motor(c.leftmotor, 10)
            motor(c.rightmotor, 100)
        else:   #on black
            motor(c.leftmotor, 100)
            motor(c.rightmotor, 10)