import random

class Rectangulo:

    def __init__(self, height, length) -> None :
        self.lenght = length
        self.height = height

    def getArea(self):
        return self.height*self.lenght
    

class Person:

    def __init__(self, name:str, lastName:str, age:int, contactlist:dict, *args,) -> None:
        self._name = name
        self._lastName = lastName
        self._age = age
        self._contactList = list(contactlist)
        self._friends = list(args)

    @property
    def name(self):
        return self._name

    @property
    def lastName(self):
        return self._lastName

    @property
    def age(self):
        return self._age

    @property
    def contactList(self):
        return self._contactList

    @property
    def friends(self):
        return self._friends
    
    @name.setter
    def name(self, name):
        self._name = name

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @age.setter
    def age(self, age):
        self._age = age

    @contactList.setter
    def contactList(self, contactList):
        self._contactList = contactList

    @friends.setter
    def friends(self, friends):
        self._friends = friends

    # def __del__(self):
    #     print(f'Object Name={self.name} {self.lastName} deleted!')

    def sayHi(self) -> str:
        return f'Hi!, my name is {self.name} {self.lastName}, nice to meet you!'
    
    def getData(self):
        return f'name={self.name}, Last Name={self.lastName}, Age={self.age}, Friends={self.friends}, Contact List= {self.contactList}'
    
class Employee(Person):
    def __init__(self, salary,  name, lastName, age, contactList, friends):
        super().__init__(name, lastName, age, contactList, friends)
        self._salary = salary
    
    def getData(self):
        return super().getData()

class switch_case:
    
    def case1(self) -> int:
        return random.randint(3211111111, 3219999999)
    
    def case2(self) -> int:
        return random.randint(3221111111, 3229999999)
    
    def case3(self) -> int:
        return random.randint(3231111111, 3239999999)
    
    def default(self):
        print("Invalid case")
    
    def switch(self, case):
        method_name = 'case'+ str(case)
        method = getattr(self, method_name, self.default)
        return method()
    


    
    
if __name__  == '__main__':
    rect1 = Rectangulo(4, 5)

    print(type(rect1))

    friendList = ("Diego", "Mario", "Johann", "Angie", "Juan David", "Juan Diego")
    contactList = {}

    s = switch_case()

    for friend in friendList:
        n = random.randint(1,3)
        contactList[str(friend)] = s.switch(n)

    person1 = Person("Andres","Pichimata", 26, contactList,friendList)

    dataPerson1 = person1.name
    print(dataPerson1)