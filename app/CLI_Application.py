import time
from BusKill_Core import Controller, Vars, Trigger_Installer

class BusKill_Application:
    def __init__(self):
        pass

    def _printStartup(self):
        print("welcome to busKill CLI")
        print("""
        By continuing you have agreed you have read the README.md file attached to the repostiory,

        we will not be responsible for any data loss.
        """)
        time.sleep(1)

    def configure_application():
        Controller._configureApplication()
        main()

    def Operation():
        Controller._operation()
        main()

    def add_new_trigger():
        Controller._addNewTrigger()
        main()

def main():
    run = True
    while run = True
    self._printStartup()

    print("Checking Config...")
    time.sleep(1)
if '__name__' == '__main__':
    main()

def Trigger_Finder():
    TriggersFound = []
    rootdir = '\\'
    for dirpath, files in os.walk(rootdir):
        for file in files:
            if 'BusKill' in dirpath:
                dirs.remove('BusKill')
            temp_var = fnmatch.filter(file, "TrigInfo.txt")
            if temp_var is not None:
                TriggersFound.append(dirpath)

def Add_New_Trigger():
    print("Searching for Triggers... Please wait ")
    existing_Triggers = _getTriggers()
    new_Trigger = Trigger_Finder()


def main():
    time.sleep(1)
    print("Please Wait while we gather some information...")
    menu = """
    1 - Initialise Buskill
    2 - Add a new Trigger
    """
    done = None
    while done is None:
        print(menu)
        option = int(input("Please Choose an Option (using Numbers): "))
        if option == 1:
            Operation()
        elif option == 2:
            Add_New_Trigger()

if __name__ == '__main__':
    main()
