import time
import uuid


class OnGoingRound:
    def __init__(self, rounduuid, post, starttime, groups):
        self.uuid = rounduuid
        self.post = post
        self.starttime = starttime
        self.groups = groups

    @classmethod
    def newongoinground(cls, post, groups):
        return cls(uuid.uuid4(), post, time.time(), groups)
