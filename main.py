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

#completed all 7 challenges
#further organize code: add utils and move drivetimed and waitforbutton
#test soda grab more (drive is not straight)

