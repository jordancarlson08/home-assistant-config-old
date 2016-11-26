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
        # lock = lock.back_door_locked_15_0
        # alarm = sensor.back_door_alarm_type_15_0
        self.lock = self.args["lock"]
        self.alarm = self.args["alarm"]

        self.log("LockSync: Initialize state listeners")
        # self.listen_state(self.lock, self.alarm, new='18')
        # self.listen_state(self.lock, self.alarm, new='21')
        #
        # self.listen_state(self.unlock, self.alarm, new='19')
        # self.listen_state(self.unlock, self.alarm, new='22')

        # self.listen_state(self.lock, "sensor.back_door_alarm_type_15_0")
        # self.listen_state(self.lock, self.alarm)

        self.listen_state(self.unlock, self.alarm)
        # self.listen_state(self.unlock, self.alarm)

    def lock(self, entity, attribute, old, new, kwargs):
        self.log("LockSync: Lock")
        self.log(old)
        self.log(new)
        # self.call_service("lock/lock", entity_id="lock.back_door_locked_15_0")

    def unlock(self, entity, attribute, old, new, kwargs):
        self.log("LockSync: Unlock")
        self.log(old)
        self.log(new)
        self.call_service("lock/unlock", entity_id=self.lock)
