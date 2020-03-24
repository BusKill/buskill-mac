import os
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
    Installed_Triggers = List_Trigger()
    for trigger in Install_Trigger:
        if Trigger == trigger:
            Trig = True
    Available_Devices = List_Device()
    for device in Available_Devices:
        if Device == device:
            Dev = True

    return Dev and Trig

def Check_Device(Device):
    if os.path.exists("/dev/"+Device) == True:
        return True
    else:
        return False

def Execute_Trigger(Trigger):
    subprocess.call("sudo python /Triggers/" + Trigger + "/Trigger.py")

def Normal_Operation(Device, Trigger):
    print("BusKill is now running")
    Triggered = False
    while Triggered == False:
        if Check_Device(Device) == False:
            Execute_Trigger(Trigger)
            Triggered = True
        time.sleep(5)

def Save_Configuration(Device, Trigger):
    if os.path.exists("config.txt") == True:
        print("CONFIG ALREADY EXISTS.")
        print("PLEASE USE -CC TO CLEAR THE CONFIG")
    else:
        with open("config.txt", "a") as config:
            config.writeline("THIS FILE CAN BE MODIFIED MANUALLY. IF IT FAILS VALIDATION PLEASE USE -CC")
            config.writeline("Device: "+Device)
            config.writeline("Trigger: "+Trigger)


def Load_Configuration(index):
    with open("config.txt", "r") as config:
        list = []
        list.append(config.readline(1).split(":")[1])
        list.append(config.readline(2).split(":")[2])

    return list[index]

def Clear_Config():
    if os.path.exists("config.txt") == False:
        print("No Config found!! Nothing to clear")
    else:
        os.remove("config.txt")
        if os.path.exists("config.txt"):
            print("Internal Error, Please Try again (or raise a user story on Github)")
        else:
            print("Config Cleared!")

def List_Device():
    Devices = os.listdir("/dev/")
    Disk_Devices = []
    for Device in Devices:
        if fnmatch.fnmatch(Device, "*disk*"):
            Disk_Devices.append(Device)

    counter = 0
    for Device in Disk_Devices:
        counter = counter + 1
        print(str(counter) + " - " + Device)

#def List_Device(): #not complete
#    df = subprocess.check_output("system_profiler SPUSBDataType -xml -detailLevel mini", shell=True)
#    if sys.version_info[0] == 2:
#        df = plistlib.readPlistFromString(df)
#    else:
#        df = plistlib.loads(df)
#    List = XML_Parser(df)
#    return List

#def XML_Parser(XML):
#    function = None
#    List = []
#    return List

def List_Trigger(): # Doesn't work
    Triggers = []
    dirlist = os.listdir("../Triggers")
    for dir in dirlist:
        if os.path.isdir("../Triggers/"+dir) == True:
            Triggers.append(dir)

    counter = 0
    for Trigger in Triggers:
        counter = counter + 1
        print(str(counter) + " - " + Trigger)

def Query_Trigger():
    function = None

def Main(args):
    Device = False
    Trigger = False
    Query = False
    Config = False
    Clear_Conf = False
    help = False
    List_Trig = False
    List_Dev = False
    for index, arg in enumerate(args):
        if arg.upper() == "-T":
            Trigger = index
        elif arg.upper() == "-Q":
            Query = index
        elif arg.upper() == "-D":
            Device = index
        elif arg.upper() == "-SC":
            Save_Conf = True
        elif arg.upper() == "-C":
            Config = True
        elif arg.upper() == "-CC":
            Clear_Conf = True
        elif arg.upper() == "-H":
            help = True
        elif arg.upper() == "-LT":
            List_Trig = True
        elif arg.upper() == "-LD":
            List_Dev = True

    if Device and Trigger == True:
        Device = args[Device + 1]
        Trigger = args[Trigger + 1]
        if Validation() == True:
            if Save_Conf == True:
                Save_Configuration(Device, Trigger)
            Normal_Operation(Device, Trigger)

    if Query == True:
        Trigger = args[Query+1]
        with open("../Triggers/"+Trigger+"/TriggerInfo.txt") as InfoFile:
            print(InfoFile.readline())
        sys.exit()

    if Config == True:
        #gets data from config
        Device = Load_Configuration(0)
        Trigger = Load_Configuration(1)
        if Validation() == True:
            Normal_Operation(Device, Trigger)
        sys.exit()

    if Clear_Conf == True:
        Clear_Config()
        sys.exit()

    if List_Trig == True:
        List_Trigger()
        sys.exit()

    if List_Dev == True:
        List_Device()
        sys.exit()

    if help == True:
        print_help()
        sys.exit()

    else:
        print_help()

Main(sys.argv)
