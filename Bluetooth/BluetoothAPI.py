import os


# noinspection PyPep8Naming
class Device(object):
    MAC = ""
    Name = ""
    Alias = ""
    Icon = ""
    Paired = False
    Trusted = False
    Blocked = False
    Connected = False
    LegacyPairing = False

    def PrintAllInfo(self):
        print("Name: " + self.Name)
        print("MAC: " + self.MAC)
        print("Alias: " + self.Alias)
        print("Icon: " + self.Icon)
        if self.Paired:
            print("Paired: True")
        else:
            print("Paired: False")
        if self.Trusted:
            print("Trusted: True")
        else:
            print("Trusted: False")
        if self.Blocked:
            print("Blocked: True")
        else:
            print("Blocked: False")
        if self.Connected:
            print("Connected: True")
        else:
            print("Connected: False")
        if self.LegacyPairing:
            print("LegacyPairing: True")
        else:
            print("LegacyPairing: False")

    def GetMoreDeviceInfo(self):
        lines = SendCommand("echo \"info " + self.MAC + "\\nquit\" | bluetoothctl").splitlines()
        for line in lines:
            split = line.split(": ")
            splitWithoutSpacers = split[0].replace(" ", "").replace("\t", "")
            print splitWithoutSpacers
            if splitWithoutSpacers.startswith("Alias"):
                self.Alias = split[1]
            elif splitWithoutSpacers.startswith("Icon"):
                self.Icon = split[1]
            elif splitWithoutSpacers.startswith("Paired"):
                if split[1] == "yes":
                    self.Paired = True
            elif splitWithoutSpacers.startswith("Trusted"):
                if split[1] == "yes":
                    self.Trusted = True
            elif splitWithoutSpacers.startswith("Blocked"):
                if split[1] == "yes":
                    self.Blocked = True
            elif splitWithoutSpacers.startswith("Connected"):
                if split[1] == "yes":
                    self.Connected = True
            elif splitWithoutSpacers.startswith("LegacyPairing"):
                if split[1] == "yes":
                    self.LegacyPairing = True

    def __init__(self, MAC, Name):
        self.MAC = MAC
        self.Name = Name
        self.GetMoreDeviceInfo()


def SendCommand(command):
    return os.popen(command).read()

def GetDevices():
    rtn = []

    # get all bluetooth device lines
    lines = SendCommand("echo \"devices\\nquit\" | bluetoothctl").splitlines()
    for line in lines:
        if line.startswith("Device"):
            MAC = line.split(' ')[1]
            Name = line.split(str(MAC) + str(" "))[1]

            if MAC and Name:
                rtn.append(Device(MAC, Name))
    return rtn

