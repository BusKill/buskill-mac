import subprocess
import fnmatch

import os
from os import path

import sys

from BusKill_Core import Vars

class Controller:

    def __init__(self):
        self.AppPath = "~/Application/BusKill/"
        self.Trigger = Vars._getTrigger()
        self.Device = Vars._getDevice()

    def _getDevices(self):
        Devices = fnmatch.filter(os.listdir('/dev/'), '*disk*')
        Usable_Devices = []
        for Device in Devices:
            if Device.startswith("disk"):
                Usable_Devices.append(Device)
        return Usable_Devices

    def _getTriggers(self):
        Directories = os.listdir("../triggers/")
        for dir in Directories:
            Trigger_Data = fnmatch.filter(os.listdir(os.path.join("../triggers/", dir)), "TrigInfo.txt")
            if Trigger_Data is not None:
                Trigger.append(dir)
        return Triggers

    def _installNewTrigger(self):
        function = None #placeholder code to be written

    def _getDefaults(self):
        function = None #placeholder code to be written

    def _checkData(self):
        function = None #placeholder code to be written

    def _validation(self):
        if self._isDevConnected(Vars._getDevice()) == True and self._checkTrigger(Vars._getTrigger()) == True:
            return True
        else:
            return False

    def _checkTrigger(self, Trigger):
        function = None # placeholder code to be written

    def _isDevConnected(self, Device):
        return os.path.exists(os.path.join("/dev", Device))

    def _printList(self, List):
        counter = 1
        for entry in List:
            print(str(counter) + " - " + entry)
            counter = counter + 1

    def _getOption(self, List, Option):
        return List[Option - 1]

    def _addNewTrigger(self):
        function = None # placeholder still needs to be coded

    def _configureApplication(self):
        while config = False:
            Triggers = self._getTriggers()
            Devices = self._getTriggers()

            print("Please Note: Triggers which have not been isntalled will not appear.")
            self._printList(self._getTriggers())
            tmp = str(input("Please select a Trigger(Please use numerical value): "))
            if tmp.lower() == "exit":
                break
            else:
                int(tmp)
                Vars._setTrigger(self._getOption(self._getTriggers(), tmp))

            self._printList(self._getDevices())
            tmp = str(input("Please select a device(Please use numerical value): "))
            if tmp.lower() == "exit":
                break
            else:
                int(tmp)
                Vars.setDevice(_getOption(self._getDevices(), tmp))

            print("""
            Trigger: {}
            Device: {}
            """).value(Vars._getTrigger(), Vars._getDevice())

            confirm = str(input("Are you happy with this configuration?(Y/N): "))
            if confirm.lower() = "y":
                Vars.writeConf()
                break

    def _operation(self):
        if self.Trigger == None and self.Device = None:
            option = str(input("No configuration found!!, Configure app now?(Y/N): "))
            if option.lower() == "y":
                self._configureApplication()
            else:
                active = True
                while active = True:
                    print("Starting Buskill in manual mode... please wait while we gather some data...")
                    Available_Devices = self._getDevices()
                    Available_Triggers = self._getTriggers()
                    time.sleep(1)

                    print("Ready to go !!...")
                    self._printList(Available_Devices)
                    tmp = str(input("Which Device would you like to use? (Please Use Numerical Value): "))
                    if tmp.lower() == "exit":
                        break
                    else:
                        Vars._setDevice(self._getOption(Available_Devices, int(tmp)))

                    self._printList(Available_Triggers)
                    tmp = str(input("Which Trigger would you like to use? (Please Use Numerical Value): "))
                    if tmp.lower() == "exit":
                        break
                    else:
                        vars._setTrigger(self._getOption(Available_Triggers, int(tmp)))

                    print("""
                    Device: {}
                    Trigger: {}
                    """).value(Vars._getTrigger(), Vars._getDevice())
                    confirm = str(input("Would you like to continue?: "))
                    if confirm.lower().contains("y"):
                        if self._isDevConnected(Vars._getDevice()) == True:
                            while self._isDevConnected(Vars._getDevice()) == True:
                                time.sleep(5)
                                if self._isDevConnected(Vars._getDevice()) == False:
                                    self._executeTrigger(Vars._getTrigger())
                                    sys.exit()
                        else:
                            print("error has occured, returning to main")
                            break
                    elif confirm.lower() == "exit":
                        break
                    else:
                        print("error has occured, returning to main")
                        break
                 
    def _executeTrigger(self, Trigger):
        subprocess.call("sudo python " + self.AppPath + Trigger)
