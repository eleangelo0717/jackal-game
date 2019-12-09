import db

class User(object):

    def __init__(self, user_info):
        self.user = user_info
        self.id = user_info.id
        self.status = None
        self.request = {}
        self.step = None
        self.save()

    def save(self):
        j = db.saveUser(self.user)
        self.user = j.get('user')
        self.status = j.get('status', '')
        self.request = j.get('request', {})
        self.step = j.get('step', '')
        self.info = j.get('info')
