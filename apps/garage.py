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

        self.listen_state(self.notify_garage, "cover.garage_door")

        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')
        self.call_service("notify/html5", title="Garage", message="Garage initialized at " + time)

    def notify_garage(self, entity, attribute, old, new, kwargs):
        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')

        self.call_service("notify/html5", title="Garage", message=new + " at " + time)

