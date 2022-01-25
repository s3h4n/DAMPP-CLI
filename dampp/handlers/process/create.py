""" 
    - Create.directory will build directories.
    - Create.document will build documents.
"""

import sys
import os


class Create:

    def __init__(self, project_name):
        self.project_name = project_name

    def directory(self, path):
        try:
            os.mkdir(f"{path}")
        except FileExistsError:
            print(f"\nError : {path} already exists.")
            sys.exit()
        except Exception:
            print(f"\nError : Can't create {path}.")
            sys.exit()

    def document(self, path, data):
        try:
            with open(f"{path}", "w") as f:
                f.writelines(data)
        except:
            print(f"Error : Can't create {path}")
            sys.exit()
