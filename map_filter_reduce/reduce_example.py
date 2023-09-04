from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6]
#
# sum_nums = reduce(lambda prev, num: prev + num if num % 2 == 0 else prev, numbers, 0)
#
# print(sum_nums)

people = [
    {
        "id": 1,
        "first_name": "Giovanni",
        "last_name": "Seredovanni",
        "age": "10"
    },
    {
        "id": 2,
        "first_name": "Jozka",
        "last_name": "Kukuricudus",
        "age": "20"
    },
]

# sum_age = reduce(lambda prev, person: prev + int(person["age"]), people, 0)
# print(sum_age)

first_names = reduce(lambda prev, person: [*prev, person["first_name"]], people, [])
# print(first_names)


def custom_reduce(callback, collection, initial_data):
    for item in collection:
        initial_data = callback(initial_data, item)

    return initial_data


first_names = custom_reduce(lambda prev, person: [*prev, person["first_name"]], people, [])
print(first_names)

# prev - 0, num - 1 , 0 + 1 = 1
# prev - 1, num - 2, 1 + 2 = 3
# prev - 3, num - 3, 3 + 3 = 6
