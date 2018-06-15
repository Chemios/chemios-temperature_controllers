import os

def package_path():
    '''Get the path to the chemios_tc directory'''
    path = os.path.abspath(__file__)
    return os.path.dirname(path)
