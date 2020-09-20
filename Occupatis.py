import psutil
 
import requests

import time

#import JSON

nut = 1

data = 0

data2 = 0

URL = 'URL goes here'
 
y = {"Zoom": '0'}

z = ['1']

ab = ['0']

z1 = [z, z]

ab1 = [ab, ab]
 
# By Sanix darker
# With this script you can check if a process is running by it's name
#
# Install dependencies by hiting : pip install psutil
#
# Then launch the script : python checkIfProcessRunning.py


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
    
 
# Check if any chrome process was running or not.

#Some of this function is mine and some is from the person above
def checker(name):
    j = {'Zoom' : '0'}
    if checkIfProcessRunning(name):
        print('The program is active')
        j['Zoom'] = '1'
        #x = requests.post(url = URL, data = {'meet': 'True'}, headers = {'id': 'Zoom'})
        x = requests.post(url = URL, data = {'Status': 'yes'}, headers = {'program': 'Zoom'})
        print(x)
    else:
        print('The program is not active')
        j['Zoom'] = '0'
        #x = requests.post(url= URL, data = {'meet': 'False'}, headers = {'id': 'Zoom'})
        x = requests.post(url= URL, data = {'Status': 'no'}, headers = {'program': 'Zoom'})
        print(x)
    return(j)
    
    
    # The code below is mine and not taken from github
    
while(nut == 1):
    time.sleep(2)
    y =  checker('Zoom')
    if (y['Zoom'] == '0' and data == 0):
        data = 0
    if (y['Zoom'] == '1' and data == 0):
        data = 1
    if (y['Zoom'] == '0' and data == 1):
        data = 0
    #g = input()
    #if(g == 'Terminate'):
    #    exit()
