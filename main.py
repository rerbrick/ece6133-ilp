import sys # for command line argument
import var
from file_parser import * # get all functions from file_parser.py
from file_generator import * # get all functions from file_generator.py
from lpsolve55 import *
from plotter import *
import timeit


###
# Just a main function
###

def main():
    var.init() # initialize global variables
 
    file_name = sys.argv[1] # get name of benchmark file
    
    # get over or under estimation from the user
    print("Enter 'o' for overestimation of 'u' for underestimation: ")
    answer = input()
    if (answer == 'o'):
        var.overestimate = True
    elif (answer == 'u'):
        var.overestimate = False
    print("\n{}".format(var.overestimate))
    
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
    
    # solve the lp file
    output_file = "{}.lp".format(file_name)

    mod1 = lpsolve("read_lp", output_file)
    lpsolve("set_timeout",mod1,120)
    res1 = lpsolve('solve', mod1)
    obj1 = lpsolve('get_objective', mod1)
    vars1 = lpsolve('get_variables', mod1)[0]
    names = lpsolve('get_origcol_name', mod1)
    print("vars1: ", vars1)
    print("names: ", names)
    mylist=vars1[0:5*(var.mod_num)+1]
    print(mylist)
    plotthing(mylist)
    
if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  