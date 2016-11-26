import appdaemon.appapi as appapi


#
# Lock Sync App
#
# Args:
#   lock
#   alarm
#

class LockSync(appapi.AppDaemon):
    def initialize(self):

        self.lock = self.args["lock"]
        self.alarm = self.args["alarm"]

        self.listen_state(self.sync_lock, self.alarm)

    def sync_lock(self, entity, attribute, old, new, kwargs):
        self.log("LockSync: Unlock")
        self.log("old:" + old)
        self.log("new:" + new)
        if new == 18 or new == 21:
            self.call_service("lock/lock", entity_id=self.lock)
        if new == 19 or new == 22:
            self.call_service("lock/unlock", entity_id=self.lock)
