"""
    * @import module sys
    * @import module os
"""

import sys
import os


class Create:

    """
        * create documents and directories
    """

    def __init__(self, project_name) -> None:
        """
            * declaring public method __init__()

            * @param self
            * @param project_name -> name of the project

            * @return None
        """

        self.project_name = project_name

    def directory(self, path) -> None:
        """
            * declaring public method directory()
                - creates directories.

            * @param self
            * @param path -> directory name with path

            * @return None     
        """

        try:

            os.mkdir(f"{path}")

        except FileExistsError:

            print(f"\nError : {path} already exists.")
            sys.exit()  # exit the program

        except Exception:

            print(f"\nError : Can't create {path}.")
            sys.exit()  # exit the program

    def document(self, path, data) -> None:
        """
            * declaring public method document()
                - creates documents.

            * @param self
            * @param path -> document name with path
            * @param data -> data needs to written into the document

            * @return None     
        """

        try:

            with open(f"{path}", "w") as f:  # open a document as f
                f.writelines(data)  # writes data to the document

        except:

            print(f"Error : Can't create {path}")
            sys.exit()  # exit the program
