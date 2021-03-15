class Addition:
    __first = 0
    __second = 0
    __answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.__first = f
        self.__second = s

    def display(self):
        print("First number = " + str(self.__first))
        print("Second number = " + str(self.__second))
        print("Addition of two numbers = " + str(self.__answer))

    def calculate(self):
        self.__answer = self.__first + self.__second

    def fun(self):
        return self.__first > self.__second
    # creating object of the class


# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()

print(obj.fun())