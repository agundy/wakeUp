# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:46:40 2013

@author: aaron
"""
import threading

class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()

        self.alarmData = alarmData

        # self.hours = int(hours)
        # self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    print("ALARM NOW!")
                    os.popen("voltage.mp3")
                    return
            time.sleep(60)
        except:
            return
    def just_die(self):
        self.keep_running = False