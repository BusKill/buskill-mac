#BusKIllUI Class
import os
import sys

from sys import platform

from functools import partial
import fnmatch

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QComboBox

class BusKillUI(QMainWindow):

    def __init__(self):
        super().__init__()

        Platform = BusKillCtrl.get_sys()
        self.setWindowTitle("BusKill " + Platform)

        #layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        #widget
        self._DropDownDriveSelection()
        self._DropDownTriggerSelection()

        if Platform == " Mac":
            self._ConfigureApplicationButton()
        elif Platform == "": #whatever Unix Os's Return
            self._RunSetupUtilityButton()
        else:
            print("an error has occured") # create a popup for errors to be universally utilised
    def _DropDownDriveSelection(self):
        self.DeviceDropDown = QComboBox()
        self.DeviceDropDown.addItem("--Device--")
        Devices = [] #populates options
        #for Device in Devices:
        #    self.DeviceDropDown.addItem(Device)
        self.DeviceDropDown.setFixedHeight(35)
        self.generalLayout.addWidget(self.DeviceDropDown)

    def _DropDownTriggerSelection(self):
        self.TriggerDropDown = QComboBox()
        self.TriggerDropDown.addItem("--Trigger--")
        Triggers = BusKillCtrl.Get_Triggers() #populates available triggers
        for trigger in Triggers:
            raw = trigger.split(".")
            trigger_name = raw[0]
            self.TriggerDropDown.addItem(trigger.split(".")[0])
        self.TriggerDropDown.setFixedHeight(35)
        self.generalLayout.addWidget(self.TriggerDropDown)


    def _RunSetupUtilityButton(self):
        self.SetupButton = QPushButton("Run Setup")
        self.SetupButton.setFixedSize(120, 40)
        self.generalLayout.addWidget(self.SetupButton)

    def _ConfigureApplicationButton(self):
        self.ApplicationButton = QPushButton("Run Agent")
        self.ApplicationButton.setFixedSize(200,40)
        self.generalLayout.addWidget(self.ApplicationButton)

class BusKillCtrl:

    def __init__(self, view):
        self._view = view
        self._connectSignals()

    def Get_Triggers():
        Triggers = fnmatch.filter(os.listdir('../triggers/'), '*.py')
        return Triggers

    def Get_Devices():
        Devices = ["1","2"]
        return Devices

    def get_sys():
        if platform.lower() == "darwin":
            return " Mac"
        else:
            return " Linux"

    #def execute_trigger(): # MacOSX Only!!!!

    #def Run_Setup(): # Linux Only

def main():
    BusKill = QApplication(sys.argv)
    view = BusKillUI()
    view.show()
    sys.exit(BusKill.exec_())

if __name__ == '__main__':
    main()
