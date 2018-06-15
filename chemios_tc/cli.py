"""
Chemios Temperature Controllers CLI

Usage:

    chemios-tc setup [--port|-p] [--address | -a] [--override | -o]
    chemios-tc -h | --help
    chemios-tc setpoint [--override | -o ]
    chemios-tc log [--stepchange --filepath --frequency --mute]

Options:
    --port -p     Serial port to which the device is connected.
    --address -a  The address of the connected device. [default: 1]
    --override -o Ignore I/O errors if temperature controller is not connected.
    --stepchange  Change in temperature to occur at the beginning of data logging.
    --filepath    Filepath for storing the csv data.
    --frequency   Data gathering frequency (in seconds). [default: 5]
"""

from docopt import DocoptExit, docopt


def main():
    args = docopt(__doc__,
                  options_first=True)
