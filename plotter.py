import matplotlib.pyplot as plt
import matplotlib.patches as patches
import var
import random


def plotthing(mylist):
 

    #print(mylist,"plotslist")
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    counter=0
    #print(var.hard_modules)
    
    for n in range(var.hard_num):
        if mylist[3+(5*counter)] == 0:
            rect1=patches.Rectangle((mylist[4+(5*counter)], mylist[5+(5*counter)]), mylist[1+(5*counter)], mylist[2+(5*counter)],facecolor='red',edgecolor='black')
            #print((mylist[4+(5*counter)], mylist[5+(5*counter)],mylist[1+(5*counter)], mylist[2+(5*counter)])," no rotate")
        else:
            rect1=patches.Rectangle((mylist[4+(5*counter)], mylist[5+(5*counter)]), mylist[2+(5*counter)], mylist[1+(5*counter)],facecolor='yellow',edgecolor='black')
            #print((mylist[4+(5*counter)], mylist[5+(5*counter)],mylist[2+(5*counter)], mylist[1+(5*counter)])," rotate")
        ax1.add_patch(rect1)
        counter = counter+1
    #counter=0
    #for n in var.soft_modules:
    plt.xlim(0,mylist[0])
    plt.ylim(0,mylist[0])
    #plt.show()
