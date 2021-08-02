# capstoneproject-comp3900-w10a-clickdown

# Introduction
Be a master of tracking where you and your collaborators are with tasks that you've got
an interest in, and use TaskMaster. This platform will allow task masters to maintain a
profile that shows tasks being worked on at a glance, where task masters can connect
with others on the platform, and communicate the state of each of their tasks through
the platform. It provides an easy way to create and assign tasks to task masters you
collaborate with, and search for any tasks within your network of task master
collaborators. You can even see an estimate of how busy each of your connected task
masters is.

# How to run

**3rd party requirements:**
Ngrok is needed in order to correctly forward the local deployment to dialogflow for running the chatbot.
Ngrok can be downloaded from here:
https://ngrok.com/download

**Run three terminals**
*Run the backend from folder #1 (backend) and the frontend from folder #2 (frontend)*
1. cd backend
2. cd frontend
3. ngrok.exe

**BACKEND**
**installation**
1. pip3 install -r requirements.txt
2. sudo apt-get install sqlite3

**running the app**
1. python3 ./init_database.py
2. python3 ./server.py

**FRONTEND**
**installation**
1. yarn install

**running the app**
1. yarn start

**Once running, do the following in terminal 3 (the one running the ngrok.exe)**
1. /ngrok authtoken 1fO0GH3r1oJj1g1d2NkAhF6Ofhu_2yJz2aRc9WaN7aEgdMQb8
2. ngrok.exe http -region=au -hostname=comp3900.au.ngrok.io 5000

This will expose port 5000 to the public url comp3900.au.ngrok.io which allows Dialogflow to send processed messages.

**Accessing the web page**
1. http://localhost:3000 

**Accessing all apis (swagger doc)**
1. http://localhost:5000

## Issues
It will take a while to install all the dependencies in this project. Furthermore, launching the app will also take times. Please contact us if there is anything wrong, appreciated.

## Teams
- Nicholai Rank `z5115301@unsw.edu.au`
- Gavin Wang `z5206647@student.unsw.edu.au`
- Justin Pham `z5075823@student.unsw.edu.au`
- Ka Wayne Ho `z5139681@student.unsw.edu.au`
- Yue Qi `z5219951@student.unsw.edu.au`
