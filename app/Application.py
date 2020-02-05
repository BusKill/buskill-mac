#BusKIllUI Class

import sys
from sys import platform

from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QComboBox

#helper functions
def get_sys():
    if platform.lower() == "darwin":
        return " Mac"
    else:
        return " Linux"
class BusKillUI(QMainWindow):

    def __init__(self):
        super().__init__()

        Platform = get_sys()
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
        else:
            self._RunSetupUtilityButton()

    def _DropDownDriveSelection(self):
        self.DeviceDropDown = QComboBox()
        self.DeviceDropDown.addItem("--Device--")
        Devices = {} #populates options
        self.DeviceDropDown.setFixedHeight(35)
        self.generalLayout.addWidget(self.DeviceDropDown)

    def _DropDownTriggerSelection(self):
        self.TriggerDropDown = QComboBox()
        Triggers = {} #populates available triggers
        self.TriggerDropDown.setFixedHeight(35)
        self.generalLayout.addWidget(self.TriggerDropDown)
        

    def _RunSetupUtilityButton(self):
        self.SetupButton = QPushButton()
        self.SetupButton.setFixedSize(120, 40)
        self.generalLayout.addWidget(self.SetupButton)

    def _ConfigureApplicationButton(self):
        self.ApplicationButton = QPushButton()
        self.ApplicationButton.setFixedSize(120,40)
        self.generalLayout.addWidget(self.ApplicationButton)

def main():
    BusKill = QApplication(sys.argv)
    view = BusKillUI()
    view.show()
    sys.exit(BusKill.exec_())

if __name__ == '__main__':
    main()
