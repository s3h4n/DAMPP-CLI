"""
    * @import module sys
    * @import module os
"""

import sys
import os


class Command:

    """ 
        * runs linux shell commands.
    """

    def __init__(self) -> None:
        """
            * declaring public method __init__()

            * @param self

            * @return None
        """

        pass

    def run(self, command) -> int:
        """
            * declaring public method run()
                - runs the shell commands.

            * @param self
            * @param command -> shell command

            * try -> @return command's return status
            * except -> @return None     
        """

        try:

            state = os.system(str(command))
            return state  # success state -> 0

        except:

            print(f"Error : Can't run command {command}.")
            sys.exit()  # exit the program
