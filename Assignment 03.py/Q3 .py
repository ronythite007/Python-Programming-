class car:
    def __init__(self, name,cost,passing):
        self.name=name
        self.cost=cost
        self.passing=passing
    def get_info(self):
        print(f"Name of the car is {self.name}")
        print(f"The cost of the car is  {self.cost}")
        print(f"Passing of the car is from  {self.passing}")

obj=car("honda","6 lac","mh12")
obj1=car("ford","14 lac","mh14")
print(obj.get_info())
print(obj1.get_info())


class marks:
    @staticmethod
    def __init__ (marks,):
        print(marks)
data=marks("50")
print(data)