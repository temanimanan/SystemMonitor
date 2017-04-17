#!/usr/bin/env python
import sys
import random
import time

print("Writing the file now...\n" )
while(1):
    time.sleep(1)
    statusFile = open('../NS/var/log/status.txt','w')    
    rand = random.randint(1, 100)
    if(rand%2 == 0):   
        statusFile.write('ALERT')
    else:
        statusFile.write('OK')
    
    statusFile.close()
