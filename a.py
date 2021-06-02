import threading
import time

class BackgroundTasks(threading.Thread):
    def run(self,*args,**kwargs):
        while True:
            print('Hello')
            time.sleep(1)
            print("test")

t = BackgroundTasks()
t.start()