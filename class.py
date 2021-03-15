# class Tet:
#     t = 100
#
# class Player:
#     def __init__(self, name, level):
#         self.__name = name
#         self.__level = level
#
#     def setName(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#
#     def setLevel(self, level):
#         self.__level = level
#
#     def getLevel(self):
#         return self.__level
#
#     __name = "Test"
#     __level = 1
#
#     __posX = 1
#     __posY = 11
#
#     # public
#     def fun(self):
#         print(self.__name)
#         print(self.__level)
#
#     # private __
#     def __fun1(self):
#         print("privet")
#
#     # protected _
#     def _fun2(self):
#         print("")
#
#
# # class World(Player):
# #     def __init__(self, name, level):
# #         # super().__init__(name, level)
# #         self.__player = Player(name, level)
# #
# #     __player = None
# #
# #     def getPlayerFun(self):
# #         self.__player.fun()
# #
# #     def getPlayer(self):
# #         return self.__player
# #
# #     def test(self):
# #         self._fun2()
# #
# #
# # l_worlds = {World("Pavel", 99), World("Mistik", 100)}
# #
# #
# # for l in l_worlds:
# #     l.getPlayerFun()
#
# l_list = [Player("Pavel", 10), Player("Mistik", 99)]
#
# # p1 = Player()
# # p1.setName("Pavel")
# # p1.setLevel(10)
# #
# # p2 = Player()
# # p2.setName("Mistik")
# # p2.setLevel(100)
# #
# # l_list = {p1, p2}
#
# # def fun(player):
# #     print(player.__name)
# #     print(player.__level)
#
#
# for item in l_list:
#     # fun(item)
#     item.fun()


class Test1:
    __name = ""

    __posX = 1
    __posY = 22
    __pos = {"x": __posX, "y": __posY}

    def setName(self, name):
        self.__name = name

    def getName(self):
        if self.__name != "":
            return self.__name
        else:
            return "Error"

    def posPlayer(self):
        return self.__pos


t = Test1()

t.setName("Pavel")
print(t.getName())

print(t.posPlayer().get("x"))
print(t.posPlayer().get("y"))