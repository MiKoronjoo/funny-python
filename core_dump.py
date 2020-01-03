""" How to get a core dump with Python :) """

def f():
    try:
        f()
    except RecursionError:
        print('oh!')
        f()

f()
