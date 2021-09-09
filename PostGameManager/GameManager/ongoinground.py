import time
import uuid


class OnGoingRound:
    def __int__(self, post, groups):
        self.uuid = uuid.uuid4()
        self.post = post
        self.starttime = time.time()
        self.groups = groups