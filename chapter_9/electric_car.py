class Car():
    '''A simple attempt to represent a car.'''

    def ___init___(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

class electricCar(car):
    '''Represent aspects of a car, specific to electric vehicles.'''
    def ___init___(self,make,year):
        '''initialize attributes of the parent class.'''
        super().___init___(make,model,year)

my_tesla = electricCar('tesla', 'model s', 2016)
print(my_teslaget_descriptive_name())
