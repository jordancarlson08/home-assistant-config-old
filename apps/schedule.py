import appdaemon.appapi as appapi
import datetime


#
# Simple Schedule App
#
# Args:
#   time_on     -- ex. 10:30:30 == 10:30am and 30 seconds
#   time_off    --
#   switch      -- the entity id of the switch or light
#

class SimpleSchedule(appapi.AppDaemon):
    def initialize(self):
        self.switch = self.args["switch"]

        # Get time string
        time_on = self.args["time_on"]
        # Convert string to datetime time
        self.time_on = datetime.datetime.strptime(time_on, "%H:%M:%S").time()

        time_off = self.args["time_off"]
        self.time_off = datetime.datetime.strptime(time_off, "%H:%M:%S").time()

        self.run_daily(self.turn_on_cb, self.time_on)
        self.run_daily(self.turn_off_cb, self.time_off)

    def turn_on_cb(self, arg):
        self.turn_on(self.switch)

    def turn_off_cb(self, arg):
        self.turn_off(self.switch)


#
# Auto Off App
#   Turn off a device during when it falls between two given times.
#
# Args:
#   start       -- ex. 10:30:30 == 10:30am and 30 seconds
#   end         --
#   switch      -- the entity id of the switch or light
#


class AutoOff(appapi.AppDaemon):
    def initialize(self):
        self.switch = self.args["switch"]
        self.start = self.args["start"]
        self.end = self.args["end"]

        time = datetime.time(0, 5, 0)
        self.run_hourly(self.turn_off_cb, time)

    def turn_off_cb(self, arg):
        now = datetime.datetime.now().time()
        start = datetime.datetime.strptime(self.start, "%H:%M:%S").time()
        end = datetime.datetime.strptime(self.end, "%H:%M:%S").time()

        if start < now < end:
            self.turn_off(self.switch)
