#9-1 Restaurant: Make a class named Restaurant that prints out two pieces
# of information and another message that indicates the restaurant being open.

class Restaurant():
    '''A simple Restaurant class'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant_name and cuisine_type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def served(self):
        '''Return how many people have been served'''
        print('This restaurant has served ' + str(self.number_served)
    def updated_served(self):
        '''
    def describe(self):
        '''Description of restaurant'''
        print(self.restaurant_name.title() + ' is the name of the restaurant')
        print(self.restaurant_name.title() + ' serves ' + self.cuisine_type + ' style cuisine')
    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is currently open')

rest1 = Restaurant('sushi kappo', 'japanese')
rest1.describe()
rest1.open_restaurant()

rest = Restaurant('allegro', 'coffee', 45)
rest.describe()
rest.open_restaurant
print( str(Restaurant(rest.number_served)) + ' have been served at '+ restaurant_name)
