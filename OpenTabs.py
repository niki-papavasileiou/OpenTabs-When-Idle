import webbrowser
import time
import subprocess as sp

import ctypes
import ctypes.util

class XScreenSaverInfo(ctypes.Structure):
    _fields_ = [
            ('window', ctypes.c_ulong),
            ('state', ctypes.c_int),
            ('kind', ctypes.c_int),
            ('til_or_since', ctypes.c_ulong),
            ('idle', ctypes.c_ulong),
            ('eventMask', ctypes.c_ulong)
    ]
XScreenSaverInfo_p = ctypes.POINTER(XScreenSaverInfo)

display_p = ctypes.c_void_p
xid = ctypes.c_ulong
c_int_p = ctypes.POINTER(ctypes.c_int)

try:
    libX11path = ctypes.util.find_library('X11')
    if libX11path == None:
        raise OSError('libX11 could not be found.')
    libX11 = ctypes.cdll.LoadLibrary(libX11path)
    libX11.XOpenDisplay.restype = display_p
    libX11.XOpenDisplay.argtypes = ctypes.c_char_p,
    libX11.XDefaultRootWindow.restype = xid
    libX11.XDefaultRootWindow.argtypes = display_p,

    libXsspath = ctypes.util.find_library('Xss')
    if libXsspath == None:
        raise OSError('libXss could not be found.')
    libXss = ctypes.cdll.LoadLibrary(libXsspath)
    libXss.XScreenSaverQueryExtension.argtypes = display_p, c_int_p, c_int_p
    libXss.XScreenSaverAllocInfo.restype = XScreenSaverInfo_p
    libXss.XScreenSaverQueryInfo.argtypes = (display_p, xid, XScreenSaverInfo_p)

    dpy_p = libX11.XOpenDisplay(None)
    if dpy_p == None:
        raise OSError('Could not open X Display.')

    _event_basep = ctypes.c_int()
    _error_basep = ctypes.c_int()
    if libXss.XScreenSaverQueryExtension(dpy_p, ctypes.byref(_event_basep),
                    ctypes.byref(_error_basep)) == 0:
        raise OSError('XScreenSaver Extension not available on display.')

    xss_info_p = libXss.XScreenSaverAllocInfo()
    if xss_info_p == None:
        raise OSError('XScreenSaverAllocInfo: Out of Memory.')

    rootwindow = libX11.XDefaultRootWindow(dpy_p)
    xss_available = True
except OSError:
    # Logging?
    xss_available = False

def getIdleSec():
   # global xss_available
    """
    Return the idle time in seconds
    """
    if not xss_available:
        return 0
    if libXss.XScreenSaverQueryInfo(dpy_p, rootwindow, xss_info_p) == 0:
        return 0
    else:
        return int(xss_info_p.contents.idle) / 1000

def close():
    global xss_available
    if xss_available:
        libX11.XFree(xss_info_p)
        libX11.XCloseDisplay(dpy_p)
        xss_available = False

while 1:
    GetLastInputInfo = int(getIdleSec())
    if GetLastInputInfo == 200:
        p = sp.Popen(["chromium", "chromium://newtab"])
            #time.sleep(5)

        p1 = sp.Popen(["chromium", "chromium://newtab"])
        time.sleep(2)

            #p.kill()

        p2 = sp.Popen(["chromium", "chromium://newtab"])
        time.sleep(2) #delay of 10 seconds

        p3 = sp.Popen(["chromium", "chromium://newtab"])
        time.sleep(2)

        p4 = sp.Popen(["chromium", "chromium://newtab"])
        time.sleep(2)

        p5 = sp.Popen(["chromium", "chromium://newtab"])
        time.sleep(12)

        p1.kill()