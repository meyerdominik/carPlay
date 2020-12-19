import os
import subprocess


def __sendcommand(command):
    return subprocess.call(command, shell=True, cwd=os.path.expanduser('~'))


def getdevices():
    rtn = list()

    AllDevices = __sendcommand("echo \"devices\\nquit\" | bluetoothctl")

    print "---"
    print AllDevices
    print "---"
