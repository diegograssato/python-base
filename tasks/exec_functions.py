import time
from subprocess import call

SUCESS = 0
MAX_ATEMPT = 3

class bcolors:
    """ Ansi Colors """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def exec_command(parm_list):
    """ Trial execution """
    print(parm_list)