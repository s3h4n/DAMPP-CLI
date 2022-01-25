"""
    Name : DAMPP

    Version : 2.2

    Author : Sehan Weerasekara (S3H4N)

    Date : 19.01.2022

    Description : Script to install and run apache, mysql, phpmyadmin in docker containers.

    URL : https://github.com/s3h4n/dampp.git

"""

# Import
from .handlers import File
from .handlers import Command
from .handlers import Create
from .handlers import Service
from .handlers import Display
from .handlers import Select

# Global vars
dampp_v = "2.2"  # Program version
docker_v = "3.3"  # Docker version

web_img = "php:8.1.1-apache"  # Php image
db_img = "mysql:latest"  # MySQL image
pma_img = "phpmyadmin:latest"  # PhpMyAdmin image

php_d = ["PHP", "8000"]  # service name and default port
db_d = ["MySQL", "6033"]  # service name and default port
pma_d = ["PMA", "8001"]  # service name and default port


def run():
    # Instance from Command class
    cmd = Command()

    # Clear screen
    cmd.run("clear")

    # Instance from Message class
    msg = Display()

    # Print banner
    msg.banner(dampp_v)

    # Instance from Select class
    select = Select()

    # Choose project name
    print("\n=== PROJECT DETAILS ======================\n")
    project = select.project_name()

    # Choose MySQL credentials
    print("\n\n=== MySQL CREDENTIALS ====================\n")
    db = select.mysql_cred()

    # Choose ports for services
    print("\n\n=== PORTS ================================\n")

    web_port = select.port(php_d[0], php_d[1])  # Web port

    while (True):
        db_port = select.port(db_d[0], db_d[1])  # Database port
        if (db_port != web_port):
            break
        # Error if port is using
        print(f"Error : Port is used for {php_d[0]}.")

    while (True):
        pma_port = select.port(pma_d[0], pma_d[1])  # PhpMyAdmin port
        if (pma_port != db_port and pma_port != web_port):
            break
        print(
            f"Error : Port is used for {php_d[0] if (pma_port==web_port) else db_d[0]}.")  # Error if port is using

    # Instance from Service class
    service = Service(project)

    # Generate details about services
    serv1 = service.web(port=web_port)
    serv2 = service.db(
        image=db_img,
        database=db["d"],
        username=db["u"],
        password=db["p"],
        root_password=db["r"],
        port=db_port,
    )
    serv3 = service.pma(
        image=pma_img,
        port=pma_port,
    )

    # Instance from File class
    fp = File(project)

    # Generate files
    file1 = fp.dockerfile(image=web_img)
    file2 = fp.docker_compose(
        docker_version=docker_v,
        service_web=serv1,
        service_db=serv2,
        service_pma=serv3,
    )
    file3 = fp.index_dot_php(pma_port=pma_port)

    # Instance from Create class
    build = Create(project)

    # Directory paths
    dir_path1 = f"{project}"
    dir_path2 = f"{project}/web"

    # Document paths
    doc_path1 = f"{dir_path1}/Dockerfile"
    doc_path2 = f"{dir_path1}/docker-compose.yml"
    doc_path3 = f"{dir_path2}/index.php"

    # Build directories and documents
    build.directory(dir_path1)
    build.directory(dir_path2)
    build.document(doc_path1, file1)
    build.document(doc_path2, file2)
    build.document(doc_path3, file3)

    # Install DAMPP
    cmd.run(f"cp dampp/scripts/dampp {project}/")
    cmd.run(f"echo && cd {project}")
    cmd.run(f"chmod +x dampp")
    cmd.run(f"docker-compose build && docker-compose up -d && docker-compose stop")

    # Print success message
    msg.success(project)
