from os import listdir
from os.path import isfile, join, exists, isdir

from numpy import full


# print(" ".join(("a and", "b")))
print(join(r"C:\kdata\myPYTHON", "get-pip.py"))

print()


def get_files(path):
    for file in listdir(path):
        full_path = join(path, file)
        if isfile(full_path):
            if exists(full_path):
                yield full_path


def get_directories(path):
    for directory in listdir(path):
        full_path = join(path, directory)
        if isdir(full_path):
            if exists(full_path):
                yield full_path


def get_files_recursively(directory):
    for file in get_files(directory):
        yield file
    for subdirectory in get_directories(directory):
        for file in get_files_recursively(subdirectory):
            yield file


files = get_files_recursively(r"C://kdata//myPYTHON//MyLearnings//Project_LinuxBot")

for file in files:
    print(file)

print()

for files in get_files(r"C://kdata//myPYTHON//MyLearnings//Project_LinuxBot"):
    print(files)

print()

for dirs in get_directories(r"C://kdata//myPYTHON//MyLearnings//Project_LinuxBot"):
    print(dirs)
