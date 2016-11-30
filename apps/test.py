import appdaemon.appapi as appapi


#
# Simple Schedule App
#
# Args:
#   time_on     -- ex. 10:30:30 == 10:30am and 30 seconds
#   time_off    --
#   switch      -- the entity id of the switch or light
#

class TestApp(appapi.AppDaemon):
    def initialize(self):
        self.switch = self.args["switch"]
        self.door = self.args["door"]

        self.listen_state(self.turn_on_cb, self.door, new="on")
        self.listen_state(self.turn_off_cb, self.door, new="off")

    def turn_on_cb(self, entity, attribute, old, new, kwargs):
        self.turn_on(self.switch)
        self.call_service("notify/simple", title="Test", message="On")

    def turn_off_cb(self, entity, attribute, old, new, kwargs):
        self.turn_off(self.switch)
        self.call_service("notify/simple", title="Test", message="Off")

