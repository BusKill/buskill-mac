
class Vars:

    def __init__(self):
        self.configFile = ""
        self.Trigger = None
        self.Device = None

    def _setTrigger(self, Trigger):
        self.Trigger = Trigger

    def _getTrigger(self):
        return self.Trigger

    def _setDevice(self, Device):
        self.Device = Device

    def _getDevice(self):
        return self.Device

    def _readConf(self):
        with open(self.configFile) as Conf:
            Config = Conf.readlines()
            self._setDevice(Config[1].split(":")[1])
            self._setTrigger(Config[0].split(":")[1])

    def _checkConfig(self):
        if self.Trigger == None or self.Device == None:
            print("You must configure this application")
            return False
        else:
            return True

    def _writeConf(self):
        with open(self.configFile, "r+") as Conf:
            config = Conf.readlines()
            line_1 = config.split(":")
            line_2 = config.split(":")
            del line_1[1]
            del line_2[1]
            line_1.append(self.Device)
            line_2.append(self.Trigger)
            Conf.write(line_1.join())
            Conf.append(line_2.join())
