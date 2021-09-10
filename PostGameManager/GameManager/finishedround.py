import uuid


class FinishedRound:
    def __init__(self, rounduuid, post, groups, scores, starttime, endtime):
        self.uuid = rounduuid
        self.post = post
        self.groups = groups
        self.scores = scores
        self.starttime = starttime
        self.endtime = endtime
