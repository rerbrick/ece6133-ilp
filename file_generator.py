# file_generator.py

from lpsolve55 import *
from lp_maker import *
import numpy as np

# hard_modules = [width, height]
hard_modules = [] # global list of hard modules

# soft_modules = [area, aspect_ratio_min, aspect_ratio_max]
soft_modules = [] # global list of soft modules

W_max = 0 # maximum width of the chip
H_max = 0 # maximum height of chip

def create_lp(file_name):
    global output # global variable for output lp file
    # add .lp extension to file name
    file_ext = "{}.lp".format(file_name)
    # create a new output file or overwirte existing file
    try:
        output = open(file_ext, "w")
    except IOError:
        # the file could not be found
        return False # file could not be opened or created
    return True # file was opened

###
# Closes the .lp output file
###
def close_lp():
    global output # add output variable to function scope
    try:
        output.close()
    except IOError:
        # there was an error while closing the file
        return False # file wasn't successfully closed
    return True # file was closed

###
# Calculates the upper bounds of the chip by summing the widths and heights of
# each model. Assigns the sum of the widths to W_max and the sum of the heights
# to H_max
#
# NOTE: Only considers hard modules for now.
###
def upper_bounds():
    global hard_modules # global variable of hard_modules list
    global W_max, H_max # global variables for chip width and height
    # @TODO: add soft module functionality
    # sum the widths and the heights of the modules
    max_val = [sum(module) for module in zip(*hard_modules)]
    W_max = max_val[0] # maximum width of the chip
    H_max = max_val[1] # maximum height of the chip

def generate_lp():
    global W_max, H_max # global variables for chip width and height
    upper_bounds() # get the upper bounds of the chip
    