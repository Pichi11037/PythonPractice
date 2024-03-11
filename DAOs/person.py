class Person:

    def __init__(self, id:int, name:str, lastName:str, email:str) -> None:
        
        self._id = id
        self._name = name
        self._lastName = lastName
        self._email = email

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @property
    def lastName(self):
        return self._lastName

    @property
    def email(self):
        return self._email
    
    @name.setter
    def name(self, name):
        self._name = name

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @email.setter
    def email(self, email):
        self._email = email

    # def __del__(self):
    #     print(f'Object Name={self.name} {self.lastName} deleted!')

    def sayHi(self) -> str:
        return f'Hi!, my name is {self.name} {self.lastName}, nice to meet you!'
    
    def __str__(self):
        return f'''Person[
            ID={self.id}, 
            name={self.name}, 
            Last Name={self.lastName}, 
            Email={str(self.email)}]
            '''
    