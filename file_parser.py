# file_parser.py

###
# Contains functions for opening a user-specified file
###

import sys # for command line argument

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