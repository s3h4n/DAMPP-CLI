""" This module will help to run linux shell commands.

    - Command.run will run given shell commands.
"""

import sys
import os


class Command:

    def __init__(self):
        pass

    def run(self, command):
        try:
            status = os.system(str(command))
            return status
        except:
            print(f"Error : Can't run command {command}.")
            sys.exit()
