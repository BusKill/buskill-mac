import os
import time
import sys
import fnmatch
import subprocess
from pathlib import Path

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

def Validation(Device, Trigger):
    Installed_Triggers = Get_Triggers()
    for trigger in Installed_Triggers:
        if Trigger.strip() == trigger:
            Trig = True
        else:
            Trig = False

    Available_Devices = Get_Devices()
    for device in Available_Devices:
        if Device.strip() == device:
            Dev = True
        else:
            Dev = False

    return Dev and Trig

def Check_Device(Device):
    if os.path.exists("/dev/"+Device) == True:
        return True
    else:
        return False

def Execute_Trigger(Trigger):
    subprocess.call("python ../Triggers/" + Trigger + "/Trigger.py", shell = True)

def Normal_Operation(Device, Trigger):
    print("BusKill is now running")
    Triggered = False
    try:
        while Triggered == False:
            if Check_Device(Device) == False:
                Execute_Trigger(Trigger)
                Triggered = True
                time.sleep(5)
    except KeyboardInterrupt:
        print("\n BusKill Stopped")

def Save_Configuration(Device, Trigger):
    if os.path.exists("config.txt") == True:
        print("CONFIG ALREADY EXISTS.")
        print("PLEASE USE -CC TO CLEAR THE CONFIG")
    else:
        with open("config.txt", "a") as config:
            config.write("THIS FILE CAN BE MODIFIED MANUALLY. IF IT FAILS VALIDATION PLEASE USE - \n")
            config.write("Device:" + Device + "\n")
            config.write("Trigger:" + Trigger + "\n")


def Get_Dev_From_Conf():
    with open("config.txt") as conf:
        return conf.readlines()[1].split(":")[1]

def Get_Trig_From_Conf():
    with open("config.txt") as conf:
        return conf.readlines()[2].split(":")[1]

def Clear_Config():
    if os.path.exists("config.txt") == False:
        print("No Config found!! Nothing to clear")
    else:
        os.remove("config.txt")
        if os.path.exists("config.txt"):
            print("Internal Error, Please Try again (or raise a user story on Github)")
        else:
            print("Config Cleared!")

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
    dirlist = os.listdir("../Triggers")
    for dir in dirlist:
        if os.path.isdir("../Triggers/"+dir) == True:
            Triggers.append(dir)
    return Triggers

def List_Triggers():
    Triggers = Get_Triggers()
    counter = 0
    for Trigger in Triggers:
        counter = counter + 1
        print(str(counter) + " - " + Trigger)

def Query_Trigger():
    function = None

def Main(args):
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
        with open("../Triggers/"+Trigger+"/TriggerInfo.txt") as InfoFile:
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
