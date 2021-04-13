# file_generator.py

import var

W_max = 0 # maximum chip width
H_max = 0 # maximum chip height
global output

###
# Creates the .lp output file or overwrites the output file if it already
# exists
#
# @param    file_name: the name of the output file provided by the user
###
def create_lp(file_name):
    global output # add output file to scope
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
    global output # add output file to scope
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
    global W_max, H_max # add upper bounds to function scope
    # @TODO: add soft module functionality
    # sum the widths and the heights of the modules
    max_val = [sum(module) for module in zip(*var.hard_modules)]
    W_max = max_val[0] # maximum width of the chip
    H_max = max_val[1] # maximum height of the chip

###
# Generates the .lp output file. Writes the necessary statements to the output
# file for the lp solver. Statements include: area minimization, non-overlap
# constraints, variable type constraints, chip width constraints, and chip
# height constraints.
#
# NOTE: Only considers non-rotated hard modules.
###
def generate_lp():
    global W_max, H_max # add upper bounds to function scope
    global output # add output file to function scope
    upper_bounds() # get the upper bounds of the chip
    
    output.write("min: y_star;\n") # try to minimize chip area
    output.write("\n") # new line for readability
    
    output.write("/* Non-overlap constraints */\n")
    for mod in range(var.hard_num):
        # for each hard module
        m = mod + 1 # number of starting module
        n = m + 1 # number of subsequent module
        while n <= var.hard_num:
            # non-overlap constraint for all subsequent modules
            tmp = ("x{} + {} <= x{} + {} x{}{} + {} y{}{};"
                   .format(m, var.hard_modules[mod][0], n, W_max, m, n, W_max, 
                           m, n))
            # add constraint to output file
            output.write(tmp + "\n")
            tmp = ("x{} - {} >= x{} - {} + {} x{}{} - {} y{}{};"
                   .format(m, var.hard_modules[mod + 1][0], n, W_max, W_max, m, 
                           n, W_max, m, n))
            # add constraint to output file
            output.write(tmp + "\n")
            tmp = ("y{} + {} <= y{} + {} + {} x{}{} - {} y{}{};"
                   .format(m, var.hard_modules[mod][1], n, H_max, H_max, m, n, 
                           H_max, m, n))
            # add constraint to output file
            output.write(tmp + "\n")
            tmp = ("y{} - {} >= y{} - {} + {} x{}{} + {} y{}{};"
                   .format(m, var.hard_modules[mod + 1][1], n, 2*H_max, H_max, 
                           m, n, H_max, m, n))
            # add constraint to output file
            output.write(tmp + "\n")
            output.write("\n") # add a new line for readability
            n = n + 1 # increment n to go to next module
        
    output.write("\n") # add a new line for readability
    output.write("/* Chip width and height constraints */\n")
    for mod in range(1, var.hard_num + 1):
        # for each hard module
        # chip width constraint
        output.write("x{} + {} <= y_star;\n".format(mod, var.hard_modules[mod - 1][0]))
        # chip height constraint
        output.write("y{} + {} <= y_star;\n".format(mod, var.hard_modules[mod - 1][1]))
    
    output.write("/* Variable type constraints */\n")
    # continuous integer constraints
    output.write("int ")
    for mod in range(1, var.hard_num + 1):
        # for each hard module
        output.write("x{}, y{}, ".format(mod, mod))
    output.write("y_star;\n") # area needs to be continuous integer
    # binary constraints
    output.write("bin ")
    for mod in range(1, var.hard_num - 1):
        # for each hard module except the last two
        next_mod = mod + 1 # number of the next module
        while next_mod <= var.hard_num:
            # binary constraints for hard modules
            output.write("x{}{}, y{}{}, ".format(mod, next_mod, mod, next_mod))
            next_mod = next_mod + 1 # increment next module
    output.write("x{}{}, y{}{};\n"
                 .format(var.hard_num - 1, var.hard_num, var.hard_num - 1, 
                         var.hard_num))