import appdaemon.appapi as appapi
import datetime


#
# Lock Sync App
#
# Args:
#   lock    -- entity id of the lock
#   alarm   -- entity id of the "lock alarm"
#

class Garage(appapi.AppDaemon):
    def initialize(self):

        self.listen_state(self.notify_garage, "call_service")

        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')
        self.call_service("notify/html5", title="Garage", message="Garage initialized at " + time)

    def notify_garage(self, event_name, data, kwargs):
        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')

        self.log(data["payload"])

        # self.call_service("notify/html5", title="Lock", message=message("unlocked", new, time))

