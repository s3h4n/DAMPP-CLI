""" This module will display outputs.

    - Messages.banner will print the program banner.
    - Messages.success will print the success message.
"""


class Display:

    def __init__(self):
        pass

    def banner(self, dampp_version):
        print(f" ____    _    __  __ ____  ____       ")
        print(f"|  _ \  / \  |  \/  |  _ \|  _ \      ")
        print(f"| | | |/ _ \ | |\/| | |_) | |_) |     ")
        print(f"| |_| / ___ \| |  | |  __/|  __/      ")
        print(f"|____/_/   \_\_|  |_|_|   |_|    v{dampp_version} ")
        print(f"\nDockerized Apache MySQL Php PhpMyAdmin\n")

    def success(self, project_name):
        print(
            f"\nDAMPP has been successfully installed in {project_name}")
        print(
            f"\nRun 'cd {project_name} && ./dampp run' and see the magic!")
