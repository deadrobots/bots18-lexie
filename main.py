#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import actions as act

# I like the init() function
# You've got some good naming conventions, but you need to be more
# consistent. c.leftmotor should be c.leftMotor, and so on
# Great code, otherwise! Excellent use of constants
# -LMB

def init():
    enable_servos()
    camera_open_black()


def main():
    print "Hello World"
    init()
    #act.driveSquare()
    #act.grabSodaCan()
    #act.sensorCanGrab()
    act.cameraCanGrab()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();

#completed line follow until soda can and grabbed soda can at end of routine

