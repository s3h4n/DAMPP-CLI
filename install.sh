#!/bin/sh

# Name : DAMPP
# Version : 2.0
# Author : Sehan Weerasekara (S3H4N)
# Date : 19.01.2022
# Last Update : 23.01.2022
# Description : Script to install and run apache, mysql, phpmyadmin in docker.
# URL : https://github.com/s3h4n/dampp.git

res=$(tput sgr0)
bld=$(tput bold)
rev=$(tput rev)
grn=$(tput setaf 2)
red=$(tput setaf 1)
yel=$(tput setaf 3)
blu=$(tput setaf 4)

docker_vesion="3.3"

php_img="php:8.1.1-apache"
php_port="8000:80"

mysql_img="mysql:latest"
mysql_port="6033:3306"

pma_img="phpmyadmin:latest"
pma_port="8080:80"

banner() {
    echo "${bld}"
    echo "      ____    _    __  __ ____  ____       "
    echo "     |  _ \  / \  |  \/  |  _ \|  _ \      "
    echo "     | | | |/ _ \ | |\/| | |_) | |_) |     "
    echo "     | |_| / ___ \| |  | |  __/|  __/      "
    echo "     |____/_/   \_\_|  |_|_|   |_|    v2.0 "
    echo "${res}"
    echo "${rev}${bld}DAMPP : Dockerized Apache MySQL Php PhpMyAdmin${res}"
    echo ""
}

create_dockerfile() {
    touch Dockerfile
    echo "" >>Dockerfile
    echo "FROM $php_img" >>Dockerfile
    echo "RUN apt-get update && apt-get upgrade -y" >>Dockerfile
    echo "RUN docker-php-ext-install mysqli" >>Dockerfile
    echo "EXPOSE 80" >>Dockerfile
}

create_docker_compose() {
    touch docker-compose.yml
    echo "" >>docker-compose.yml
    echo "version: '$docker_version'" >>docker-compose.yml
    echo "" >>docker-compose.yml
    echo "services:" >>docker-compose.yml
    echo "" >>docker-compose.yml
    echo "  web:" >>docker-compose.yml
    echo "    build:" >>docker-compose.yml
    echo "      context: ./web" >>docker-compose.yml
    echo "      dockerfile: ../Dockerfile" >>docker-compose.yml
    echo "    container_name: $name_php" >>docker-compose.yml
    echo "    depends_on:" >>docker-compose.yml
    echo "      - db" >>docker-compose.yml
    echo "    volumes:" >>docker-compose.yml
    echo "      - ./web:/var/www/html" >>docker-compose.yml
    echo "    ports:" >>docker-compose.yml
    echo "      - $php_port" >>docker-compose.yml
    echo "" >>docker-compose.yml
    echo "  db:" >>docker-compose.yml
    echo "    container_name: $name_mysql" >>docker-compose.yml
    echo "    image: $mysql_img" >>docker-compose.yml
    echo "    command: --default-authentication-plugin=mysql_native_password" >>docker-compose.yml
    echo "    restart: always" >>docker-compose.yml
    echo "    environment:" >>docker-compose.yml
    echo "      MYSQL_ROOT_PASSWORD: $mysql_root_pass" >>docker-compose.yml
    echo "      MYSQL_DATABASE: $mysql_db" >>docker-compose.yml
    echo "      MYSQL_USER: $mysql_user" >>docker-compose.yml
    echo "      MYSQL_PASSWORD: $mysql_pass" >>docker-compose.yml
    echo "    ports:" >>docker-compose.yml
    echo "      - $mysql_port" >>docker-compose.yml
    echo "" >>docker-compose.yml
    echo "  phpmyadmin:" >>docker-compose.yml
    echo "    container_name: $name_pma" >>docker-compose.yml
    echo "    image: $pma_img" >>docker-compose.yml
    echo "    depends_on:" >>docker-compose.yml
    echo "      - db" >>docker-compose.yml
    echo "    restart: always" >>docker-compose.yml
    echo "    ports:" >>docker-compose.yml
    echo "      - $pma_port" >>docker-compose.yml
    echo "    environment:" >>docker-compose.yml
    echo "      - MYSQL_ROOT_PASSWORD: $mysql_root_pass" >>docker-compose.yml
    echo "      - MYSQL_DATABASE: $mysql_user" >>docker-compose.yml
    echo "      - MYSQL_PASSWORD: $mysql_pass" >>docker-compose.yml
    echo "" >>docker-compose.yml
}

install() {
    banner

    read -p "Project Name   (Default: example-app)  :: " p_name
    read -p "MySQL Database (Default: test)         :: " db
    read -p "MySQL Username (Default: admin)        :: " usr
    read -p "MySQL Password (Default: pass)         :: " psswd
    read -p "MySQL Root Password (Default: root)    :: " root_p

    if [ -z "$p_name" ]; then
        dir_name="example-app"
    else
        dir_name="$p_name"
    fi

    if [ -z "$db" ]; then
        mysql_db="test"
    else
        mysql_db="$db"
    fi

    if [ -z "$usr" ]; then
        mysql_user="admin"
    else
        mysql_user="$usr"
    fi

    if [ -z "$psswd" ]; then
        mysq_pass="pass"
    else
        mysq_pass="$psswd"
    fi

    if [ -z "$root_p" ]; then
        mysql_root_pass="root"
    else
        mysql_root_pass="$root_p"
    fi

    name_php="dampp-$dir_name-php"
    name_mysql="dampp-$dir_name-mysql"
    name_pma="dampp-$dir_name-pma"

    mkdir $dir_name $dir_name/web && cd $dir_name

    wget https://raw.githubusercontent.com/s3h4n/dampp/main/resources/dampp
    wget -P web/ https://raw.githubusercontent.com/s3h4n/dampp/main/resources/index.php

    chmod +x dampp

    create_dockerfile
    create_docker_compose
    docker-compose build && docker-compose up -d && docker-compose stop

    if [ "$?" = 0 ]; then
        echo ""
        echo "${bld}${grn}Success!${res}${bld} DAMPP has been installed in $dir_name.${res}"
        echo ""
        echo "Run 'cd $dir_name && ./dampp up' and see the magic!"
        echo ""
    else
        echo ""
        echo "${bld}${red}Failed!${res}${bld} DAMPP has already installed or something went wrong.${res}"
    fi
}

install
