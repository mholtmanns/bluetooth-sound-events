#!/usr/bin/python

import os
import sys
import signal
import logging
import logging.handlers
import dbus
import dbus.service
import dbus.mainloop.glib
import gobject

LOG_LEVEL = logging.INFO
LOG_FILE = "/dev/log"
BLUEZ_DEV = "/org/bluez/hci0/"
SCRIPT_PATH = os.path.dirname(os.path.realpath("__file__"))

def interface_change(object_path, properties, member):
    global bus

    if BLUEZ_DEV not in object_path:
        return

    CMDAction = "Connect" if member == "InterfacesAdded" else "Disconnect"
    cmd = ("%s/play-event.sh %s %s" % (SCRIPT_PATH, CMDAction, SCRIPT_PATH))
    logger.info("CMDAction - %s, cmd - %s" % (CMDAction, cmd))
    os.system(cmd)

def shutdown(signum, frame):
    mainloop.quit()

if __name__ == "__main__":
    # shut down on a TERM signal
    signal.signal(signal.SIGTERM, shutdown)

    # start logging
    logger = logging.getLogger("bt_auto_loader")
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(logging.handlers.SysLogHandler(address = LOG_FILE))
    logger.info("Starting to monitor Bluetooth/A2DP connections")

    # Get the system bus
    try:
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus = dbus.SystemBus()
    except Exception as ex:
        logger.error("Unable to get the system dbus: '{0}'. Exiting. Is dbus running?".format(ex.message))
        sys.exit(1)

    # listen for signals on the Bluez bus
    bus.add_signal_receiver(interface_change, bus_name="org.bluez", signal_name="InterfacesAdded", member_keyword="member")
    bus.add_signal_receiver(interface_change, bus_name="org.bluez", signal_name="InterfacesRemoved", member_keyword="member")

    try:
        mainloop = gobject.MainLoop()
        mainloop.run()
    except KeyboardInterrupt:
        pass
    except:
        logger.error("Unable to run the gobject main loop")
        sys.exit(1)

    logger.info("Shutting down")
    sys.exit(0)
