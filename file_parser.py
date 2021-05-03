# file_parser.py

###
# Contains functions for opening a user-specified file, parsing the file for
# chip constraints, and closing the benchmark file
###

import var # import global variables from settings.py
from math import sqrt # import square root function

global benchmark

###
# Uses the file name given by the user, adds the directory to the file path,
# and tries to open the file. Alerts the user if the file does not exist.
#
# Expects user to enter only one valid file name without the .ilp extension.
#
# @param    file_name: the name of the benchmark file provided by the user
###
def open_benchmark(file_name):
    global benchmark # add benchmark file to function scope
    # add benchmark directory to file path
    file_path = "benchmarks/{}.ilp".format(file_name)
    # try to open the file in read-only mode
    try:
        benchmark = open(file_path, "r")
    except IOError:
        # the file could not be found
        return False # file could not be opened
    return True # file was opened

###
# Closes the benchmark file
###
def close_benchmark():
    global benchmark # add benchmark file to function scope
    try:
        benchmark.close()
    except IOError:
        # there was an error while closing the file
        return False # file wasn't successfully closed
    return True # file was closed
    
###
# Reads values from benchmark file and adds them to lists for hard and soft
# modules
#
# Expects files to be written as example in README in benchmarks directory
###
def read_benchmark():
    global benchmark # add benchmark file to function scope
    while True: # iterate through the file
        line = benchmark.readline() # get one line of benchmark file
        if len(line) == 0:
            # line does not have any characters
            # get total number of modules
            var.mod_num = var.hard_num + var.soft_num
            return # exit function
        # split line into module type and number of modules
        module = line.strip().split(' - ')
        if module[0] == 'hard':
            # following values are hard modules
            var.hard_num = int(module[1]) # assign number of hard modules
            for num in range(var.hard_num):
                # read the number of hard modules
                line = benchmark.readline()
                values = line.strip().split(',') # remove commas
                # convert string to integers and add to hard modules list
                temp_list = ["hard", int(values[0]), int(values[1])]
                var.all_mod.append(temp_list)
        elif module[0] == 'soft':
            # following values are soft modules
            var.soft_num = int(module[1]) # assign number of soft modules
            for num in range(var.soft_num):
                # read the number of soft modules
                line = benchmark.readline()
                values = line.strip().split(',') # remove commas
                # convert string to integers and add to soft modules list
                area = float(values[0]) # area of soft module
                print(area)
                w_min = sqrt(area * float(values[1])) # minimum width
                w_max = sqrt(area * float(values[2])) # maximum width
                slope = -(area/(w_max ** 2)) # slope for height equation
                intercept = 2 * (area/w_max) # intercept for height equation
                h_min = slope * w_max + intercept # minimum height
                h_max = slope * w_min + intercept # maximum height
                temp_list = ["soft", w_min, w_max, slope, intercept, h_min, h_max,area]
                var.all_mod.append(temp_list)
        else:
            pass # go on to the next line            