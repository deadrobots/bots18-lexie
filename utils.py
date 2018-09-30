import os, sys
from wallaby import *
import constants as c


def drivetimed(lspeed, rspeed, time):
    motor(c.leftmotor, lspeed)
    motor(c.rightmotor, rspeed)
    msleep(time)
    ao()


def wait_for_button():
    while not right_button():
        pass