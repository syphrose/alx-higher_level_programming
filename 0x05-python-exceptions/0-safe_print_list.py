#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print x elements of a list
    
    Args:
        my_list (list): where elements are printed from
        x (int): num of elements to be printed

    Returns:
        The number of elements to printed
    """    

    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return(ret)
