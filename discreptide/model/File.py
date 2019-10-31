import os

FILE_NAME = ""


def set_file(file_name):
    global FILE_NAME
    FILE_NAME = file_name
    os.chdir('/'.join(file_name.split('/')[:-1]))


def get_file():
    return FILE_NAME
