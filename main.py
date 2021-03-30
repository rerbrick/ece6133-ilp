import sys
import os

###
# Gets the file name given by the user, adds the directory to the file path,
# and tries to open the file. Alerts the user if the file does not exist.
#
# Expects user to enter only one valid file name.
###
def get_file():
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
        return # exit the function
    print("File was successfully opened.")
    benchmark.close() # close the file

###
# Just a main function
###
def main():
    get_file()
    
if __name__ == "__main__":
    main()