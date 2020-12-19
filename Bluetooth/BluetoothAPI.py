import os
import Device


def __sendcommand(command):
    return os.popen(command).read()


def getdevices():
    rtn = list()

    # get all bluetooth device lines
    lines = __sendcommand("echo \"devices\\nquit\" | bluetoothctl").splitlines()
    for line in lines:
        if line.startswith("Device"):
            MAC = ""
            Name = ""
            split = line.split(' ')

            MAC = split[1]
            Name = line.split(str(MAC) + str(" "))[1]

            print MAC
            print Name
            #list.__add__(Device(Group, MAC, Name))


    return rtn

