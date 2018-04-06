import time

class errorhandler(object):
    def __init__(self):
        self.entries = {'eh':[]} # sender, msg, timestamp

    def isType(self, item1, item2):
        return type(item1) is type(item2)

    def isTypeStr(self, item):
        return self.isType(item, "string")

    def add(self, sender, msg):
        if not self.isTypeStr(sender):
            self.entries['eh'].append(["sender: requires str, is " + str(type(sender)), time.time()])
        if not self.isTypeStr(msg):
            self.entries['eh'].append(["message: requires str, is" + str(type(sender)), time.time()])
        else:
            if sender not in self.entries:
                self.entries[sender] = []
            self.entries[sender].append([msg, time.time()])

    def numEntries(self):
        entry_count = 0
        for sender, errors in self.entries.items():
            entry_count += len(errors)
        return entry_count

    def numEntriesOfSender(self, sender):
        if not self.isTypeStr(sender):
            self.add('eh', 'num entries must be given a string')
        else:
            return len(self.entries[sender])
        return None

    def getEntriesOfSender(self, sender, remove):
        if remove is None:
            remove = False
        if not self.isTypeStr(sender):
            self.add('eh', 'num entries of sender must be given a string')
        else:
            print(self.entries)
            entry_list = self.entries[sender]
            if remove:
                self.entries[sender] = []
            return entry_list
        return []
