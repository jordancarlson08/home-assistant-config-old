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
        self.listen_state(self.garage_reminder, "cover.garage_door")


        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')
        self.call_service("notify/html5", title="Garage", message="Garage initialized at " + time)

    def notify_garage(self, entity, attribute, old, new, kwargs):
        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')

        self.call_service("notify/html5", title="Garage", message=new + " at " + time)


    def garage_reminder(self, entity, attribute, old, new, kwargs):
        if (new == 'open'):
        	# Start a timer
        	self.handle = self.run_in(self.notify_garage_open, 15)
        # else:
        	# if handler isn't null, cancel timer
        	# self.cancel_timer(handle)





        time = datetime.datetime.now().time()
        time = time.strftime('%l:%M:%S %p')

        self.call_service("notify/html5", title="Garage", message=new + " at " + time)


    def notify_garage_open(self, kwargs):
        self.call_service("notify/html5", title="Garage", message="Garage open for 15 seconds")    	


# 2017-04-05 14:49:09.234471 DEBUG Event type:state_changed:
# 2017-04-05 14:49:09.235124 DEBUG {'entity_id': 'cover.garage_door', 
# 'old_state': {'entity_id': 'cover.garage_door', 'attributes': {'friendly_name': 'Garage Door'}, 'state': 'closed', 'last_updated': '2017-04-05T17:20:04.676486+00:00', 'last_changed': '2017-04-05T17:20:04.676486+00:00'}, 
# 'new_state': {'entity_id': 'cover.garage_door', 'attributes': {'friendly_name': 'Garage Door'}, 'state': 'open', 'last_updated': '2017-04-05T20:49:09.122719+00:00', 'last_changed': '2017-04-05T20:49:09.122719+00:00'}}