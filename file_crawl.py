"""
This script is only tested on a window 10 environment
"""


import os.path
from os import listdir
import pickle
import subprocess

#file paths list
files = []


def crawl_paths(path):
    """
    takes a string path then check the contents of the paths
    if it contains another folder it would check the contents of that folder
    :param path:
    :return:
    """
    directories = listdir(path)
    for item in directories:
        if os.path.isdir(os.path.join(path,item)):
            files.append(os.path.join(path,item))
            new_path = os.path.join(path,item)
            crawl_paths(new_path)
        else:
            files.append(os.path.join(path,item))
    return


def save_paths(paths):
    """
    takes a list of paths as param
    and saves the list of paths
    :param paths:
    :return:
    """
    temp = open("path.pickle", "wb")
    pickle.dump(paths, temp)
    temp.close()


def load_paths():
    """
    retrieves list of paths
    :return:
    """
    temp = open("path.pickle","rb")
    paths = pickle.load(temp)
    return paths


def open_paths(paths):
    """
    takes the unpickled list of paths
    and open the first five folders using windows explorer
    :param paths:
    :return:
    """
    print('Opening the first 5 folders!!!')
    cnt = 0
    for path in paths:
        if cnt < 5:
            if os.path.isdir(path):
                subprocess.Popen(r"explorer /open,{}".format(path))
                cnt += 1

#main program
if __name__ == '__main__':
    while True:
        path = input('Please Input Path to check for Directories:')
        if not os.path.isdir(path):
            print('Please use a valid Path')
        else:
            crawl_paths(path)
            break

    save_paths(files)
    paths = load_paths()
    open_paths(paths)
