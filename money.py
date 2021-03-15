class Money:
    def __init__(self,d,c):
        self.total_cents = d*100+c

    @property
    def dollars(self):
        return self.total_cents//100

    @property
    def cents(self):
        return self.total_cents % 100

    @dollars.setter
    def dollars(self,value):
        if isinstance(value,int) and value >=0:
            self.total_cents = value*1 + self.cents
        else:
            print("Error Dollars")

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 100 > value >= 0:
            self.total_cents = self.dollars * 100 + value
        else:
            print("Error Cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"