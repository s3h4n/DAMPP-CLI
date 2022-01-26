"""
    * @import module sys 
"""

import sys


class Select:

    """
        * return user selected values or default values.
    """

    def __init__(self) -> None:
        """
            * declaring public method __init__()

            * @param self

            * @return None
        """

        pass

    def project_name(self) -> str:
        """
            * declaring public method project_name()
                - return user selected name or default name of the project

            * @param self

            * @return str
        """

        # if user input is empty default value will be assigned
        return input("Project Name \t(Default: my-app)\t:: ") or "my-app"

    def mysql_cred(self, data={}) -> dict:
        """
            * declaring public method mysql_cred()
                - return user selected database credentials or default values

            * @param self
            * @param data -> a dictionary to hold input values

            * @return dict
                        - 'd' -> Database name
                        - 'u' -> Username
                        - 'p' -> Password 
                        - 'r' -> Root password
        """

        # if user input is empty default value will be assigned
        data["d"] = input("Database Name \t(Default: test)\t\t:: ") or "test"

        # if user input is empty default value will be assigned
        data["u"] = input("Username \t(Default: admin)\t:: ") or "admin"

        # if user input is empty default value will be assigned
        data["p"] = input("Password \t(Default: pass)\t\t:: ") or "pass"

        # if user input is empty default value will be assigned
        data["r"] = input("Root Password \t(Default: root)\t\t:: ") or "root"

        return data

    def port(self, service_name, default_port) -> int:
        """
            * declaring public method port()
                - return user selected port number or default value

            * @param self
            * @param service_name -> name of the service
            * @param default_port -> default port

            * try -> @return int
            * except -> @return None
        """

        try:

            txt = f"{service_name} \t\t(Default: {default_port})\t\t:: "

            # if user input is empty default value will be assigned
            port = int(input(txt) or (f"{default_port}"))

            return port if ((port > 0) and (port < 65535)) else exit()

        except:

            print("\nError : Port must be an integer between 0 and 655535.")
            sys.exit()  # exit the program
