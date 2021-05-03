# file_generator.py

import var

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
# to H_max. Returns the maximum of the two values
#
# @return   the largest of the maximum height and maximum width
#
# NOTE: Only considers hard modules for now.
###
def upper_bound():
    # @TODO: add soft module functionality
    # sum the widths and the heights of the modules
    W_max = 0 # initialize W_max before using it
    H_max = 0 # initialize H_max before using it
    for module in var.all_mod:
        if (module[0] == "hard"):
            # hard module
            W_max += max(module[1], module[2]) # max of height and width
            H_max += max(module[1], module[2]) # max of height and width
        elif (module[0] == "soft"):
            W_max += module[2] # maximum width
            H_max += module[6] # maximum height
    # return the maximum value between the width and height
    return max(W_max, H_max)

###
# Generates the .lp output file. Writes the necessary statements to the output
# file for the lp solver. Statements include: area minimization, non-overlap
# constraints, variable type constraints, chip width constraints, and chip
# height constraints.
#
# NOTE: Only considers rotatable hard modules.
###
def generate_lp():
    global output # add output file to function scope
    
    bound = upper_bound() # get maximum bound between the height and width
    
    output.write("min: y_star;\n") # try to minimize chip area
    output.write("\n") # new line for readability
    
    output.write("/* Chip width and height constraints */\n")
    for mod in range(1, var.mod_num + 1):
        if (var.all_mod[mod - 1][0] == "hard"):
            # module is a hard module
            # given width of hard module
            output.write("w{} = {};\n".format(mod, var.all_mod[mod - 1][1]))
            # given height of hard module
            output.write("h{} = {};\n".format(mod, var.all_mod[mod - 1][2]))
            # module rotation constraints
            output.write("z{} >= 0;\n".format(mod))
            # chip width constraint
            output.write("x{} + {} - {} z{} + {} z{} <= y_star;\n"
                         .format(mod, var.all_mod[mod - 1][1],
                                 var.all_mod[mod - 1][1], mod,
                                 var.all_mod[mod - 1][2], mod))
            # chip height constraint
            output.write("y{} + {} - {} z{} + {} z{} <= y_star;\n"
                         .format(mod, var.all_mod[mod - 1][2],
                                 var.all_mod[mod - 1][2], mod,
                                 var.all_mod[mod - 1][1], mod))
        elif (var.all_mod[mod - 1][0] == "soft"):
            # module is a soft module
            # min and max width of soft module
            output.write("{} <= w{} <= {};\n".format(var.all_mod[mod - 1][1],
                         mod, var.all_mod[mod - 1][2]))
            # min and max height of soft module
            output.write("{} <= h{} <= {};\n".format(var.all_mod[mod - 1][5],
                         mod, var.all_mod[mod - 1][6]))
            # relationship between width and height
            output.write("h{} = {} w{} + {};\n".format(mod, var.all_mod[mod - 1][3],
                         mod, var.all_mod[mod - 1][4]))
            # module rotation constraints
            output.write("z{} = 0;\n".format(mod))
            # chip width constraint
            output.write("x{} + w{} <= y_star;\n".format(mod, mod))
            # chip height constraint
            output.write("y{} + h{} <= y_star;\n".format(mod, mod))
    output.write("\n") # add a new line for readability
    
    output.write("/* Non-overlap constraints */\n")
    for mod in range(var.mod_num):
        # for all modules
        m = mod + 1 # number of starting module
        n = m + 1 # number of subsequent module
        while n <= var.mod_num:
            # variable assignments for hard and soft modules
            # module m
            if (var.all_mod[m - 1][0] == "hard"):
                width_m = var.all_mod[m - 1][1]
                width_z_m = ("{} z{}".format(var.all_mod[m - 1][1], m))
                height_m = var.all_mod[m - 1][2]
                height_z_m = ("{} z{}".format(var.all_mod[m - 1][2], m))
            elif (var.all_mod[m - 1][0] == "soft"):
                width_m = ("w{}".format(m))
                width_z_m = 0
                height_m = ("h{}".format(m))
                height_z_m = 0
            # module n
            if (var.all_mod[n - 1][0] == "hard"):
                width_n = var.all_mod[n - 1][1]
                width_z_n = ("{} z{}".format(var.all_mod[n - 1][1], n))
                height_n = var.all_mod[n - 1][2]
                height_z_n = ("{} z{}".format(var.all_mod[n - 1][2], n))
            elif (var.all_mod[n - 1][0] == "soft"):
                width_n = ("w{}".format(n))
                width_z_n = 0
                height_n = ("h{}".format(n))
                height_z_n = 0
            # non-overlap constraint for all subsequent modules
            # x_m + h_m * z_m + w_m(1 - z_m) <= x_n + W_max(x_mn + y_mn)
            tmp = ("x{} + {} + {} - {} <= x{} + {} x{}_{} + {} y{}_{};"
                   .format(m,               # x_m
                           height_z_m,      # h_m * z_m
                           width_m,         # w_m
                           width_z_m,       # w_m * z_m
                           n,               # x_n
                           bound, m, n,     # W_max * x_mn
                           bound, m, n))    # W_max * y_mn
            # add constraint to output file
            output.write(tmp + "\n")
            # x_m - h_n * z_n - w_n(1 - z_n) >= x_n - W_max(1 - x_mn + y_mn)
            tmp = ("x{} - {} - {} + {} >= x{} - {} + {} x{}_{} - {} y{}_{};"
                   .format(m,               # x_m
                           height_z_n,      # h_n * z_n
                           width_n,         # w_n
                           width_z_n,       # w_n * z_n
                           n,               # x_n
                           bound,           # W_max
                           bound, m, n,     # W_max * x_mn
                           bound, m, n))    # W_max * y_mn
            # add constraint to output file
            output.write(tmp + "\n")
            # y_m + h_m * z_m + h_m(1 - z_m) <= y_n + W_max(1 + x_mn - y_mn)
            tmp = ("y{} + {} + {} - {} <= y{} + {} + {} x{}_{} - {} y{}_{};"
                   .format(m,               # y_m
                           width_z_m,       # w_m * z_m
                           height_m,        # h_m
                           height_z_m,      # h_m * z_m
                           n,               # y_n
                           bound,           # W_max
                           bound, m, n,     # W_max * x_mn
                           bound, m, n))    # W_max * y_mn
            # add constraint to output file
            output.write(tmp + "\n")
            # y_m - w_n * z_n - h_n(1 - z_n) <= y_n + W_max(2 - x_mn - y_mn)
            tmp = ("y{} - {} - {} + {} >= y{} - {} + {} x{}_{} + {} y{}_{};"
                   .format(m,               # y_m
                           width_z_n,       # w_n * z_n
                           height_n,        # h_n
                           height_z_n,      # h_n * z_n
                           n,               # y_n
                           2 * bound,       # 2 * W_max
                           bound, m, n,     # W_max * x_mn
                           bound, m, n))    # W_max * y_mn
            # add constraint to output file
            output.write(tmp + "\n")
            output.write("\n") # add a new line for readability
            n = n + 1 # increment n to go to next module
    
    output.write("/* Variable type constraints */\n")
    # continuous integer constraints
    for mod in range(1, var.mod_num + 1):
        next_mod = mod + 1 # number of the next module
        if (var.all_mod[mod - 1][0] == "hard"):
            output.write("bin z{};\n".format(mod))
    output.write("bin ") # relative position constraints
    for mod in range(1, var.mod_num - 1):
        # for each module except the last two
        next_mod = mod + 1 # number of the next module
        while next_mod <= var.mod_num:
            # binary constraints for hard modules
            output.write("x{}_{}, y{}_{}, ".format(mod, next_mod, mod, next_mod))
            next_mod = next_mod + 1 # increment next module
    output.write("x{}_{}, y{}_{};\n"
                 .format(var.mod_num - 1, var.mod_num, var.mod_num - 1, 
                         var.mod_num))