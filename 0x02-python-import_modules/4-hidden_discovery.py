#!/usr/bin/python3
if _name_ == "_main_":
    from hidden_4 import *
    array = dir()
    for i in range(0, len(array)):
        if array[i][0:2] != "__":
            print("{}".format(array[i]))
