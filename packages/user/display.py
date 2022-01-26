class Display:

    """
        * print messages in the console
    """

    def __init__(self) -> None:
        """
            * declaring public method __init__()

            * @param self

            * @return None
        """

        pass

    def banner(self, app_version) -> None:
        """
            * declaring public method banner()
                - prints the application banner

            * @param self
            * @param app_version -> version of the application

            * @return None
        """

        print(f" ____    _    __  __ ____  ____       ")
        print(f"|  _ \  / \  |  \/  |  _ \|  _ \      ")
        print(f"| | | |/ _ \ | |\/| | |_) | |_) |     ")
        print(f"| |_| / ___ \| |  | |  __/|  __/      ")
        print(f"|____/_/   \_\_|  |_|_|   |_|    v{app_version} ")

        print(f"\nDockerized Apache MySQL Php PhpMyAdmin\n")

    def success(self, project_name) -> None:
        """
            * declaring public method success()
                - return the service details of web server

            * @param self
            * @param project_name -> name of the project

            * @return None
        """

        print(
            f"\nDAMPP has been successfully installed in {project_name}")

        print(
            f"\nRun 'cd {project_name} && ./dampp run' and see the magic!")
