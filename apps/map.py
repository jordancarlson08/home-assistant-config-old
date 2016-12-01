import appdaemon.appapi as appapi
import datetime


#
# Map Command App
#
# Bold attempt to map any command from google home to home assistant service
#
# Args:
#   time_on     -- ex. 10:30:30 == 10:30am and 30 seconds
#   time_off    --
#   switch      -- the entity id of the switch or light
#

class MapCommand(appapi.AppDaemon):
    def initialize(self):
        self.log("initialize")
        self.listen_event(self.log_details, "script.vol_up")

    def log_details(self, arg):
        self.log("Inside log details")
        self.log(arg)
