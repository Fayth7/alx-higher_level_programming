#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter to keep track of the integers printed
    try:
        for i in range(x):
            if i < len(my_list):
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    count += 1
            else:
                break
    except TypeError:
        pass
    finally:
        print()
        return count
