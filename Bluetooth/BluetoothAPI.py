import os
import Device


def __sendcommand(command):
    return os.popen(command).read()


def getdevices():
    rtn = list()

    # get all bluetooth device lines
    lines = __sendcommand("echo \"devices\\nquit\" | bluetoothctl").splitlines()
    bDevices = False
    for line in lines:
        print "line" + line
        if bDevices and not line.startswith("[bluetooth]"):
            Group, MAC, Name = ""
            split = line.split(' ')

            Group = split[0]
            MAC = split[1]
            Name = line.split(str(MAC) + str(" "))[1]

            print Group
            print MAC
            print Name
            #list.__add__(Device(Group, MAC, Name))

        if line.startswith("[bluetooth]"):
            if bDevices:
                print "false"
                bDevices = False
            else:
                print "true"
                bDevices = True



    return rtn

