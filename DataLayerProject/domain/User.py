class User:
    def __init__(self, id=None,  username=None, password=None):
        self._id = id
        self._username = username
        self._password = password

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, nId):
        self._id = nId

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, nUsername):
        self._username = nUsername
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, nPassword):
        oldpassword = input('Please type the old password: ')
        if oldpassword == self._password:
            newPassword = input('Please retype the new password: ')
            if newPassword == nPassword:
                self._password = nPassword

    def __str__(self) -> str:
        return f'''
User:
    [ID: {self._id}, username: {self._username}, password: {self._password}]
    '''