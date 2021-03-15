class T1:
    __name = "11"

    def getName1(self):
        return self.__name

    def setName1(self, name):
        self.__name = name

class T2(T1):
    __name = ""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return super().getName1()


    def setName(self, name):
        super().setName1(name)

    def getName2(self):
        return self.__name


t = T2("Pavel")
t.setName("Mistik")
print(t.getName())
print(t.getName2())


class T:
    test = ""

    def fun(self):
        return self.test


t1 = T()
print(t1.fun())
