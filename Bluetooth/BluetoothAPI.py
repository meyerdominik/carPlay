import os


def __SendCommand(command):
    return os.system(command)

def GetDevices():
    rtn = list()

    AllDevices = __SendCommand("echo \"devices\\nquit\" | bluetoothctl")

    print "---"
    print AllDevices
    print "---"