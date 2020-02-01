from plyer import notification 
from playsound import playsound 
from datetime import datetime 
import time

class Notification:
    def __init__(self, message, when):
        self.title = "Your reminder"
        self.message = message
        self.time = (when - datetime.now()).total_seconds()

    def activate(self):
        time.sleep(self.time)
        notification.notify(title=self.title,
                            message=self.message,
                            app_icon="icon.ico", 
                            timeout=10,
                            )  
        playsound("toasty.wav")



