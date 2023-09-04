ids = [1, 2, 3]
animals = ["Sunny", "Ash", "Luna"]

# result = zip(ids, animals)
#
# for item in result:
#     print(item)

# {1: "Sunny", 2: "Ash", 3: "Luna"}

# Solution 1

# result = {}
#
# for i in range(len(ids)):
#     result[ids[i]] = animals[i]
#
# print(result)

# Solution 2

# result = {key: value for key, value in zip(ids, animals)}
# print(result)

# Solution

# result = dict(zip(ids, animals))
# result = dict(zip("ahoj", [1, 2, 3, 4]))
# print(result)

# list_1 = [1, 2]
# list_2 = [3, 4]
#
# print([*list_1, *list_2])
# print(list_1 + list_2)

# person_data_1 = {
#     "id": 1,
#     "first_name": "Giovanni",
# }
#
# person_data_2 = {
#     "last_name": "Seredovanni",
#     "age": "10"
# }
#
# print({**person_data_1, **person_data_2})
# print(person_data_1 + person_data_2) # nejde
