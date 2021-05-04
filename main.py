import sys # for command line argument
import var
from file_parser import * # get all functions from file_parser.py
from file_generator import * # get all functions from file_generator.py
from module_scaler import *
from lpsolve55 import *
from plotter import *

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
        
    file_num = 1
    for chunk in var.all_mod:
        # for each chunk of modules
        tmp_file_name = file_name + str(file_num)
        # try to create the output .lp file
        if not create_lp(tmp_file_name):
            # file could not be created or rewritten
            print("Error: File could not be created.")
            return -1 # return error code
        # output file was created if code gets here
        print("Output file {} was opened.".format(file_num))
            
        generate_lp(chunk, False)  # generate the lp file
    
        # try to close the output .lp file
        if not close_lp():
            # output file could not be closed
            print("Error: File could not be closed.")
            return -1 # return error code
        # output file was closed if code gets here
        print("Output file {} was closed.".format(file_num))

        # solve the lp file
        output_file = "{}.lp".format(tmp_file_name)
        mod1 = lpsolve("read_lp", output_file)
        # let lpsolve run for 120 seconds at most
        lpsolve("set_timeout", mod1, 120)
        res1 = lpsolve('solve', mod1)
        obj1 = lpsolve('get_objective', mod1)
        vars1 = lpsolve('get_variables', mod1)[0]
        names = lpsolve('get_origcol_name', mod1)
                
        mylist=vars1[0:5*(len(chunk))+1]
        
        # add chunk of modules to list of chunks as hard modules
        resize(mylist, chunk)
        # add list of values for one floorplan to list of all values
        var.big_list.append(mylist.copy())
        
        file_num += 1
    
    # run lpsolver with individual floor plans
    tmp_file_name = file_name + str("final")
    # try to create the output .lp file
    if not create_lp(tmp_file_name):
        # file could not be created or rewritten
        print("Error: File could not be created.")
        return -1 # return error code
    # output file was created if code gets here
    print("Final output file was opened.")
        
    generate_lp(var.mod_chunks, True)
    
    # try to close the output .lp file
    if not close_lp():
        # output file could not be closed
        print("Error: File could not be closed.")
        return -1 # return error code
    # output file was closed if code gets here
    print("Final output file was closed.")
    
    # solve the final lp file
    output_file = "{}.lp".format(tmp_file_name)
    mod1 = lpsolve("read_lp", output_file)
    # let lpsolve run for 120 seconds at most
    lpsolve("set_timeout", mod1, 120)
    res1 = lpsolve('solve', mod1)
    obj1 = lpsolve('get_objective', mod1)
    vars1 = lpsolve('get_variables', mod1)[0]
    names = lpsolve('get_origcol_name', mod1)

    final_list=vars1[0:5*(len(var.mod_chunks))+1]
    
    # plot all the modules
    plotthing(var.big_list, var.all_mod, final_list)
    # print final width, height, and area to console
    print("Chip Width: {}".format(final_list[0]))
    print("Chip Height: {}".format(final_list[0]))
    print("Chip Area: {}".format(final_list[0] ** 2))
    
    
if __name__ == "__main__":
    main()