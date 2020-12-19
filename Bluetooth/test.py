import BluetoothAPI

for device in BluetoothAPI.GetDevices():
    device.PrintAllInfo()