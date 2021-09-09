import uuid


class Game:
    def __int__(self):
        self.uuid = uuid.uuid4()
        self.groups = set()
        self.posts = set()

    def addgroup(self, group):
        self.groups.add(group)
        return

    def addpost(self, post):
        self.posts.add(post)
        return

    def removegroup(self, group):
        self.posts.remove(group)
        return

    def removepost(self, post):
        self.posts.remove(post)
        return