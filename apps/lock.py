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

        self.listen_state(self.lock, self.alarm, new="18")
        self.listen_state(self.lock, self.alarm, new="21")

        self.listen_state(self.unlock, self.alarm, new="19")
        self.listen_state(self.unlock, self.alarm, new="22")

    def lock(self):
        self.call_service("lock.lock", entity_id=self.lock)

    def unlock(self):
        self.call_service("lock.unlock", entity_id=self.lock)
