# 8-12 sandwiches: write a function that accepts a list of items a person
#wants on a sanwcich.
#req: 1 parameter, print a summary of the sandwhich order.
#needs 3 calls using different arguements each time/.

def build_sandwhich(item0, item1, **item):
    '''build a function that lists all of the items a person wants in their
        sandwich'''
    list = {}
    list ['first_ingredient'] = item0
    list ['second_ingredient'] = item1
    for key, value in item.items():
        list['Extra'] = value
    return list

sandwich = build_sandwhich("swiss", "tomato", extra1 = 'ham')
sandwhich1 = build_sandwhich('cheddar', 'turkey', extra = 'cream cheese')
sandwhich2 = build_sandwhich('pepperjack', 'avacado', extra = 'red onions')


print (sandwich)
print (sandwhich1)
print (sandwhich2)
