import appdaemon.appapi as appapi


#
# Lock Sync App
#
# Args:
#

class LockSync(appapi.AppDaemon):
    def initialize(self):
    #     self.switch = self.args["switch"]
    #
    #     # Get time string
    #     time_on = self.args["time_on"]
    #     # Convert string to datetime time
    #     self.time_on = datetime.datetime.strptime(time_on, "%H:%M:%S").time()
    #
    #     time_off = self.args["time_off"]
    #     self.time_off = datetime.datetime.strptime(time_off, "%H:%M:%S").time()
    #
    #     self.run_daily(self.turn_on_cb, self.time_on)
    #     self.run_daily(self.turn_off_cb, self.time_off)
    #
    # def turn_on_cb(self, arg):
    #     self.turn_on(self.switch)
    #
    # def turn_off_cb(self, arg):
    #     self.turn_off(self.switch)
