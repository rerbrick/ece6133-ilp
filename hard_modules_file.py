import sys
from lpsolve55 import *

# hard_modules = [width, height]
 # global list of hard modules


def hard_modules_run(input_module):
    print(input_module)
    fact =1
    width=0
    height=0
    #numvars contains the number of variables being used
    numvars=0
    width_list=[]
    height_list=[]
    for n in input_module:
        width = width+n[0]
        height = height+n[1]
        width_list.append(n[0])
        height_list.append(n[1])
        numvars=numvars+1

    #get the number of x(n.m) 
    for i in range(1,numvars):
        fact = fact * i
    print(fact)

    x=0
    stop=1
    xlist=[]
    while(numvars-stop>0):
        for i in range(numvars-stop):
            xlist.append(x)
        x=x+1
        stop=stop+1
    print(xlist)

    ylist=[]
    start=1
    stop=1
    for i in range(numvars-1):
        counter=start
        for i in range(numvars-stop):
            ylist.append(counter)
            counter=counter+1
        start=start+1
        stop=stop+1
    
    print(ylist)

    axlists=[]
    n=0
    for i in range(fact):
        axl=[]
        for j in range(numvars):
            if(j==xlist[i]):
                axl.append(-1)
            elif(j==ylist[i]):
                axl.append(1)
            else:
                axl.append(0)
        axlists.insert(n,axl)
        n=n+1

    print(axlists)

    finallist=[]
    totalcount=0
    for i in range(fact):
        counter=0
        for j in range(2):
            templist=[]
            for p in range(numvars):
                templist.append(axlists[i][p])
            for k in range(numvars):
                templist.append(0)
            for l in range(fact):
                if(l==counter):
                    templist.append(width)
                else:
                    templist.append(0)
            for l in range(fact):
                if(l==counter):
                    if(totalcount%4==0 or totalcount%4==3):
                        templist.append(width)
                    else:
                        templist.append(width*-1)
                else:
                    templist.append(0)
            finallist.insert(totalcount,templist)
            print(totalcount)
            print("top")
            totalcount=totalcount+1
        for j in range(2):
            templist=[]
            for k in range(numvars):
                templist.append(0)
            for p in range(numvars):
                templist.append(axlists[i][p])
            for l in range(fact):
                if(l==counter):
                    templist.append(height)
                else:
                    templist.append(0)
            for l in range(fact):
                if(l==counter):
                    if(totalcount%4==0 or totalcount%4==3):
                        templist.append(height)
                    else:
                        templist.append(height*-1)
                else:
                    templist.append(0)
            print(totalcount)
            print("bot")
            finallist.insert(totalcount,templist)
            totalcount=totalcount+1
        counter+1
            


    for i in range(len(finallist)):
        print(finallist[i])
    #print(numvars)
    #print(width)
    #print(height)
    #print(width_list)
    #print(height_list)