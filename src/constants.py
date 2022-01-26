# docker version and program version

APP_V = "2.2.2"
DOCKER_V = "3.3"


# docker images

WEB_IMAGE = "php:8.1.1-apache"
DB_IMAGE = "mysql:latest"
PMA_IMAGE = "phpmyadmin:latest"


# default service names and ports

DEFAULT_WEB = ["PHP", "8000"]
DEFAULT_DB = ["MySQL", "6033"]
DEFAULT_PMA = ["PMA", "8001"]


# user input sections

SECTION_1 = "\n=== PROJECT DETAILS ======================\n"
SECTION_2 = "\n\n=== MySQL CREDENTIALS ====================\n"
SECTION_3 = "\n\n=== PORTS ================================\n"
