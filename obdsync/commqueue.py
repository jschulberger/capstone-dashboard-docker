import obd
import time
import operator

class commqueue(object):
    def __init__(self):
        self.commlist = {}
        self.queue = {}
        self.lastupdate = 0

    def timeInMilli(self):
        return int(round(time.time() * 1000))

    def sortQueue(self):
        self.queue = sorted(self.queue.items(), key = operator.itemgetter(1), reverse = False)

    def register(self, command, interval):
        if not type(command) is str:
            return False
        if not type(interval) is int:
            return False
        if command in commlist:
            return False
        if not obd.commands.has_name(command):
            return False
        if command in self.queue:
            return False
        self.commlist[command] = interval
        return True

    def update(self):
        if self.lastupdate <= 0:
            self.queue.clear()
            for command, interval in self.commlist.items():
                self.queue[command] = interval
            self.lastupdate = self.timeInMilli()
        else:
            for command, interval in self.queue.items():
                self.queue[command] = interval - (self.timeInMilli() - self.lastupdate)
            self.lastupdate = self.timeInMilli()
            self.sortQueue()

    def getnext(self):
        self.update()
        for command, interval in self.queue.items():
            if interval < 0:
                self.queue[command] = self.commlist[command]
                return command
        return None
