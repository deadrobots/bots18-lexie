import os, sys
from wallaby import *
import constants as c


def wait_for_button(): 
	# Don't forget to use a print() statement here to display a message
	# How will I know that your robot is waiting for user input, unless
	# you tell the user? :) -LMB
    while not right_button():
        pass



