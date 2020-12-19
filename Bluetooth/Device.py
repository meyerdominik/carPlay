class Device:
    Group = ""
    MAC = ""
    Name = ""

    def __init__(self, Group, MAC, Name):
        self.Group = Group
        self.MAC = MAC
        self.Name = Name