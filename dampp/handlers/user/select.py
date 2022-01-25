""" This module will select user inputs.

    - Select.project_name will return the name of project.
    - Select.mysql_creds will return the database credentials.
    - Select.ports will return the port number.
"""

import sys


class Select:

    def __init__(self):
        pass

    def project_name(self):
        return input("Project Name \t(Default: my-app)\t:: ") or "my-app"

    def mysql_cred(self, data={}):
        """This function will ask user to enter values.
        If the input is empty, default values will be assigned.

        Returns:
            dictionary: Following keys can be used to access the data.
                        'd' = Database name, 
                        'u' = Username, 
                        'p' = Password, 
                        'r' = Root password, 
        """

        data["d"] = input("Database Name \t(Default: test)\t\t:: ") or "test"
        data["u"] = input("Username \t(Default: admin)\t:: ") or "admin"
        data["p"] = input("Password \t(Default: pass)\t\t:: ") or "pass"
        data["r"] = input("Root Password \t(Default: root)\t\t:: ") or "root"

        return data

    def port(self, service_name, default_port):
        try:
            txt = f"{service_name} \t\t(Default: {default_port})\t\t:: "
            port = int(input(txt) or (f"{default_port}"))
            return port if ((port > 0) and (port < 65535)) else exit()
        except:
            print("\nError : Port must be an integer between 0 and 655535.")
            sys.exit()
