# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from temper import Temper
from octoprint.util import RepeatedTimer


class USBTempPlugin(octoprint.plugin.StartupPlugin):
    def __init__(self):
        self.temper = Temper()
        self.cur_temps = {}

    def on_after_startup(self):
        self._logger.info(f"Starting usb temp timer")
        self._checkTempTimer = RepeatedTimer(
            10.0, self.update_temp, run_first=True, daemon=False
        )
        self._checkTempTimer.start()

    def update_temp(self):
        new_temps = {}
        self._logger.debug(f"Update loop run")
        results = self.temper.read()
        self._logger.debug(results)
        for device in results:
            devname = f"USB{str(device['busnum']).rjust(3,'0')}:{str(device['devnum']).rjust(3,'0')}"
            new_temps[devname] = (device["internal temperature"], 0.0)
            self._logger.debug(
                f"USB {devname} temperature is {device['internal temperature']}"
            )
        self.cur_temps = new_temps

    def callback(self, comm, parsed_temps):
        parsed_temps.update(self.cur_temps)
        self._logger.debug(f"Updated parsed_temps: {parsed_temps}")
        return parsed_temps


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = USBTempPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.temperatures.received": __plugin_implementation__.callback
    }
