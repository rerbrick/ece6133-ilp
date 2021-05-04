# module_scaler.py

import var
from file_generator import *

###
# Resizes the floorplan of the modules to account for overestimating or
# underestimating when optimizing the height and width of soft modules. Adds
# the height and width of the floorplan to a list with other floorplans.
#
# @param    mylist: the list of results from lpsolve
# @param    chunk: a chunk of modules at most 10 modules large
###
def resize(mylist, chunk):
    counter=0
    ymax=0
    for mod in chunk:
        if mod[0] == "hard":
            counter += 1 # increment counter
        elif mod[0] == "soft":
            if(chunk[counter][7]/mylist[1+(5*counter)]>ymax):
                # if the height of the soft module is greater than ymax
                ymax=chunk[counter][7]/mylist[1+(5*counter)]+mylist[5+(5*counter)]
            counter = counter+1
    if(ymax>mylist[0]):
        # if ymax is greater than the y value of the floorplan
        temp_list = ["hard", float(mylist[0]), float(ymax)]
        print("Block Area: {}".format(mylist[0] * ymax))
        var.mod_chunks.append(temp_list)
    else:
        # ymax is not greater than the y value of the floorplan
        temp_list = ["hard", float(mylist[0]), float(mylist[0])]
        print("Block Area: {}".format(mylist[0] ** 2))
        var.mod_chunks.append(temp_list)

