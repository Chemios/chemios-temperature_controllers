'''
Create a new temperature controller instrument

Usage:
    new_instrument.py INSTRUMENT_NAME

Arguments:
    INSTRUMENT_NAME Name of new instrument
Options:
    -h --help Show this screen
'''
import os
from chemios_tc.utils import package_path
from shutil import copyfile
from fileinput import FileInput
from docopt import docopt

def new_instrument(instrument_name):
    '''Create a new instrument based on the base files'''
    #Change to chemios_tc directory and copy base file
    working_path = package_path()
    old_path = os.getcwd()
    os.chdir(working_path)

    #Create new filename
    if instrument_name.rstrip('.py') == instrument_name:
        instrument_filename = '_' + instrument_name.lower().replace(' ','_').replace('-', '_') + '.py'
    copyfile('chemios_tc_base.py', instrument_filename)

    #Open the file and change the import statement and the name of the class
    class_name = instrument_name.title().replace(' ', '') + '(TemperatureControllers)'
    with FileInput(instrument_filename, inplace=True) as file:
        for line in file:
            print(line.replace('TemperatureControllers(ABC)', class_name).replace('from abc import ABC', 'from .chemios_tc_base import TemperatureControllers'),
                  end='')


    #Change back to the original directory
    os.chdir(old_path)

args = docopt(__doc__)
if args['INSTRUMENT_NAME']:
    new_instrument(args['INSTRUMENT_NAME'])
