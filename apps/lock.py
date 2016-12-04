import appdaemon.appapi as appapi
import datetime


#
# Lock Sync App
#
# Args:
#   lock    -- entity id of the lock
#   alarm   -- entity id of the "lock alarm"
#

def lock_code_to_string(string_code):
    if string_code == "18" or string_code == "19":
        method = "with the keypad"
    elif string_code == "21" or string_code == "22":
        method = "by hand"
    elif string_code == "24" or string_code == "25":
        method = "by Zwave"
    else:
        method = "by an unknown method"
    return method


def message(state, new, time):
    return "Back door " + state + " " + lock_code_to_string(new) + " at " + time


class LockSync(appapi.AppDaemon):
    def initialize(self):
        self.lock = self.args["lock"]
        self.alarm = self.args["alarm"]
        self.listen_state(self.sync_lock, self.alarm)

        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')
        self.call_service("notify/html5", title="Lock", message="LockSync initialized at " + time)

    def sync_lock(self, entity, attribute, old, new, kwargs):
        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')

        # Sync the UI with the locks
        if new == "18" or new == "21":
            self.call_service("lock/lock", entity_id=self.lock)
        if new == "19" or new == "22":
            self.call_service("lock/unlock", entity_id=self.lock)

        # Notify of any changes in state
        if new == "18" or new == "21" or new == "24":
            self.call_service("notify/html5", title="Lock", message=message("locked", new, time))
        if new == "19" or new == "22" or new == "25":
            self.call_service("notify/html5", title="Lock", message=message("unlocked", new, time))

