#!/usr/bin/env python
# import os
# cwd = os.getcwd()
#print(cwd)

# dir_path = os.path.dirname(os.path.realpath('__file__'))
#print(dir_path)
import os

# print("Path at terminal when executing this file")
# print(os.getcwd() + "\n")

# # print("This file path, relative to os.getcwd()")
# # print(__file__ + "\n")

# print("This file full path (following symlinks)")
# full_path = os.path.realpath(__file__)
# print(full_path)

# print("This file directory and name")
# path, filename = os.path.split(full_path)
# print(path + ' --> ' + filename + "\n")

full_path = os.path.realpath(__file__)
print(full_path)

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path)
print(type(path))