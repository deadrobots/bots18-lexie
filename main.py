#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import actions as act


def main():
    print "Hello World"
    act.driveSquare()
    act.grabSodaCan()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();

#installed ET and tophat
#two weeks: program line follow until ET sees can - pick up and drive "home"

