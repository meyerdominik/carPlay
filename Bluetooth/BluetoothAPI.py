import os
import subprocess


def __sendcommand(command):
    return subprocess.call(command, stdout=subprocess.PIPE)


def getdevices():
    rtn = list()

    AllDevices = __sendcommand("echo \"devices\\nquit\" | bluetoothctl")

    print "---"
    print AllDevices
    print "---"
