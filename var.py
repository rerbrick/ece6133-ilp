# var.py

###
# Initializes the global variables used by multiple files
###
def init():
    global hard_num # number of hard modules
    hard_num = 0 # initial number of hard modules is 0
    global soft_num # number of soft modules
    soft_num = 0 # initial number of soft modules is 0
    global mod_num # total number of hard and soft modules
    mod_num = 0
    
    # hard modules = ["hard", width, height]
    # soft_modules = ["soft", min_width, max_width
    #                  slope, intercept,
    #                  min_height, max_height, area]
    global all_mod # list of all modules
    all_mod = []
    
    # hard modules = ["hard", width, height]
    global mod_chunks # list of chunks of modules
    mod_chunks = []
    
    # overestimation or underestimation
    global overestimate
    overestimate = False
    
    # list of all modules in all chunks
    global big_list
    big_list = []