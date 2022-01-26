"""
    * @import module constants as c
    * @import module packages as p
"""

from . import constants as c
from ..packages import App
from ..packages import File
from ..packages import Command
from ..packages import Create
from ..packages import Service
from ..packages import Select
from ..packages import Display


class Handler:

    """
        * this will handle the setup process
    """

    def __init__(self) -> None:
        """
            * declaring public method __init__()

            * @param self

            * @return None
        """

        pass

    def handler(self) -> None:
        """
            * declaring public method handler()

            * @param self

            * @return None
        """

        app_v = c.APP_V  # app version
        docker_v = c.DOCKER_V  # docker version

        img_web = c.WEB_IMAGE  # php-apache image
        img_db = c.DB_IMAGE  # mysql image
        img_pma = c.PMA_IMAGE  # phpmyadmin image

        default_web = c.DEFAULT_WEB  # default web name and port
        default_db = c.DEFAULT_DB  # default db name and port
        default_pma = c.DEFAULT_PMA  # default phpmyadmin name and port

        sec_project = c.SECTION_1  # project name section
        sec_db = c.SECTION_2  # database section
        sec_port = c.SECTION_3  # port section

        cmd = Command()  # instance from command class
        msg = Display()  # instance from display class
        choice = Select()  # instance from select class
        app = App()  # instance from app class

        cmd.run("clear")  # clear the console

        msg.banner(app_v)  # display appliction banner

        # project section
        print(sec_project)
        project = choice.project_name()

        # database section
        print(sec_db)
        db_data = choice.mysql_cred()

        # port section
        print(sec_port)

        port_web = choice.port(default_web[0], default_web[1])  # web port

        while (True):

            port_db = choice.port(default_db[0], default_db[1])  # db port

            if (port_db != port_web):
                break

            # print error if port is using
            print(f"Error : Port is used for {default_web[0]}.")

        while (True):

            port_pma = choice.port(default_pma[0], default_pma[1])  # pma port

            if (port_pma != port_db and port_pma != port_web):
                break

            # print error if port is using
            print(f"Error : Port is used for \
                    {default_web[0] if (port_pma==port_web) else default_web[0]}.")

        srv = Service(project)  # instance from service class
        fp = File(project)  # instance from file class
        build = Create(project)  # instance from create class

        # generate details of web service
        srv_web = srv.web(port=port_web)

        # generate details of database service
        srv_db = srv.db(
            image=img_db,
            database=db_data["d"],
            username=db_data["u"],
            password=db_data["p"],
            root_password=db_data["r"],
            port=port_db,
        )

        # generate details of phpmyadmin service
        srv_pma = srv.pma(
            image=img_pma,
            port=port_pma,
        )

        # generate details of dockerfile
        file_docker = fp.dockerfile(
            image=img_web
        )

        # generate details of docker-compose.yml
        file_dcompose = fp.docker_compose(
            docker_version=docker_v,
            service_web=srv_web,
            service_db=srv_db,
            service_pma=srv_pma,
        )

        # generate details of index.php
        file_index = fp.index_dot_php(
            pma_port=port_pma
        )

        # generate details of the app
        file_app = app.export(app_v)

        dir_path_project = f"{project}"  # directory path for the project
        dir_path_web = f"{project}/web"  # directory path for the web

        # file path for the dockerfile
        path_docker = f"{dir_path_project}/Dockerfile"
        # file path for the docker-compose.yml
        path_dcompose = f"{dir_path_project}/docker-compose.yml"
        # file path for the dampp(app)
        path_app = f"{dir_path_project}/dampp"
        # file path for the index.php
        path_index = f"{dir_path_web}/index.php"

        # build directories
        build.directory(dir_path_project)
        build.directory(dir_path_web)

        # build files
        build.document(path_docker, file_docker)
        build.document(path_dcompose, file_dcompose)
        build.document(path_index, file_index)
        build.document(path_app, file_app)

        # finalize the project
        cmd.run(f"echo")
        cmd.run(f"cd {project} && chmod +x dampp")

        # print success state
        msg.success(project)
