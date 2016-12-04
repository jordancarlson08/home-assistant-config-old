import requests
import datetime

time = datetime.datetime.now().time()
time = time.strftime('%l:%M %p')
test = "back door at " + time
print(test)
