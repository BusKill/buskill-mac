import sys

def print_help():
    print(
    """
    TEXT WILL GO HERE
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
    function = None

def Execute_Trigger(Trigger):
    function = None

def Normal_Operation(Device, Trigger):
    print("BusKill is now running")
    Triggered = False
    while Triggered = False:
        if Check_Device(Device) == False:
            Execute_Trigger(Trigger)
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


def Load_Configuration():
    list = []
    list.append(Device)
    list.append(Trigger)
    return list

def Clear_Config():
    function = None

def List_Device(): #not complete
    df = subprocess.check_output("system_profiler SPUSBDataType -xml -detailLevel mini", shell=True)
    if sys.version_info[0] == 2:
        df = plistlib.readPlistFromString(df)
    else:
        df = plistlib.loads(df)
    List = XML_Parser(df)
    return List

def XML_Parser(XML):
    function = None
    List = []
    return List

def List_Trigger():
    Directories = os.listdir("../triggers/")
    for dir in Directories:
        Trigger_Data = fnmatch.filter(os.listdir(os.path.join("../triggers/", dir)), "TrigInfo.txt")
        if Trigger_Data is not None:
            Trigger.append(dir)
    return Directories

def Query_Trigger():
    function = None

def Install_Trigger():
    function = None

def Main()(args):
    for index, arg in enumerate(args):
        if arg.upper() == "-T":
            Trigger = index
        elif arg.upper() == "-Q":
            Query = index
        elif arg.upper() == "-I"
            Install = True
        elif arg.upper() == "-D":
            Device = index
        elif arg.upper() == "-SC":
            Save_Conf = True
        elif arg.upper() == "-C"
            Config = True
        elif arg.upper() == "-CC":
            Clear_Config = True
        elif arg.upper() == "-H":
            help = True
        elif arg.upper() == "-LT":
            List_Trigger = True

    if Device and Trigger != None:
        Device = args[Device + 1]
        Trigger = args[Trigger + 1]
        if Validation() == True:
            if Save_Conf == True:
                Save_Configuration(Device, Trigger)
            Normal_Operation(Device, Trigger)

    if Query != None:
        Trigger = args[Query+1]
        with open("/Triggers/"+Trigger+"TriggerInfo.txt") as InfoFile:
            print(InfoFile.readline())

    if Install == True:
        #search and install trigger
        function = None

    if Config = True:
        #gets data from config
        Device = None # will equal something
        Trigger = None # will equal something
        if Validation() == True:
            Normal_Operation(Device, Trigger)

    if Clear_Config == True:
        #Delete Config File
        function = None

    if List_Trigger = True:
        for child in os.listdir("triggers/")
            print(child)

    if help == True:
        print_help()

    else:
        print_help()


Main(sys.argv)
'''
options
    triggers
        -T (needed for normal operation(Defines Trigger to be used)) untested
        -Q (Queries Trigger immediatly after (if empty is an error)) untested
        -LT (Lists available/Installed Triggers) untested
        -I (Installs a new Trigger)-in app(still not coded)
    Devices
        -D (needed for normal operation(Defines Device to be used)) untested
        -LD (Lists available devices on the system) -in app(still not coded)
    Configuration
        -SC (Creates a configuration file)
        -CC (Deletes Config File) -in app(still not coded)
        -C (Reads a configuration file) -in app(still not coded)
    other
        -H (Help File)
'''
