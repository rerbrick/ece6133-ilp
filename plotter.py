import matplotlib.pyplot as plt
import matplotlib.patches as patches
import var
import random


def plotthing(mylist, all_mods, final_list):
 
    print(mylist,"plotslist")
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    list_index = 0
    for chunk in all_mods:
        # for each chunk of modules in the list of all modules
        index = 0
        #ymax=0
        # get scaled x and y value for each module in the chunk
        x_scale = final_list[4 + (5 * list_index)]
        y_scale = final_list[5 + (5 * list_index)]
        for mod in chunk:
            if mod[0] == "hard":
                if mylist[list_index][3+(5*index)] == 0:
                    rect1 = patches.Rectangle(
                            (mylist[list_index][4+(5*index)] + x_scale,
                            mylist[list_index][5+(5*index)] + y_scale), 
                            mylist[list_index][1+(5*index)], 
                            mylist[list_index][2+(5*index)],
                            facecolor='red',edgecolor='black')
                else:
                    rect1 = patches.Rectangle(
                            (mylist[list_index][4+(5*index)] + x_scale, 
                            mylist[list_index][5+(5*index)] + y_scale),
                            mylist[list_index][2+(5*index)], 
                            mylist[list_index][1+(5*index)],
                            facecolor='yellow',edgecolor='black')
                ax1.add_patch(rect1)
            
            elif mod[0] == "soft":
                rect1 = patches.Rectangle(
                        (mylist[list_index][4+(5*index)] + x_scale, 
                        mylist[list_index][5+(5*index)] + y_scale), 
                        mylist[list_index][1+(5*index)], 
                        chunk[index][7]/mylist[list_index][1+(5*index)],
                        facecolor='orange',edgecolor='black')
                ax1.add_patch(rect1)
                    
            index += 1
        list_index += 1

    plt.ylim(0, final_list[0])
    plt.xlim(0, final_list[0])
    plt.show()

