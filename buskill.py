#!/usr/bin/env python

import os
import time
import sys
import fnmatch
import subprocess
import datetime

def print_help():
    print(
    """
    For Normal Usage:
        BusKill.py -D Device_Name -T Trigger_Name
    triggers
        -T  -- USed to define the Trigger Buskill is configured to use
        -Q  -- Reads the TrigInfo.txt, this file contains information about the Trigger
        -LT -- Lists Installed Triggers on the system
    Devices
        -D  -- Used to define the Device Buskill is configured to use
        -LD -- Creates a List for available Devices within MacOSX
    Configuration
        -SC -- Creates a configuration File. Use -SC at the end of normal usage to save the config
        -CC -- Clears the Configuration File created by -SC
        -C  -- Uses a Configuration File, Must be created by -SC
    other
        -H  -- Reads the Help File
    """)

def Find_Run_Path():
    dirname = os.path.abspath(__file__).split("/")
    del dirname[len(dirname) - 1]
    return "/".join(dirname)

def Write_Log(LOG_LOCATION, LEVEL, MESSAGE):
    with open(LOG_LOCATION, "a") as logfile:
        logfile.write(str(datetime.datetime.now().ctime()) + " - " +  LEVEL + " - " + MESSAGE + "\n")

def Validation(LOG_LOCATION, Device, Trigger):
    for trigger in Get_Triggers():
        if Trigger.strip() == trigger:
            Trig = True
            break
        else:
            Trig = False

    if Trig != True:
        Write_Log(LOG_LOCATION, "ERROR", Trigger + " was not found")
    else:
        Write_Log(LOG_LOCATION, "INFO", Trigger + " was found")

    for device in Get_Devices():
        if Device.strip() == device:
            Dev = True
            break
    try:
        if Dev != True:
            Dev = False
            Write_Log(LOG_LOCATION, "ERROR", Device + " was not found")
        else:
            Write_Log(LOG_LOCATION, "INFO", Device + " was found")
    except UnboundLocalError:
        print("Device was not found.")
        Write_Log(LOG_LOCATION, "ERROR", Device + " was not found")
        return

    return (Dev and Trig)

def Check_Device(LOG_LOCATION, Device):
    if os.path.exists("/dev/"+Device) == True:
        return True
    else:
        Write_Log(LOG_LOCATION, "INFO", Device + " has been removed")
        return False

def Execute_Trigger(LOG_LOCATION, Trigger):
    try:
        Write_Log(LOG_LOCATION, "INFO", "Device Removal Detected!" + Trigger + " Executing")
        subprocess.call("python Trigger.py", shell = True)

    except IOError:
        Write_Log(LOG_LOCATION, "ERROR", Trigger + " has not been found. Application Error")
        print("Something went wrong!")

def Normal_Operation(LOG_LOCATION, Device, Trigger):
    os.chdir("Triggers/"+Trigger+"/")
    print("BusKill is now running")
    Triggered = False
    try:
        while Triggered == False:
            if Check_Device(LOG_LOCATION, Device) == False:
                Execute_Trigger(LOG_LOCATION ,Trigger)
                Write_Log(LOG_LOCATION, "INFO", "BusKill executed")
                Triggered = True
                time.sleep(5)
    except KeyboardInterrupt:
        Write_Log(LOG_LOCATION, "INFO", "BusKill was stopped via a KeyboardInterrupt")
        print("\n BusKill Stopped")

def Save_Configuration(LOG_LOCATION, Device, Trigger):
    if os.path.exists("config.txt") == True:
        Write_Log(LOG_LOCATION, "ERROR", "Configuration Change attempted, failed due to Configuration existing")
        print("CONFIG ALREADY EXISTS.")
        print("PLEASE USE -CC TO CLEAR THE CONFIG")
        Write_Log(LOG_LOCATION, "WARNING", "Attempted config save. However, already existed")
    else:
        with open("config.txt", "a") as config:
            config.write("THIS FILE CAN BE MODIFIED MANUALLY. IF IT FAILS VALIDATION PLEASE USE - \n")
            config.write("Device:" + Device + "\n")
            config.write("Trigger:" + Trigger + "\n")
        Write_Log(LOG_LOCATION, "INFO", "Config saved.")


def Get_Dev_From_Conf():
    with open("config.txt") as conf:
        return conf.readlines()[1].split(":")[1]

def Get_Trig_From_Conf():
    with open("config.txt") as conf:
        return conf.readlines()[2].split(":")[1]

