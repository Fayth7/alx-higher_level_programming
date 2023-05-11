#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

print("{} argument{}:".format(num_arguments, "s" if num_arguments != 1 else ""))

if num_arguments == 0:
    print("0 arguments.")
else:
    for i, argument in enumerate(arguments, start=1):
        print("{}: {}".format(i, argument))
