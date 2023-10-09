import uuid


class Client:
    def __init__(self, name, address, email, number, uid = None):
        self.name = name
        self.address = address
        self.email = email
        self.number = number
        self.uid = uid or uuid.uuid4()


    def to_dict(self):
        return vars(self)


    @staticmethod
    def schema():
        return ['name', 'address', 'email', 'number', 'uid']
