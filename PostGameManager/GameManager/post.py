# TODO: How to implement requirements?
import time
import uuid
from ongoinground import OnGoingRound
from finishedround import FinishedRound


class Post:
    def __init__(self, postuuid, name, gametype, user, limitgroups):
        self.uuid = postuuid
        self.name = name
        self.type = gametype
        self.user = user
        self.limitgroups = limitgroups

    @classmethod
    def newpost(cls, name, type, user, limitgroups):
        return cls(uuid.uuid4(), name, type, user, limitgroups)

    def startround(self, groups):
        ongoinground = OnGoingRound(self, groups)
        return ongoinground

    def endround(self, ongoinground, scores):
        return FinishedRound(ongoinground.uuid, ongoinground.post, ongoinground.post, scores, ongoinground.starttime,
                             time.time())
