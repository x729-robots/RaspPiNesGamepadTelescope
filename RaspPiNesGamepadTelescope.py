#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 13:27:48 2021

@author: chuv
"""

"""from evdev import InputDevice
from os import listdir
from os.path import isfile, join
mypath='/dev/input/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


gamepad = InputDevice('/dev/input/event3')
print(gamepad)
if gamepad.name.replace(' ', '')=="USBgamepad" :
    print ("OK!!!")"""


import inputs
import time

def current_milli_time():
    return round(time.time() * 1000)
def getKeyAndState(event):    
    GamePadStates={
    'BTN_TOP2':{
        1:{'Key':'L','State':1},
        0:{'Key':'L','State':0}
        },
    'BTN_PINKIE':{
        1:{'Key':'R','State':1},
        0:{'Key':'R','State':0}
        },
    'ABS_Y':{
        0  :{'Key':'UP'  ,'State':1},
        127:{'Key':'UPandDOWN'  ,'State':0},
        255:{'Key':'DOWN','State':1},
        },
    'ABS_X':{
        0  :{'Key':'LEFT' ,'State':1},
        127:{'Key':'LEFTandRIGHT' ,'State':0},
        255:{'Key':'RIGHT','State':1},
        },
    'BTN_BASE3':{
        1:{'Key':'SELECT','State':1},
        0:{'Key':'SELECT','State':0}
        },
    'BTN_BASE4':{
        1:{'Key':'START','State':1},
        0:{'Key':'START','State':0}
        },
    'BTN_TRIGGER':{
        1:{'Key':'X','State':1},
        0:{'Key':'X','State':0}
        },
    'BTN_TOP':{
        1:{'Key':'Y','State':1},
        0:{'Key':'Y','State':0}
        },
    'BTN_THUMB':{
        1:{'Key':'A','State':1},
        0:{'Key':'A','State':0}
        },
    'BTN_THUMB2':{
        1:{'Key':'B','State':1},
        0:{'Key':'B','State':0}
        }    
    }
    if event.ev_type=='Key' or event.ev_type=='Absolute':
        return GamePadStates[event.code][event.state]
    else:
        return "No"

print(inputs.devices.gamepads)
pads = inputs.devices.gamepads



if len(pads) == 0:
    raise Exception("Couldn't find any Gamepads!")
i=0
while True:
    CurTime=current_milli_time()
    events = inputs.get_gamepad()
    NewTime=current_milli_time()
    if NewTime-CurTime>1000:
        print("---------------------------")
    for event in events:
        i+=1
        #print(i,event.ev_type, event.code, event.state)
        print(getKeyAndState(event))
        
"""
event.ev_type
Key or Absolute

event.code    event.state


BTN_TOP         1/0         Y
BTN_THUMB       1/0         A
BTN_THUMB2      1/0         B
---------------------------
BTN_TOP2        1/0         L
BTN_PINKIE      1/0         R
ABS_Y           0/127       UP
ABS_Y           255/127     DOWN
ABS_X           0/127       LEFT
ABS_X           255/127     RIGHT
BTN_BASE3       1/0         SELECT
BTN_BASE4       1/0         START
BTN_TRIGGER     1/0         X
BTN_TOP         1/0         Y
BTN_THUMB       1/0         A
BTN_THUMB2      1/0         B
"""