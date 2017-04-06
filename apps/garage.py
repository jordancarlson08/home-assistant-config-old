import appdaemon.appapi as appapi
import datetime


#
# Garage App
# Notifications and reminders
#
# Args:
#

class Garage(appapi.AppDaemon):
    def initialize(self):
        self.listen_state(self.notify_garage, "cover.garage_door")
        self.listen_state(self.garage_reminder, "cover.garage_door")
        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')
        self.call_service("notify/html5", title="Garage", message="Garage initialized at " + time)


    def notify_garage(self, entity, attribute, old, new, kwargs):
        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')
        actionData={ "tag" : "garage_" + new }
        self.call_service("notify/html5", title="Garage", message=new + " at " + time, data=actionData)


    def garage_reminder(self, entity, attribute, old, new, kwargs):
        if (new == 'open'):
            self.handle = self.run_in(self.notify_garage_open, 300)
        else:
            # if handler isn't null, cancel timer
            self.cancel_timer(self.handle)


    def notify_garage_open(self, kwargs):
        actionData={"tag" : "garage_reminder", "actions": [ {"action": "garage_close", "title": "Close Garage" } ] } 
        self.call_service("notify/html5", title="Garage", message="Garage open for 5 minutes.", data=actionData)      