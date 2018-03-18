#9-3 Users

class User():

    def __init__(self, first_name, last_name, age, sex, location):
        '''Initialize first and last name as well as several other attributes'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.location = location

    def describe_user(self):
        '''prints a summary of a created user'''
        print('\n' + self.first_name.title() + ' ' + self.last_name.title() +
            ' : ' + '\nAge: ' + str(self.age) + '\nSex ' + self.sex.title() +
            '\nLocation: ' + self.location.title())

    def greet_user(self):
        print('\nGreetings! ' + self.first_name.title() + ' ' + self.last_name.title())

user1 = User('devon', 'gonzalez', 24, 'male', 'seattle')
user2 = User('megan', 'ingalls', 23, 'female', 'seattle')
user3 = User('dani', 'sandivol', 24, 'neutral', 'seattle')
user4 = User('libby', 'something', 23, 'female', 'seattle')


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user4.describe_user()
user4.greet_user()
