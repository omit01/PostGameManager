import uuid

class Group:
    def __int__(self, name, number, user):
        self.uuid = uuid.uuid4()
        self.name = name
        self.numberofplayers = number
        self.user = user
