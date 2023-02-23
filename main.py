from datetime import datetime
import pytz

class Clock:
    def __init__(self, timezone):
        self.shift = timezone

    def __str__(self):
        return f"A clock instance with a timezone of {self.shift}"
    
    def time(self):
        return datetime.now().strftime("%H:%M:%S")
    def date(self):
        return datetime.now().strftime("%d,%b,%Y")
    def currentTZ(self):
        # Does samething as current statement
        #naive = datetime.now()
        #timezone = pytz.timezone("Asia/Tokyo")
        #aware1 = timezone.localize(naive)
        #return aware1.utcoffset()
        return pytz.timezone("Asia/Tokyo").localize(datetime.now()).utcoffset()
        

local = Clock(-8)
print(local)
print(local.time())
print(local.date())
print(local.currentTZ())