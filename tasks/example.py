# example.py
import multitasking
import time
import random
import signal
import argparse
# kill all tasks on ctrl-c
from tasks import multicast
from tasks.multicast import multicast
from tasks.tasks import Tasks

from utils import ssh
import sys

signal.signal(signal.SIGINT, multitasking.killall)


def execute():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--operation', type=str, choices=('network', 'multicast', 'unicast'), help='operation',
                        required=True)
    parser.add_argument('-s', '--source', type=str, help='username', required=True)
    parser.add_argument('-p', '--destination', type=str, help='password', required=True)
    args = parser.parse_args()

    # call the methods magically
    test_command = getattr(sys.modules[__name__], args.operation)
    if issubclass(test_command, Tasks):
        command = test_command()
        command.execute(args)
    else:
        raise NotImplementedError()
    sys.exit(0)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-o', '--operation', type=str, choices=('network', 'multicast', 'unicast'), help='operation',
#                         required=True)
#     parser.add_argument('-s', '--source', type=str, help='username', required=True)
#     parser.add_argument('-p', '--destination', type=str, help='password', required=True)
#     args = parser.parse_args()
#
#     # call the methods magically
#     test_command = getattr(sys.modules[__name__], args.operation)
#     if issubclass(test_command, Tasks):
#         command = test_command()
#         command.execute(args)
#     else:
#         raise NotImplementedError()
#     sys.exit(0)
