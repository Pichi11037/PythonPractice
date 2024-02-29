from Classes import Person, switch_case, Employee
import random

print('Objects created'.center(30, '-'))

friendList = ("Diego", "Mario", "Johann", "Angie", "Juan David", "Juan Diego")
contactList = {}
s = switch_case()

for friend in friendList:
    n = random.randint(1,3)
    contactList[str(friend)] = s.switch(n)

person1 = Employee(1234, "Carlos","Pichimata", 26, contactList,friendList)

print(person1.getData())
