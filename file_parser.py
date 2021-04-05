# file_parser.py

###
# Contains functions for opening a user-specified file, parsing the file for
# chip constraints, and closing the benchmark file
###

import sys # for command line argument

# hard_modules = [width, height]
hard_modules = [] # global list of hard modules
# soft_modules = [area, aspect_ratio_min, aspect_ratio_max]
soft_modules = [] # global list of soft modules

###
# Gets the file name given by the user, adds the directory to the file path,
# and tries to open the file. Alerts the user if the file does not exist.
#
# Expects user to enter only one valid file name.
###
def open_file():
    global benchmark # global variable for reading the file
    file_name = sys.argv[1] # get name of benchmark file
    # add benchmark directory to file path
    file_path = "benchmarks/{}".format(file_name)
    # try to open the file in read-only mode
    try:
        benchmark = open(file_path, "r")
    except IOError:
        # the file could not be found
        print("Error: File does not appear to exist.")
        return False # file could not be opened
    print("Benchmark file was opened.")
    return True # file was opened

###
# Closes the benchmark file
###
def close_file():
    global benchmark # add benchmark variable to function scope
    try:
        benchmark.close()
    except IOError:
        # there was an error while closing the file
        print("Error: File could not be closed.")
        return False # file wasn't successfully closed
    print("Benchmark file was closed.")
    return True # file was closed
    
###
# Reads values from benchmark file and adds them to lists for hard and soft
# modules
#
# Expects files to be written as example in README in benchmarks directory
###
def read_file():
    global benchmark # add benchmark variable to function scope
    global hard_modules # list for hard module width and height
    global soft_modules # list for soft module area and area ratio range
    while True: # iterate through the file
        line = benchmark.readline() # get one line of benchmark file
        if len(line) == 0:
            # line does not have any characters
            return # exit function
        # split line into module type and number of modules
        module = line.strip().split(' - ')
        if module[0] == 'hard':
            # following values are hard modules
            for num in range(int(module[1])):
                # read the number of hard modules
                line = benchmark.readline()
                values = line.strip().split(',') # remove commas
                # convert string to integers and add to hard modules list
                temp_list = [int(values[0]), int(values[1])]
                hard_modules.append(temp_list)
        elif module[0] == 'soft':
            # following values are soft modules
            for num in range(int(module[1])):
                # read the number of soft modules
                line = benchmark.readline()
                values = line.strip().split(',') # remove commas
                # convert string to integers and add to soft modules list
                temp_list = [int(values[0]), float(values[1]), float(values[2])]
                soft_modules.append(temp_list)
        else:
            pass # go on to the next line
                
            