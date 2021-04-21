# var.py

###
# Initializes the global variables used by multiple files
###
def init():
    global hard_num # number of hard modules
    hard_num = 0 # initial number of hard modules is 0
    global soft_num # number of soft modules
    soft_num = 0 # initial number of soft modules is 0
    
    global hard_modules # hard_modules = [width, height]
    hard_modules = []
    global soft_modules # soft_modules = [area, aspect_ratio_min, aspect_ratio_max]
    soft_modules = []