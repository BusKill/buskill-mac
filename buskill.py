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

def Write_Log(LEVEL, MESSAGE):
    with open("log.txt", "a") as logfile:
        logfile.write(str(datetime.date.today().ctime()) + " - " +  LEVEL + " - " + MESSAGE + "\n")

def Find_Run_Path():
    full_path=sys.argv[0].split("/")
    length = len(full_path)
    del full_path[length-1]
    return "/".join(full_path)

def Validation(Device, Trigger):
    print(Device)
    print(Trigger)
    for trigger in Get_Triggers():
        if Trigger.strip() == trigger:
            Trig = True
            break
        else:
            Trig = False

    if Trig != True:
        Write_Log("ERROR", Trigger + " was not found")
    else:
        Write_Log("INFO", Trigger + " was found")

    for device in Get_Devices():
        if Device.strip() == device:
            Dev = True
            break
    if Dev != True:
        Dev = False
        Write_Log("ERROR", Device + " was not found")
    else:
        Write_Log("INFO", Device + " was found")

    return (Dev and Trig)

def Check_Device(Device):
    if os.path.exists("/dev/"+Device) == True:
        return True
    else:
        return False
        Write_Log("INFO", Device + " has been removed")

def Execute_Trigger(Trigger):
    os.chdir(Find_Run_Path() + "/Triggers/" + Trigger)
    try:
        Write_Log("INFO", "Device Removal Detected!" + Trigger + "Executing")
        subprocess.call("python Trigger.py", shell = True)

    except IOError, OSError:
        Write_Log("ERROR", Trigger + " has not been found. Application Error")
        print("Something went wrong!")

def Normal_Operation(Device, Trigger):
    os.chdir("Triggers/"+Trigger+"/")
    print("BusKill is now running")
    Triggered = False
    try:
        while Triggered == False:
            if Check_Device(Device) == False:
                Execute_Trigger(Trigger)
                Triggered = True
                time.sleep(5)
    except KeyboardInterrupt:
        Write_Log("INFO", "BusKill was stopped via a KeyboardInterrupt")
        print("\n BusKill Stopped")

def Save_Configuration(Device, Trigger):
    if os.path.exists("config.txt") == True:
        print("CONFIG ALREADY EXISTS.")
        print("PLEASE USE -CC TO CLEAR THE CONFIG")
        Write_Log("WARNING", "Attempted config save. However, already existed")
    else:
        with open("config.txt", "a") as config:
            config.write("THIS FILE CAN BE MODIFIED MANUALLY. IF IT FAILS VALIDATION PLEASE USE - \n")
            config.write("Device:" + Device + "\n")
            config.write("Trigger:" + Trigger + "\n")
        Write_Log("INFO", "Config saved.")


def Get_Dev_From_Conf():
    with open("config.txt") as conf:
        return conf.readlines()[1].split(":")[1]

def Get_Trig_From_Conf():
    with open("config.txt") as conf:
        return conf.readlines()[2].split(":")[1]

def Clear_Config():
    if os.path.exists("config.txt") == False:
        print("No Config found!! Nothing to clear")
        Write_Log("INFO", "Config Removal attempted, not found")
    else:
        os.remove("config.txt")
        if os.path.exists("config.txt"):
            print("Internal Error, Please Try again (or raise a user story on Github)")
            Write_Log("ERROR", "BusKill could not remove the config file")
        else:
            print("Config Cleared!")
            Write_Log("WARNING", "Configuration Removed")


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

def Query_Trigger():
    with open("Triggers/"+Trigger+"/TriggerInfo.txt") as InfoFile:
        DATA = InfoFile.read().splitlines()
        for line in DATA:
            print(line)

def Main(args):
    os.chdir(Find_Run_Path())
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
        if Validation(Device, Trigger):
            if Save_Conf == True:
                Save_Configuration(Device, Trigger)
            Normal_Operation(Device, Trigger)
            sys.exit()
        else:
            print("Something went wrong")
            sys.exit()

    if Query == True:
        Trigger = args[Query+1]
        with open("/Triggers/"+Trigger+"/TriggerInfo.txt") as InfoFile:
            print(InfoFile.readline())
        sys.exit()

    if Config == True:
        Device = Get_Dev_From_Conf().strip()
        Trigger = Get_Trig_From_Conf().strip()
        if Validation(Device, Trigger):
            Normal_Operation(Device, Trigger)
            sys.exit()
        else:
            print("Invalid Device or Trigger")
            sys.exit()

    if Clear_Conf == True:
        Clear_Config()
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
