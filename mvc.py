#Define Model: The component that stores data
class Devices:

    ipAddress = ""
    port = ""

    @staticmethod
    def findDevices():
        devices = []

        d = Devices()
        d.ipAddress = "192.168.1.1"
        d.port = "2001"

        devices.append(d)

        d.ipAddress = "192.168.1.50"
        d.port = "7091"

        devices.append(d)

        d.ipAddress = "192.168.1.100"
        d.port = "80"

        devices.append(d)

        return devices

#Define View: The component that displays data

class DevicesView:
    def showDevices(self,devices):
        for d in devices:
            print("________")
            print("IP Address:  " + d.ipAddress)
            print("Port: " + str(d.port))
            print("________")

#Define Controller: handles logic flow, user interactions, and direct models and view.

class DevicesController:
    def __init__(self):
        devices = Devices.findDevices()

        v = DevicesView()

        v.showDevices(devices)

c= DevicesController()




