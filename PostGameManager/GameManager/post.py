# TODO: How to implement requirements?
import time
import uuid
from ongoinground import OnGoingRound
from finishedround import FinishedRound

class Post:
    def __int__(self, name, gametype, limitgroups, user):
        self.uuid = uuid.uuid4()
        self.name = name
        self.type = gametype
        self.user = user
        self.limitgroups = limitgroups

    def startround(self, players):
        starttime = time.time()
        ongoinground = OnGoingRound(self, starttime, players)
        return ongoinground

    def endround(self, ongoinground, scores):
        return FinishedRound(ongoinground.uuid, ongoinground.post, ongoinground.post, scores, ongoinground.starttime, time.time())