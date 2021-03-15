class Heavy_tanks:
    name = "VK.100.01.P"
    health_points = 2200
    speed = 20

    def set(self, name,health_points, speed):
        self.name = name
        self.health_points = health_points
        self.speed = speed
Maushchen = Heavy_tanks ()
Maushchen.set ("Мышонок", 2800, 15)
print("Тяжелый танк" , " " , Maushchen.name , " " + str(Maushchen.speed) + " " + "Километров в час")
# class Medium_tanks:
#     name = "Panther II"
#     health_points = 1600
#     speed = 45
#     print(Medium_tanks.)