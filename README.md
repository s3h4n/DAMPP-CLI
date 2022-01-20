# DAMP 🚢

DAMP is a linux shell script to setup MySQL, Php, Apache, PhpMyAdmin inside of docker containers on any Ubuntu based system.

## Prerequisite ✔️
You must have <a href="https://docs.docker.com/engine/install/ubuntu/" target="_blank">Docker</a> installed in your system.
If your system is **Ubuntu based**, and it doesn't have Docker, you can install it by using <a href="https://github.com/s4nduni/docker-installer.git" target="_blank">docker-installer</a>. 

## Installation ✨

Clone the repository.
```bash
git clone https://github.com/s3h4n/damp.git
cd damp
```

## Usage 🔥

Use -s to start containers.
```bash
./damp -s
```
Use -c to stop containers.
```bash
./damp -c
```
Use -rm to remove containers.
```bash
./damp -rm
```
Use -h to access help menu.
```bash
./damp -h
```

## Contributing 🤝
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
