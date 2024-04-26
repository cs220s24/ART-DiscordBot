#!/bin/bash

# Installs Pip
sudo yum install -y pip

#Installs redis
sudo yum install -y redis6 

# Installs the requirements for the bot
.venv/bin/pip install -r requirements.txt

# Enables the redis files
sudo systemctl enable redis6

# Downloads and starts docker
sudo yum install -y docker
sudo systemctl enable docker
sudo systemctl start docker

# Allow access to the ec2 user
sudo usermod -a -G docker ec2-user

echo "------------------------------------------"
echo "Nano .env file and log out and log back in"
echo "------------------------------------------"

