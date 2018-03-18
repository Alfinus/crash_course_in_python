#8-13 user profile: build a profile for yourself using a previous example

def build_profile (first, last, **user_info):
    ''' Build a dictionary containing everything we know about a user.'''
    profile = {}
    profile ['frst_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location = 'princeton',
                            field = 'physics')
print(user_profile)

user_profile1 = build_profile('devon','yoxtheimer',
                                field = 'sociology & political economics',
                                location = 'seattle',
                                sex = 'male')
print(user_profile1)
