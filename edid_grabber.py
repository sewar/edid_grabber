import sys

from uploader import EDID_Uploader

def get_grabber():
    if sys.platform.startswith('win'):
        from grabbers.windows import WindowsGrabber
        return WindowsGrabber()
    elif sys.platform.startswith('linux'):
        return None
        #from grabbers.linux import LinuxGrabber
        #return LinuxGrabber()
    elif sys.platform.startswith('darwin'):
        return None
        #from grabbers.macosx import MacOSXGrabber
        #return MacOSXGrabber()
    else:
        return None

mygrabber = get_grabber()
mygrabber.grab_EDID()

#myuploader = EDID_Uploader()
#myuploader.upload_list(mygrabber.EDIDs)
