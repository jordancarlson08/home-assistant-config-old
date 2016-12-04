import appdaemon.appapi as appapi
import datetime

#
# Lock Sync App
#
# Args:
#   lock    -- entity id of the lock
#   alarm   -- entity id of the "lock alarm"
#

class LockSync(appapi.AppDaemon):
    def initialize(self):
        self.lock = self.args["lock"]
        self.alarm = self.args["alarm"]
        self.listen_state(self.sync_lock, self.alarm)

        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M %p')
        self.call_service("notify/html5", title="Lock", message="LockSync initialized at " + time)

    def sync_lock(self, entity, attribute, old, new, kwargs):
        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M %p')

        if new == "18" or new == "21":
            self.call_service("lock/lock", entity_id=self.lock)
        if new == "19" or new == "22":
            self.call_service("lock/unlock", entity_id=self.lock)
        if new == "18" or new == "21" or new == "24":
            self.call_service("notify/html5", title="Lock", message="Back door locked at " + time)
        if new == "19" or new == "22" or new == "25":
            self.call_service("notify/html5", title="Lock", message="Back door unlocked at " + time)
