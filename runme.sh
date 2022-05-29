#!/bin/bash
#Create a simple shell script named runme.sh 
#which runs the uvicorn webserver on a publically accessible IP address (0.0.0.0:54321) 
#when the user types ./runme.sh into a shell


#run uvicron on 
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000