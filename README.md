# OctoPrint-Usbtemp

An OctoPrint plugin which fetches temperature from USB thermometers using the [temper-py library](https://github.com/ccwienk/temper).

Whilst fetching the data works, what to do with it afterwards is still a work in progress. If you install [PlotyTempGraph](https://github.com/jneilliii/OctoPrint-PlotlyTempGraph) the usb temperatures should automatically appear in the web UI.


## Setup
Installation is via the regular OctoPrint plugin manager.

### Permissions
You may find that the default permissions do not allow octoprint to access the usb device as required.

These permissions may be a problem:

```
pi@octoprint:~ $ ls -lah /dev/hidraw*
crw------- 1 root root 244, 0 Dec  6 12:01 /dev/hidraw0
crw------- 1 root root 244, 1 Dec  6 12:01 /dev/hidraw1
```

A solution is to configure udev to give the `plugdev` group read+write access when the devices are created.

1. Place the `99-hidraw.rules` file into the directory `/etc/udev/rules.d/`.
2. Reload the udev configs `udevadm control --reload-rules && udevadm trigger`.

The permissions should now look like this:

```
pi@octoprint:~ $ ls -lah /dev/hidraw*
crw-rw-r-- 1 root plugdev 244, 0 Dec  6 12:03 /dev/hidraw0
crw-rw-r-- 1 root plugdev 244, 1 Dec  6 12:03 /dev/hidraw1
```

### Debugging

Turn up the log level for the plugin via the logging section on the settings menu. This will dumb verbose information about the devices & data the plugin is fetching.