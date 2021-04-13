import sys # for command line argument
from file_parser import * # get all functions from file_parser.py
from file_generator import * # get all functions from file_generator.py

###
# Just a main function
###
def main():
    # global variables for lists of hard and soft modules
    global hard_modules, soft_modules
 
    file_name = sys.argv[1] # get name of benchmark file
    
    # try to open the benchmark file
    if not open_benchmark(file_name):
        # file could not be opened
        print("Error: File does not appear to exist.")
        return -1 # return error code
    # benchmark file was successfully opened if code gets here
    print("Benchmark file was opened.")
    
    read_benchmark() # read the benchmark file and get module specs
    
    # try to close the benchmark file
    if not close_benchmark(): 
        # benchmark file could not be closed
        print("Error: File could not be closed.")
        return -1 # return error code
    # benchmark file was closed if code gets here
    print("Benchmark file was closed.")
    
    # try to create the output .lp file
    if not create_lp(file_name):
        # file could not be created or rewritten
        print("Error: File could not be created.")
        return -1 # return error code
    # output file was created if code gets here
    print("Output file was opened.")
    
    generate_lp()  # generate the lp file
    
    # try to close the output .lp file
    if not close_lp():
        # output file could not be closed
        print("Error: File could not be closed.")
        return -1 # return error code
    # output file was closed if code gets here
    print("Output file was closed.")
    
if __name__ == "__main__":
    main()