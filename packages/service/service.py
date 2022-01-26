class Service:

    """
        * return the services data
    """

    def __init__(self, project_name) -> None:
        """
            * declaring public method __init__()

            * @param self
            * @param project_name -> name of the project

            * @return None
        """

        self.project_name = project_name
        self.string = ""
        self.space = " "

    def web(self,
            port: str = ...) -> str:
        """
            * declaring public method web()
                - return the service details of web server

            * @param self
            * @param port -> port number of web server

            * @return str
        """

        string = self.string
        space = self.space

        string += f"\n{space*2}web:\n"
        string += f"{space*4}build:\n"
        string += f"{space*6}context: ./web\n"
        string += f"{space*6}dockerfile: ../Dockerfile\n"
        string += f"{space*4}container_name: dampp-{self.project_name}-php\n"
        string += f"{space*4}depends_on:\n"
        string += f"{space*6}- db\n"
        string += f"{space*4}volumes:\n"
        string += f"{space*6}- ./web:/var/www/html\n"
        string += f"{space*4}ports:\n"
        string += f"{space*6}- {port}:80\n"

        return string

    def db(self,
           image: str = ...,
           database: str = ...,
           username: str = ...,
           password: str = ...,
           root_password: str = ...,
           port: str = ...) -> str:
        """
            * declaring public method db()
                - return the service details of database server

            * @param self
            * @param image -> name of the mysql image
            * @param database -> name of the database
            * @param username -> database username
            * @param password -> database password
            * @param root_password -> database root password
            * @param port -> port number of database server

            * @return str
        """

        string = self.string
        space = self.space

        string += f"\n{space*2}db:\n"
        string += f"{space*4}container_name: dampp-{self.project_name}-mysql\n"
        string += f"{space*4}image: {image}\n"
        string += f"{space*4}command: --default-authentication-plugin=mysql_native_password\n"
        string += f"{space*4}restart: always\n"
        string += f"{space*4}environment:\n"
        string += f"{space*6}MYSQL_ROOT_PASSWORD: {root_password}\n"
        string += f"{space*6}MYSQL_DATABASE: {database}\n"
        string += f"{space*6}MYSQL_USER: {username}\n"
        string += f"{space*6}MYSQL_PASSWORD: {password}\n"
        string += f"{space*4}ports:\n"
        string += f"{space*6}- 3360:{port}\n"

        return string

    def pma(self,
            image: str = ...,
            port: str = ...) -> str:
        """
            * declaring public method pma()
                - return the service details of phpmyadmin

            * @param self
            * @param image -> name of the phpmyadmin image
            * @param port -> port number of phpmyadmin

            * @return str
        """

        string = self.string
        space = self.space

        string += f"\n{space*2}phpmyadmin:\n"
        string += f"{space*4}container_name: dampp-{self.project_name}-pma\n"
        string += f"{space*4}image: {image}\n"
        string += f"{space*4}depends_on:\n"
        string += f"{space*6}- db\n"
        string += f"{space*4}restart: always\n"
        string += f"{space*4}ports:\n"
        string += f"{space*6}- {port}:80\n"
        string += f"{space*4}environment:\n"
        string += f"{space*6}- PMA_ARBITRARY=1\n"

        return string
