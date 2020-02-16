import subprocess
import time

import os
from os import path

import sys
from sys import platform

import fnmatch

def _isDevConnected(Device):
    Dev_Path = "\dev\"" + Device
    Still_There = os.path.exists(Dev_Path)
    return Still_There

def _executeTrigger(Trigger):
    subprocess.call("sudo python ../triggers/" + Trigger)
    
def _getDevices():
    Devices = fnmatch.filter(os.listdir('/dev/'), '*disk*')
    Usable_Devices = []
    for Device in Devices:
        if Device.startswith("disk"):
            Usable_Devices.append(Device)
    return Usable_Devices

def _getTriggers():
    Triggers = fnmatch.filter(os.listdir('../triggers/'), '*.py')
    return Triggers
    
def _printTriggerList(Triggers):
    counter = 1
    for Trigger in Triggers:
        print(str(counter) + " - " + Trigger)
        counter = counter + 1

def _printDeviceList(Devices):
    counter = 1
    for Device in Devices:
        print(str(counter) + " - " + Device)
        counter = counter + 1

def _getDevName(Devices, number):
    number = number + 1
    return Devices[number]

def main():
    print("welcome to busKill CLI")
    time.sleep(1)
    print("Please Wait while we gather some information...")
    Available_Devices = _getDevices()
    Available_Triggers = _getTriggers()
    time.sleep(5)
    print("Ready to go!")
    time.sleep(2)
    if len(Available_Devices) == 0:
        Device_Name = str(input("please enter device name: "))
    else:
        _printDeviceList(Available_Devices)
        Dev = int(input("Please select option (using number): "))
        Device_Name = _getDevName(Available_Devices, Dev)
    _printTriggerList(Available_Triggers)
    Trig = int(input("Please select option (using number): "))
    Dev_Connected = _isDevConnected(Device_Name)
    if Dev_Connected == True:
        print(Dev + "is still connected - " + Dev_Connected)
    else:
        print("unexpected error occured")
    while Dev_Connected == True:
        time.sleep(5)#finish this
        if _isDevConnected(Device_Name) == False:
            Dev_Connected == False
            _execute_Trigger(Trig)
            sys.exit()

if __name__ == '__main__':
    main()
