import PyQt5.QtWidgets as Qt
from PyQt5 import *
import sys

from BusKill_Core import Controller, Configuration, Runtime

class MainWindow(Qt.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("BusKill Mac")
        self.setFixedSize(500,200)
        self.APP_CTRL = Controller()
        self.APP_CONF = Configuration()
        self.Triggers = self.APP_CTRL._getTriggers()
        self.Devices = self.APP_CTRL._getDevices()
        self.Configs = self.APP_CTRL._getConfig()

        #Tabs
        self.Tabs = Qt.QTabWidget(self)
        self.Tabs.setFixedSize(500,200)
        self.setCentralWidget(self.Tabs)
        self.MainTab = Qt.QWidget(self)

        self.MainTab.layout = Qt.QGridLayout()
        self.MainTab.setLayout(self.MainTab.layout)

        #Left Pane Code
        self.RunWithOptionLabel = Qt.QLabel("Run with Options")
        self.RunWithOptionLabel.setFixedSize(175, 30)
        self.MainTab.layout.addWidget(self.RunWithOptionLabel, 0, 0)

        self.MainTriggerMenu = Qt.QComboBox(self)
        self.MainTriggerMenu.setFixedSize(175, 30)
        if len(self.Triggers) != 0:
            self.MainTriggerMenu.addItem("--Triggers--")
            for entry in self.Triggers:
                self.MainTriggerMenu.addItem(entry)
        else:
            self.MainTriggerMenu.addItem("No Triggers Found!")
            self.APP_CTRL._errorHandling("Critical", "No Triggers Found!")
        self.MainTab.layout.addWidget(self.MainTriggerMenu, 1, 0)

        self.MainDeviceMenu = Qt.QComboBox(self)
        self.MainDeviceMenu.setFixedSize(175, 30)
        if len(self.Devices) != 0:
            self.MainDeviceMenu.addItem("--Devices--")
            self.MainDeviceMenu.addItems(self.Devices)
        else:
            self.MainDeviceMenu.addItem("No Devices Found!")
            self.APP_CTRL._errorHandling("Critical", "No Devices Found!")
        self.MainTab.layout.addWidget(self.MainDeviceMenu, 2, 0)

        if len(self.Devices) != 0 and len(self.Triggers) != 0:
            self.RunWithOption = Qt.QPushButton("Go!")
            self.RunWithOption.setFixedSize(179, 30)
            self.RunWithOption.clicked.connect(self._runBusKill)
            self.MainTab.layout.addWidget(self.RunWithOption, 3, 0)

        #Right Pane Code
        self.RunWithConfigLabel = Qt.QLabel("Run With Config")
        self.RunWithConfigLabel.setFixedSize(175, 30)
        self.MainTab.layout.addWidget(self.RunWithConfigLabel, 0, 2)

        self.MainConfigMenu = Qt.QComboBox(self)
        self.MainConfigMenu.setFixedSize(175, 30)
        if len(self.Configs) != 0:
            self.MainConfigMenu.addItem("--config--")
            for entry in self.Configs:
                self.MainConfigMenu.addItem(entry)
        else:
            self.MainConfigMenu.addItem("No Config Found!")
        self.MainTab.layout.addWidget(self.MainConfigMenu, 1, 2)

        if len(self.Configs) != 0:
            self.RunWithConfig = Qt.QPushButton("Go!")
            self.RunWithConfig.setFixedSize(179, 30)
            #self.RunWithConfig.clicked.connect(APP_CTRL._runConf)
            self.MainTab.layout.addWidget(self.RunWithConfig, 3, 2)

        self.Tabs.addTab(self.MainTab, "Main")

        self.ConfigTab = Qt.QWidget(self)
        self.ConfigTab.layout = Qt.QGridLayout(self)
        self.ConfigTab.setLayout(self.ConfigTab.layout)

        self.ConfigureBusKillLabel = Qt.QLabel("Configure BusKill")
        self.ConfigureBusKillLabel.setFixedSize(175, 30)
        self.ConfigTab.layout.addWidget(self.ConfigureBusKillLabel, 0, 0)

        self.ConfigTriggerMenu = Qt.QComboBox(self)
        self.ConfigTriggerMenu.setFixedSize(175,30)
        if len(self.Triggers) != 0:
            self.ConfigTriggerMenu.addItem("--Trigger--")
            for entry in self.Triggers:
                self.ConfigTriggerMenu.addItem(entry)
        else:
            self.ConfigTriggerMenu.addItem("No Triggers Found!")
        self.ConfigTab.layout.addWidget(self.ConfigTriggerMenu, 1, 0)

        self.ConfigDeviceMenu = Qt.QComboBox(self)
        self.ConfigDeviceMenu.setFixedSize(175,30)
        if len(self.Devices) != 0:
            self.ConfigDeviceMenu.addItem("--Device--")
            for entry in self.Devices:
                self.ConfigDeviceMenu.addItem(entry)
        else:
            self.ConfigDeviceMenu.addItem("No Devices Found!")
        self.ConfigTab.layout.addWidget(self.ConfigDeviceMenu, 2, 0)

        self.ConfigSaveAs = Qt.QLineEdit(self)
        self.ConfigSaveAs.setFixedSize(175, 20)
        self.ConfigSaveAs.placeholderText()
        self.ConfigTab.layout.addWidget(self.ConfigSaveAs, 3, 0)

        self.SaveConfig = Qt.QPushButton("Save Configuration")
        self.SaveConfig.setFixedSize(175, 30)
        #self.SaveConfig.clicked.connect()
        self.ConfigTab.layout.addWidget(self.SaveConfig, 4, 0)

        self.Tabs.addTab(self.ConfigTab, "Config")

        self.AdvancedTab = Qt.QWidget(self)
        self.AdvancedTab.layout = Qt.QGridLayout(self)
        self.AdvancedTab.setLayout(self.AdvancedTab.layout)

        #Left Pane
        self.AdvancedLogLabel = Qt.QLabel("Logging")
        self.AdvancedLogLabel.setFixedSize(175, 20)
        self.AdvancedTab.layout.addWidget(self.AdvancedLogLabel, 0, 0)

        self.ExportFileLocation = Qt.QGridLayout(self)
        self.ExportFileLocationLineEdit = Qt.QLineEdit(self)
        self.ExportFileLocation.addWidget(self.ExportFileLocationLineEdit, 0, 0, 1, 7)
        self.ExportFileLocationButton = Qt.QPushButton()
        #self.ExportFileLocationButton.clicked.connect()
        self.ExportFileLocation.addWidget(self.ExportFileLocationButton, 0, 8)

        self.AdvancedTab.layout.addLayout(self.ExportFileLocation, 1, 0)

        self.AdvancedLogExport = Qt.QPushButton("Export Log File")
        #self.AdvancedLogExport.clicked.connect()
        self.AdvancedTab.layout.addWidget(self.AdvancedLogExport, 2, 0)

        #Right Pane
        self.AdvancedTriggerLabel = Qt.QLabel("Triggers")
        self.AdvancedTab.layout.addWidget(self.AdvancedTriggerLabel, 0, 1)

        self.InstallTrigger = Qt.QGridLayout(self)
        self.InstallTriggerLineEdit = Qt.QLineEdit(self)
        self.InstallTrigger.addWidget(self.InstallTriggerLineEdit, 0, 0, 1, 7)
        self.InstallTriggerLocation = Qt.QPushButton()
        self.InstallTrigger.addWidget(self.InstallTriggerLocation, 0, 8)
        #self.InstallTriggerLocation.clicked.connect()
        self.AdvancedTab.layout.addLayout(self.InstallTrigger, 1, 1)

        self.InstallTriggerButton = Qt.QPushButton("Install Trigger")
        self.AdvancedTab.layout.addWidget(self.InstallTriggerButton, 2, 1)

        self.Tabs.addTab(self.AdvancedTab, "Advanced")

    def _runBusKill(self):
        self.Trigger = self.MainTriggerMenu.currentText()
        self.Device = self.MainDeviceMenu.currentText()
        if self.APP_CTRL._validation(self.Trigger, self.Device) == True:
            self.close()
            self.runpage = BusKill_Run(self.Trigger, self.Device)
            self.runpage.show()
        else:
            APP_CTRL._errorHandling("Critical", "Validation has failed")
            return

    def _runBusKillWithConf(self):
        Vars = Configuration._getConf(self.MainConfigMenu.currentText())
        if self.APP_CTRL._validation(Vars[0], Vars[1]) == True:
            self.close()
            self.runpage = BusKill_Run(Vars[0], Vars[1])
            self.runpage.show()
        else:
            APP_CTRL._errorHandling("Critical", "Validation has failed")
            return

class BusKill_Run(Qt.QMainWindow):

    def __init__(self, Trigger, Device):

        super().__init__()
        self.APP_CTRL = Controller()

        self.setWindowTitle("BusKill Mac - running")
        self.setFixedSize(500, 200)

        wid = Qt.QWidget(self)
        self.setCentralWidget(wid)
        self.Layout = Qt.QGridLayout(self)
        wid.setLayout(self.Layout)

        self.IsRunningLabel = Qt.QLabel("BusKill is running")
        self.IsRunningLabel.setFixedSize(175, 30)
        self.Layout.addWidget(self.IsRunningLabel, 0, 0)

        self.TriggerLabel1 = Qt.QLabel("Trigger:")
        self.TriggerLabel1.setFixedSize(175, 30)
        self.Layout.addWidget(self.TriggerLabel1, 1, 0)

        self.TriggerLabel2 = Qt.QLabel(Trigger)
        self.TriggerLabel2.setFixedSize(175, 30)
        self.Layout.addWidget(self.TriggerLabel2, 1, 1)

        self.DeviceLabel1 = Qt.QLabel("Device:")
        self.DeviceLabel1.setFixedSize(175, 30)
        self.Layout.addWidget(self.DeviceLabel1, 2, 0)

        self.DeviceLabel2 = Qt.QLabel(Device)
        self.DeviceLabel2.setFixedSize(175, 30)
        self.Layout.addWidget(self.DeviceLabel2, 2, 1)

        self.CloseButton = Qt.QPushButton("Stop BusKill")
        self.CloseButton.setFixedSize(175, 30)
        self.Layout.addWidget(self.CloseButton, 3, 1)

        self.show()
        self.run = Runtime(Trigger, Device)
        self.run.start()

    def _backToMain():
        self.close()
        self.Main = MainWindow()
        self.Main.show()

def main():
    app = Qt.QApplication(sys.argv)
    UI = MainWindow()
    UI.show()
    app.exec_()

main()
