class Switch:
    def case1(self):
        print("This is case 1")

    def case2(self):
        print("This is case 2")

    def case3(self):
        print("This is case 3")

    def default(self):
        print("Invalid case")

    def switch(self, argument):
        method_name = 'case' + str(argument)
        method = getattr(self, method_name, self.default)
        return method()

# Create an instance and call the switch method with the desired case
s = Switch()

l = [1,2,3,4,5]

s.switch(l[1])
