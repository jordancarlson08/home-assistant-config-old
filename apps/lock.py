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

        self.log("LockSync: Initialize state listeners")
        self.listen_state(self.lock, self.alarm, new=18)
        self.listen_state(self.lock, self.alarm, new=21)

        self.listen_state(self.unlock, self.alarm, new=19)
        self.listen_state(self.unlock, self.alarm, new=22)

    def lock(self, entity, attribute, old, new, kwargs):
        self.log("LockSync: Lock")
        self.call_service("lock.lock", entity_id=self.lock)

    def unlock(self, entity, attribute, old, new, kwargs):
        self.log("LockSync: Unlock")
        self.call_service("lock.unlock", entity_id=self.lock)
