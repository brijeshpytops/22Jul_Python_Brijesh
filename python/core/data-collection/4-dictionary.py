"""
syntax:

dict_name = dict()
dict_name = {
    'key1': value1,
    'key2': value2,
    .
    .
    .
}
"""

contacts = {
    'A': [
        {
            'name': 'ajay',
            'phone': '123-456-7890',
            'email': 'ajay@example.com'
        },
        {
            'name': 'ajay2',
            'phone': '987-654-3210',
            'email': ['ajay2@example.com','aj123@gmail.com']
        }
    ],
    'B': [
        {   
            'name': 'bobby',
            'phone': '555-555-5555',
            'email': 'bobby@example.com'
        },
        {
            'name': 'bobby2',
            'phone': '555-555-5556',
            'email': 'bobby2@example.com'
        }
    ],
    'C': [
        {
            'name': 'charlie',
            'phone': '555-555-5557',
            'email': 'charlie@example.com'
        },
        {
            'name': 'charlie2',
            'phone': '555-555-5558',
            'email': 'charlie2@example.com'
        }
    ]
}

# Access dict:
# print(contacts)
# print(contacts['A'])
# print(contacts['A'][1])
# print(contacts['A'][1]['phone'])


# d = dict()
# print(dir(d))


# items = ['tomato', 'potato', 'onion']
# price = 20

# products = dict()

# print(products.fromkeys(items, price))

# car = {
#     'brand': 'Toyota',
#     'model': 'Camry',
#     'year': 2015,
#     # 'color': 'blue',
#     'mileage': 50000
# }

# car.setdefault("color", "black")
# print(car)

# print(car.get('color'))
# car.pop('color')
# car.popitem()
# print(car)

# print(car.keys())

# for key in car.keys():
#     print(key, car[key])
# for value in car.values():
#     print(value)

# print(car.items())
# for key, value in car.items():
#     print(key, value)

# mango_shake = {
#     'milk': 1.5,
#     'mango puree': 2.0,
#     'ice cream': 1.0,
# }

# mango_shake.update({'sugar':2.0})
# mango_shake.update({'kaju-badam-pista':200.0})
# print(mango_shake)