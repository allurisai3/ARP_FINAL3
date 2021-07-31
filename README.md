# Assignment-3 (5060551 SAI KRISHNA RAMA CHANDER RAJU ALLURI)

**AIM**

By using socket as the IPC primitive make philosopher to enter, sit and eat endlessly and makes a philsopher to stop eating and exiting.

**MODULES THAT NEED TO BE INSTALLED BEFORE**

pip3 install multiprocessing && pip3 import time && pip3 import random


**EXCUTING THE CODE**

python3 p1.py

In new terminal

python3 main.py

**ABOUT THE CODE**


We have 2 different python files: main.py and p1.py. Each one represents the 2 processes and these 2 processes' connection is provided via socket. Each files must be run in different shell window . The main.py writes to the socket in order to p1.py read from same socket which is local URL port is 8888 in this case. It is arbitrary to choose the port but it must be local. We have 5 philosopher and each one enter the restaurant, sit in the place, start to eat in randomly given time interval between 3 to 15 seconds, queued on a FIFO basis. These data send to p1.py process via socket. After each philosopher finishes the operation the main.py prints out philosopher stop eating and left.At the end it sends close message to p1.py that triggers the close the connection between 2 processes.


**EXPECTED RESULTS**

p1.py gives the result:

philosopher 0 enter the restaurant
philosopher 0 sit in the place
philosopher 0 started to eating

after that in the main.py window prints out

philosopher 1 stop eating and leave restaurant

THEN

p1.py prints result below after some seconds between 3 to 33

philosopher 2 enter the restaurant
philosopher 2 sit in the place
philosopher 2 started to eating

main.py

philosopher 2 stop eating and leave restaurant

this processes continue for 5 philosophers
