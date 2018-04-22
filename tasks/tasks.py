from abc import ABC, abstractmethod
import yaml
import os
import sys

class Tasks(ABC):

    def __init__(self):
        self.config=None

    @abstractmethod
    def execute(self, args):
        raise NotImplementedError()



    def read_configuration(self, file):

        #dir_path = os.path.dirname(os.path.realpath(__file__))
        #full_file_path = dir_path + "/" + file
        if os.path.isfile(file):
            with open(file, 'r') as stream:
                try:
                    return yaml.load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
                    return 1
        else:
            raise FileNotFoundError()