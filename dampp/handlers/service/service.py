""" This module will help to generate service details.

    - Services.web will return the details of web service.
    - Services.db will return the details of db service.
    - Services.pma will return the details of phpmyadmin service.
"""


class Service:

    def __init__(self, project_name):
        self.project_name = project_name
        self.line = ""
        self.t = " "

    def web(self, port: str = ...):
        l, t = self.line, self.t
        l += f"\n{t*2}web:\n"
        l += f"{t*4}build:\n"
        l += f"{t*6}context: ./web\n"
        l += f"{t*6}dockerfile: ../Dockerfile\n"
        l += f"{t*4}container_name: dampp-{self.project_name}-php\n"
        l += f"{t*4}depends_on:\n"
        l += f"{t*6}- db\n"
        l += f"{t*4}volumes:\n"
        l += f"{t*6}- ./web:/var/www/html\n"
        l += f"{t*4}ports:\n"
        l += f"{t*6}- {port}:80\n"

        return l

    def db(self, image: str = ..., database: str = ..., username: str = ..., password: str = ..., root_password: str = ..., port: str = ...):
        l, t = self.line, self.t
        l += f"\n{t*2}db:\n"
        l += f"{t*4}container_name: dampp-{self.project_name}-mysql\n"
        l += f"{t*4}image: {image}\n"
        l += f"{t*4}command: --default-authentication-plugin=mysql_native_password\n"
        l += f"{t*4}restart: always\n"
        l += f"{t*4}environment:\n"
        l += f"{t*6}MYSQL_ROOT_PASSWORD: {root_password}\n"
        l += f"{t*6}MYSQL_DATABASE: {database}\n"
        l += f"{t*6}MYSQL_USER: {username}\n"
        l += f"{t*6}MYSQL_PASSWORD: {password}\n"
        l += f"{t*4}ports:\n"
        l += f"{t*6}- 3360:{port}\n"

        return l

    def pma(self, image: str = ..., port: str = ...):
        l, t = self.line, self.t
        l += f"\n{t*2}phpmyadmin:\n"
        l += f"{t*4}container_name: dampp-{self.project_name}-pma\n"
        l += f"{t*4}image: {image}\n"
        l += f"{t*4}depends_on:\n"
        l += f"{t*6}- db\n"
        l += f"{t*4}restart: always\n"
        l += f"{t*4}ports:\n"
        l += f"{t*6}- {port}:80\n"
        l += f"{t*4}environment:\n"
        l += f"{t*6}- PMA_ARBITRARY=1\n"

        return l
