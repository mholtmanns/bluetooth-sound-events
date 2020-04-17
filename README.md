# bluetooth-sound-events
Add new functionalities:
- Sound on boot (when A2DP sink into Pulseaudio is ready)
- Sound on connect or disconnect events (when new A2DP interface is added or removed)

Code as expansion for this [tutorial][1].
Originally from [here][2] by Douglas6 written for Raspberry Pi.

Usage:
- Make clone using `git clone https://github.com/Pivek/bluetooth-sound-events` in your Raspberry Pi home dir for pi user
- Go to cloned directory and run `./install.sh`. It will create global `bluetooth-sound-events-onchange` and local `bluetooth-sound-events-onboot` services

Dependencies and assumptions:
- System `Raspbian GNU/Linux 10 (buster)`
- Bluetooth/A2DP and Pulseaudio are configured according tu mentioned tutorial
- Python 2.7 is installed with following modules: `os`, `sys`, `signal`, `logging`, `logging.handlers`, `dbus`, `dbus.service`, `dbus.mainloop.glib`, `gobject`
- You have installed `mpg123` terminal player
- Your bluetooth device is operating as `hci0` in bus object_path `/org/bluez/hci0/`

[1]:https://www.raspberrypi.org/forums/viewtopic.php?t=235519
[2]:https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=85101
