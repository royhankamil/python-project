# hello
"""just example to use module"""


__counter = 0 # private variabel (begin with double underscore(__))

def suml(the_list):
    """to sum list"""
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
    """to time all in list"""
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == "__main__":
    print("I know this it can")
else:
    print("i dont knpw this is can, i think no")
