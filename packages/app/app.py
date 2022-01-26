class App:

    """
        * generates the data needed to create the main application.
    """

    def __init__(self) -> None:
        """
            * declaring public method __init__()

            * @param self

            * @return None
        """

        self.string = ""

    def export(self, app_version) -> str:
        """
            * declaring public method export()
                - will return the data required to build the application.

            * @param self

            * @param app_version -> application version

            * @return str             
        """

        string = self.string

        # details section
        string += '#!/bin/bash\n'
        string += '# Name : DAMPP\n'
        string += '# Version : 2.1\n'
        string += '# Author : Sehan Weerasekara (S3H4N)\n'
        string += '# Created : 19.01.2022\n'
        string += '# Description : Script to install and run apache, mysql, phpmyadmin in docker containers.\n'
        string += '# URL : https://github.com/s3h4n/dampp.git\n'

        # function section -> banner
        string += '\n# prints the program name.\n'
        string += 'banner() {\n'
        string += '    echo ""\n'
        string += '    echo " ____    _    __  __ ____  ____       "\n'
        string += '    echo "|  _ \  / \  |  \/  |  _ \|  _ \      "\n'
        string += '    echo "| | | |/ _ \ | |\/| | |_) | |_) |     "\n'
        string += '    echo "| |_| / ___ \| |  | |  __/|  __/      "\n'
        string += f'    echo "|____/_/   \_\_|  |_|_|   |_|    v{app_version} "\n'
        string += '    echo ""\n'
        string += '    echo "DAMPP : Dockerized Apache MySQL Php PhpMyAdmin"\n'
        string += '    echo ""\n'
        string += '}\n'

        # function section -> find port numbers
        string += '\n# find the service ports from docker-compose.yml.\n'
        string += 'find_port() {\n'
        string += '    var=$(grep -E "[[:digit:]]{4,10}" "docker-compose.yml")\n'
        string += '    arr=(${var//"-"/ })\n'
        string += '    web=(${arr[0]//":"/ })\n'
        string += '    db=(${arr[1]//":"/ })\n'
        string += '    pma=(${arr[2]//":"/ })\n'
        string += '}\n'

        # function section -> help
        string += '\n# help prompt.\n'
        string += 'help_page() {\n'
        string += '    echo ""\n'
        string += '    echo "Usage: ./dampp [COMMAND]"\n'
        string += '    echo ""\n'
        string += '    echo "Options:"\n'
        string += '    echo "  run     -  Start DAMPP containers"\n'
        string += '    echo "  stop    -  Stop DAMPP containers"\n'
        string += '    echo "  rm      -  Remove DAMPP containers"\n'
        string += '    echo ""\n'
        string += '    echo "Ports:"\n'
        string += '    echo "  $web       -  Apache server"\n'
        string += '    echo "  $pma       -  PhpMyAdmin"\n'
        string += '    echo "  $db       -  MySQL server"\n'
        string += '    echo ""\n'
        string += '    echo "Run "./dampp help" to access this menu."\n'
        string += '    echo ""\n'
        string += '    echo "Please use "docker --help" to learn more about using docker containers."\n'
        string += '    echo ""\n'
        string += '}\n'

        # function section -> start containers
        string += '\n# start the containers.\n'
        string += 'start() {\n'
        string += '    docker-compose up -d\n'
        string += '    echo ""\n'
        string += '    if [ "$?" = 0 ]; then\n'
        string += '        echo "DAMPP : Running!"\n'
        string += '        echo ""\n'
        string += '        echo "Default Ports:"\n'
        string += '        echo "    Server     : http://localhost:$web"\n'
        string += '        echo "    PhpMyAdmin : http://localhost:$pma"\n'
        string += '    else\n'
        string += '        echo "DAMPP : Failed!"\n'
        string += '        echo "DAMPP is already running or an error occured."\n'
        string += '    fi\n'
        string += '    echo ""\n'
        string += '}\n'

        # function section -> stop containers
        string += '\n# stop the containers.\n'
        string += 'stop() {\n'
        string += '    docker-compose stop\n'
        string += '    echo ""\n'
        string += '    if [ "$?" = 0 ]; then\n'
        string += '        echo "DAMPP : Stopped!"\n'
        string += '    else\n'
        string += '        echo "DAMPP : Failed!"\n'
        string += '        echo "DAMPP has already stopped or an error occured."\n'
        string += '    fi\n'
        string += '    echo ""\n'
        string += '}\n'

        # function section -> remove containers
        string += '\n# remove the containers.\n'
        string += 'remove() {\n'
        string += '    docker-compose down\n'
        string += '    echo ""\n'
        string += '    if [ "$?" = 0 ]; then\n'
        string += '        echo "DAMPP : Removed!"\n'
        string += '    else\n'
        string += '        echo "DAMPP : Failed!"\n'
        string += '        echo "DAMPP has already removed or an error occured."\n'
        string += '    fi\n'
        string += '    echo ""\n'
        string += '}\n'

        # main section
        string += '\nopt=$1\n'
        string += 'opt=${opt,,}\n'

        string += '\nfind_port\n'

        string += '\nif [ "$opt" = "run" ]; then\n'
        string += '    banner\n'
        string += '    start\n'
        string += 'elif [ "$opt" = "stop" ]; then\n'
        string += '    banner\n'
        string += '    stop\n'
        string += 'elif [ "$opt" = "rm" ]; then\n'
        string += '    banner\n'
        string += '    remove\n'
        string += 'elif [ "$opt" = "help" ]; then\n'
        string += '    banner\n'
        string += '    help_page\n'
        string += 'else\n'
        string += '    echo ""\n'
        string += '    echo "Wrong usage of commands!"\n'
        string += '    help_page\n'
        string += 'fi\n'

        return string
