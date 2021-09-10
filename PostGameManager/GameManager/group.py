import uuid


class Group:
    def __init__(self, groupuuid, name, number, user):
        self.uuid = groupuuid
        self.name = name
        self.numberofplayers = number
        self.user = user

    @classmethod
    def newGroup(cls, name, number, user):
        return cls(uuid.uuid4(), name, number, user)
