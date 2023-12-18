#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    p = 0

    try:
        for i in my_list:
            if p < x:
                print('{}'.format(my_list[p]), end='')
                p += 1

        print()
    except TypeError:
        pass
    finally:
        return p
