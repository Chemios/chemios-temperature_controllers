'''
Create a new instrument in the current instrument type

Usage:

    new_instrument <instrument_name>

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
    if instrument_name.rstrip('.py') == instrument_name:
        instrument_filename = '_' + instrument_name.lower().replace(' ','_').replace('-', '_') + '.py'
    copyfile('chemios_tc_base.py', instrument_filename)

    #Open the file and change the name of the class
    class_name = instrument_filename.title().replace(' ', '') + '(object)'
    with FileInput(instrument_filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('TemperatureControllers(ABC)', class_name), end='')

    #Change back to the original directory
    os.chdir(old_path)

if __name__ == '__main__':
    args = docopt(__doc__)
    if args['instrument_name']:
        new_instrument(args['instrument_name'])

