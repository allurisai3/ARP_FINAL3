from multiprocessing.connection import Client
import time
import random

# Client 1

conn = Client(('localhost', 3333), authkey=b'secret password') 

# write to the socket which url port which is local 3333
i = 0
while(i!=5):
    conn.send("philosopher "+str(i)+" enter the restaurant")
    conn.send("philosopher "+str(i)+" sit in the place")
    conn.send("philosopher "+str(i)+" started to eating")
    #send these messages to the listener process via socket 
    time.sleep(random.randint(3, 33))
    #choose random time interval between 3 and 33 seconds for every operation
    
    print("philosopher "+str(i)+" stop eating and leave restaurant")
    i+=1
    #when next philosopher and current philosopher eating time finishes print in 
    #the shell window
   
conn.send('close')
conn.close()

#after wihile loop finishes its job sends to the P1 close message
