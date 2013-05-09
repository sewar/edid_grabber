import _winreg

from grabbers import Grabber

class WindowsGrabber(Grabber):
    """
    Stored at "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\DISPLAY\{{monitor_name}}\{{monitor_name_id}}\Device Parameters"
    monitor_name: "%s%s" % (ID Manufacturer Name, ID Product Code)
    monitor_name_id: Unknown, can be more than one per monitor
    """

    def grab_EDID(self):
        displays_key, displays = self._get_displays()

        for display in displays:
            IDs_key, IDs = self._get_IDs(displays_key, display)

            for ID in IDs:
                parameters_key = _winreg.OpenKey(IDs_key, r"%s\%s" % (ID, r"Device Parameters"))

                try:
                    n, v, t = _winreg.EnumValue(parameters_key, 0)
                    if n == "EDID" and t == _winreg.REG_BINARY:
                        self.EDIDs.append(v)
                except WindowsError:
                    pass

                parameters_key.Close()

            IDs_key.Close()

        displays_key.Close()

    def _get_displays(self):
        displays = []
        displays_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Enum\DISPLAY")

        for i in range(1024):
            try:
                displays.append(_winreg.EnumKey(displays_key, i))
            except WindowsError:
                break

        return displays_key, displays

    def _get_IDs(self, displays_key, display):
        IDs = []
        IDs_key = _winreg.OpenKey(displays_key, display)

        for i in range(1024):
            try:
                IDs.append(_winreg.EnumKey(IDs_key, i))
            except WindowsError:
                break

        return IDs_key, IDs