def Clear_Config(LOG_LOCATION):
    if os.path.exists("config.txt") == False:
        print("No Config found!! Nothing to clear")
        Write_Log(LOG_LOCATION, "INFO", "Config Removal attempted, not found")
    else:
        os.remove("config.txt")
        if os.path.exists("config.txt"):
            print("Internal Error, Please Try again (or raise a user story on Github)")
            Write_Log(LOG_LOCATION, "ERROR", "BusKill could not remove the config file")
        else:
            print("Config Cleared!")
            Write_Log(LOG_LOCATION, "WARNING", "Configuration Removed")


def Get_Devices():
    Devices = os.listdir("/dev/")
    Disk_Devices = []
    for Device in Devices:
        if fnmatch.fnmatch(Device, "*disk*"):
            if Device.startswith("r") == False:
                if fnmatch.fnmatch(Device, "*isk*s*") == False:
                    if Device.endswith("1") == False:
                        if Device.endswith("0") == False:
                            Disk_Devices.append(Device)
    return Disk_Devices

def List_Devices():
    Devices = Get_Devices()
    counter = 0
    for Device in Devices:
        counter = counter + 1
        print(str(counter) + " - " + Device)

def Get_Triggers():
    Triggers = []
    dirlist = os.listdir("Triggers/")
    for dir in dirlist:
        if os.path.isdir("Triggers/"+dir) == True:
            Triggers.append(dir.lower())
    return Triggers

def List_Triggers():
    Triggers = Get_Triggers()
    counter = 0
    for Trigger in Triggers:
        counter = counter + 1
        print(str(counter) + " - " + Trigger)

def Query_Trigger(Trigger):
    with open("Triggers/"+Trigger+"/TriggerInfo.txt") as InfoFile:
        DATA = InfoFile.read().splitlines()
        for line in DATA:
            print(line)

def Main(args):
    dirname = Find_Run_Path()
    LOG_LOCATION = dirname + "/log.txt"
    #remeber to change where all the write logs are pointing to 
    os.chdir(dirname)
    Dev = False
    Trig = False
    Quer = False
    Query = False
    Config = False
    Clear_Conf = False
    Save_Conf = False
    Help = False
    List_Trig = False
    List_Dev = False
    for index, arg in enumerate(args):
        if arg.upper() == "-T":
            Trig = True
            Trigger = index
        elif arg.upper() == "-Q":
            Quer = True
            Query = index
        elif arg.upper() == "-D":
            Dev = True
            Device = index
        elif arg.upper() == "-SC":
            Save_Conf = True
        elif arg.upper() == "-C":
            Config = True
        elif arg.upper() == "-CC":
            Clear_Conf = True
        elif arg.upper() == "-H":
            Help = True
        elif arg.upper() == "-LT":
            List_Trig = True
        elif arg.upper() == "-LD":
            List_Dev = True

    if Dev and Trig == True:
        Device = args[Device + 1]
        Trigger = args[Trigger + 1]
        if Validation(LOG_LOCATION, Device, Trigger):
            if Save_Conf == True:
                Save_Configuration(LOG_LOCATION, Device, Trigger)
            Normal_Operation(LOG_LOCATION, Device, Trigger)
            sys.exit()
        else:
            print("Something went wrong")
            sys.exit()

    if Quer == True:
        Trigger = args[Query+1]
        with open("/Triggers/"+Trigger+"/TriggerInfo.txt") as InfoFile:
            print(InfoFile.readline())
        sys.exit()

    if Config == True:
        Device = Get_Dev_From_Conf().strip()
        Trigger = Get_Trig_From_Conf().strip()
        if Validation(LOG_LOCATION, Device, Trigger):
            Write_Log(LOG_LOCATION, "INFO", "Validation passed for " + Device + " and " + Trigger)
            Normal_Operation(LOG_LOCATION, Device, Trigger)
            sys.exit()
        else:
            Write_Log(LOG_LOCATION, "ERROR", "Validation failed for " + Device + " and " + Trigger)
            print("Invalid Device or Trigger")
            sys.exit()

    if Clear_Conf == True:
        Clear_Config(LOG_LOCATION)
        sys.exit()

    if List_Trig == True:
        List_Triggers()
        sys.exit()

    if List_Dev == True:
        List_Devices()
        sys.exit()

    if Help == True:
        print_help()
        sys.exit()

    else:
        print_help()

Main(sys.argv)