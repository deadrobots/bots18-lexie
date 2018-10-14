#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import actions as act


def init():
    enable_servos()


def main():
    print "Hello World"
    init()
    #act.driveSquare()
    #act.grabSodaCan()
    act.sensorCanGrab()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();

#completed line follow until soda can and grabbed soda can at end of routine

