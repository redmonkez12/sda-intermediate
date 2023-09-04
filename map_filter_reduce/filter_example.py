# people = [
#     {
#         "id": 1,
#         "first_name": "Jozka",
#         "last_name": "Kukuricudus",
#         "age": 20,
#     },
#     {
#         "id": 2,
#         "first_name": "Leos",
#         "last_name": "Slunicko",
#         "age": 30,
#     },
#     {
#         "id": 3,
#         "first_name": "Giovanni",
#         "last_name": "Seredovanni",
#         "age": 10,
#     },
# ]
#
#
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def custom_filter(callback, collection):
#     for item in collection:
#         result = callback(item)
#         if result:
#             yield item
#
#
# result = custom_filter(lambda person: person["age"] < 18, people)
# # result = custom_filter(lambda letter: letter != "b", "aaaabbbcccc")
#
# for item in result:
#     print(item)
#
# # nums = [1, 2, 3, 4, 5]

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

# normalized_data = map(lambda person: dict(person, age=int(person["age"])), people)

children = filter(
    lambda person: person["age"] < 18,
    map(lambda person: dict(person, age=int(person["age"])), people),
)

for item in children:
    print(item)

# result = custom_filter(lambda person: person["age"] < 18, people)