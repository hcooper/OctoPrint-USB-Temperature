# OctoPrint-Usbtemp

An OctoPrint plugin which fetches temperature from USB thermometers using temper-py library.

## Setup
You may find that the default permissions do not allow octoprint to access the device.

These permissions may be a problem:
```
pi@octoprint:~ $ ls -lah /dev/hidraw*
crw------- 1 root root 244, 0 Dec  6 12:01 /dev/hidraw0
crw------- 1 root root 244, 1 Dec  6 12:01 /dev/hidraw1
```

A solution is to configure udev to create these devices with read+write access to the `plugdev` group.

Place the `99-hidraw.rules` into the directory `/etc/udev/rules.d/`.
Reload the udev configs `udevadm control --reload-rules && udevadm trigger`.

```
pi@octoprint:~ $ ls -lah /dev/hidraw*
crw-rw-r-- 1 root plugdev 244, 0 Dec  6 12:03 /dev/hidraw0
crw-rw-r-- 1 root plugdev 244, 1 Dec  6 12:03 /dev/hidraw1
```