#!/bin/bash

#install requirements
sudo apt-get update
sudo apt-get install python3-venv python3-pip -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

#run pytest with cov reports
cd server
python3 -m pytest --cov=app --cov-report term-missing
cd ..

cd class_api
python3 -m pytest --cov=class_app --cov-report term-missing
cd ..

cd race_api
python3 -m pytest --cov=race_app --cov-report term-missing
cd ..