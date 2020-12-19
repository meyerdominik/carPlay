import os
import subprocess


def __sendcommand(command):
    return os.popen(command).read()


def getdevices():
    rtn = list()

    AllDevices = __sendcommand("echo \"devices\\nquit\" | bluetoothctl")

    print "---"
    print AllDevices
    print "---"
