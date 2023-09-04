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

result = (lambda a, b: a + b)(4, 5)
print(result)
# print(sum(1, 2))

# def sum(a: int, b: int) -> int:
#     return a + b

# result = map(lambda person: dict(
#     person,
#     age=int(person["age"]),
#     full_name=person["first_name"] + " " + person["last_name"]
# ), people)


def custom_map(callback, collection):
    for item in collection:
        yield callback(item)


def extend_person(person):
    return dict(
        person,
        age=int(person["age"]),
        full_name=person["first_name"] + " " + person["last_name"]
    )

result = custom_map(extend_person, people)

for item in result:
    print(item)


# people[0]["dalsi_klic"] = 10000
# people[0]["first_name"] = "Pepicek"

# another_person = dict(people[0], dalsi_klic=1000, first_name="Pepicek")

# print(people[0])

# person["full_name"] =

# people.append({
#     "id": 3,
#     "first_name": "Leos",
#     "last_name": "Slunicko",
#     "age": "30"
# })
#
# for item in result:
#     print(item)

# print(list(result))