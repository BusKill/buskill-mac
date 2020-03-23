import sys

def Normal_Operation(Device, Trigger):
    function = None

def Save_Configuration(Device, Trigger):
    function = None

def Load_Configuration():
    list = []
    list.append(Device)
    list.append(Trigger)
    return list

def Clear_Config():
    function = None

def List_Device():
    function = None

def List_Trigger():
    function = None

def Query_Trigger():
    function = None

def Install_Trigger():
    function = None

if sys.argv[1].upper().contains("L"):
    QueryManager(sys.argv[1])

for index, arg in enumerate(sys.argv):
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

if Device and Trigger != None:
    Device = sys.argv[Device + 1]
    Trigger = sys.argv[Trigger + 1]
    #Validation
    if Save_Conf == True:
        Save_Configuration(Device, Trigger)
    Normal_Operation(Device, Trigger)

if Query != None:
    #find Trigger Description
    function = None

if Install == True:
    #search and install trigger
    function = None

if Config = True:
    #gets data from config
    Device = None # will equal something
    Trigger = None # will equal something
    #Validation
    Normal_Operation(Device, Trigger)

if Clear_Config == True:
    #Delete Config File
    function = None
'''
options
    triggers
        -T (needed for normal operation(Defines Trigger to be used)) -in app(still not coded)
        -Q (Queries Trigger immediatly after (if empty is an error)) -in app(still not coded)
        -LT (Lists available/Installed Triggers) -in app(still not coded)
        -I (Installs a new Trigger)-in app(still not coded)
    Devices
        -D (needed for normal operation(Defines Device to be used)) -in app(still not coded)
        -LD (Lists available devices on the system) -in app(still not coded)
    Configuration
        -SC (Creates a configuration file) -in app(still not coded)
        -CC (Deletes Config File) -in app(still not coded)
        -C (Reads a configuration file) -in app(still not coded)
'''
