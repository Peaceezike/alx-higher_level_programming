#!/usr/bin/python3
if _name_ == "_main_":
    import sys
    result = 0
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])
    print("{}".format(result))
