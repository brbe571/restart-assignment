#!/bin/bash

#Create a simple shell script named install.sh 
#which installs the latest version of Python 
#and the required Python libraries (fastapi & uvicorn).

#check version
python3 --version
#update version for mac via homebrew
brew update && brew upgrade
#install fastapi
pip install fastapi
#installuvicorn
pip install "uvicorn[standard]"

#reference https://realpython.com/installing-python/