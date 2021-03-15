# 10 . В справочной аэропорта имеется расписание вылета самолетов на сле-
# дующие сутки. Для каждого рейса указаны номер рейса, пункт назначения,
# время вылета. Вывести для заданного пункта назначения номера рейсов и время
# вылета самолетов.

# Laba 10
# 10 . Ключ: время вылета. Сортировка выбором.

# Laba 11
# 10 . Найти самолет, вылетающий в 14.00.

# class Airport:
#     def __init__(self, flightNumber, destination, departureTime) -> None:
#         super().__init__()
#         self.__flightNumber = flightNumber
#         self.__destination = destination
#         self.__departureTime = departureTime
#
#     # private:
#     __flightNumber = 0  # номер рейса
#     __destination_ = ""  # пункт назначения
#     __departureTime = 0  # время вылета min
#
#     def setAll(self, flightNumber, destination, departureTime):
#         self.__flightNumber = flightNumber
#         self.__destination = destination
#         self.__departureTime = departureTime
#
#     def setFlightNumber(self, flightNumber):
#         self.__flightNumber = flightNumber
#
#     def setDestination(self, destination):
#         self.__destination = destination
#
#     def setDepartureTime(self, departureTime):
#         self.__departureTime = departureTime
#
#     def showAirport(self):
#         print("")
#         print("Show Airport")
#         print("FlightNumber:",self.__flightNumber)
#         print("Destination:", self.__destination)
#         print("DepartureTime:", self.__departureTime)
#
# l_list = [Airport(100, "Minsk 1", 600), Airport(5, "Minsk 2", 1500)]
#
# # t1 = Airport()
# # t1.setAll(100, "Minsk 1", 600)
#
# # t2 = Airport()
# # t2.setAll(5, "Minsk 2", 1500)
#
# # l_list = [t1, t2]
#
# for item in l_list:
#     item.showAirport()
