from file_parser import * # get all functions from file_parser file

###
# Just a main function
###
def main():
    # try to open the benchmark file
    if not open_file():
        # file could not be opened
        return -1 # return error code
    # try to close the benchmark file
    if not close_file(): 
        # close the benchmark file
        return -1 # return error code
    
if __name__ == "__main__":
    main()