#8-14 build a function that stores information about cars into a dictionary and creates a list of other functions.


def build_car (manufacturer, model, **car_info):
    ''' Build a dictionary containing everything we know about the car.'''
    profile = {}
    profile ['manufacturer'] = manufacturer
    profile['model car'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile

car_profile = build_car('subaru', 'outback',
                            color = 'blue',
                            tow_package = 'True')
print(car_profile)
