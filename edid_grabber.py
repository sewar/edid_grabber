import sys

from uploader import EDIDUploader


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


print 'Starting EDID Grabber\n\n'

print 'Collecting EDIDs from operating system ...'
grabber = get_grabber()
grabber.grab_EDID()
print 'EDID items found: %s\n' % (len(grabber.EDIDs))

if len(grabber.EDIDs) > 0:
    print 'Uploading EDIDs ...'
    uploader = EDIDUploader()
    uploader.upload(grabber.EDIDs)
    print 'Succeeded: %s, Failed: %s\n' % (uploader.succeeded, uploader.failed)
else:
    print 'No EDIDs to upload.\n'

print 'Aborting.'
