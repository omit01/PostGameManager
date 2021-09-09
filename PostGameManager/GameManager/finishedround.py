import uuid


class FinishedRound:
    def __int__(self, rounduuid, post, groups, scores, starttime, endtime):
        self.uuid = rounduuid
        self.post = post
        self.groups = groups
        self.score = scores
        self.starttime = starttime
        self.endtime = endtime