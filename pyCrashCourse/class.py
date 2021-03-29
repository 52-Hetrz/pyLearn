class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def update_odometer(self, new_odometer):
        self.odometer_reading = new_odometer

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make
        return long_name.title()


class Master:
    def __init__(self, name='', age=''):
        self.name = name
        self.age = age

    def describe_master(self):
        master_information = self.name + str(self.age)
        return master_information


class ElectricCar(Car):
    def __init__(self, make, model, year, master_name):
        super().__init__(make, model, year)
        self.master = Master(master_name)

    def electric_car(self):
        print("this is an electric car,and it's master is "+self.master.describe_master())


my_electric_car = ElectricCar('tesla', 'model s', 2016, '王粟鹏')
my_electric_car.electric_car()
print(my_electric_car.get_descriptive_name())
