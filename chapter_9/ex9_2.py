#9-2  Three Restaurants: Make a class named Restaurant that prints out two pieces of information and another message that indicates the restaurant being # open.

class Restaurant():
    '''A simple Restaurant class'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant_name and cuisine_type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe(self):
        '''Description of restaurant'''
        print('\n' + self.restaurant_name.title() + ' is the name of the restaurant')
        print(self.restaurant_name.title() + ' serves ' + self.cuisine_type + ' style cuisine')
    def open_restaurant(self):
        print('\n' + self.restaurant_name.title() + ' is currently open')

rest1 = Restaurant('sushi kappo', 'japanese')
rest1.describe()
rest1.open_restaurant()

rest2 = Restaurant('north lake tavern', 'american')
rest2.describe()
rest2.open_restaurant()

rest3 = Restaurant('allegro', 'italian')
rest3.describe()
rest3.open_restaurant()
