import re

from fileDialog import Aapp


def load(history):
    # We call the fileDialog.py file to create the open a file window and obtain the path of the file
    file = Aapp()
    dir = file.openFileNameDialog()
    file.hide()

    f = open(dir, "r")

    # We obtain the data of the file, no matter how the numbers are separated
    # It can be 1 2 3 4    1, 2, 3, 4   1,2,3,4  or one number per line

    listN = re.split(', |,| |\n', f.read())
    while ("" in listN):
        listN.remove("")
    listN = list(map(int, listN))
    f.close()
    history = history + listN
    return history


def save(history):
    file = Aapp()
    dir = file.saveFileDialog()
    file.hide()

    f = open(dir, "w+")
    for i in history:
        f.write(str(i) + " ")
    f.close()
