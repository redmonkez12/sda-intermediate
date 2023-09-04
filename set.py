properties = [
    {
        "id": 1,
        "property_type": "LAND",
    },
    {
        "id": 2,
        "property_type": "HOUSE",
    },
    {
        "id": 3,
        "property_type": "FLAT",
    },
    {
        "id": 4,
        "property_type": "HOUSE",
    },
]

# result = []

property_type = set()

for item in properties:
    property_type.add(item["property_type"])
    # if item not in result:
    #     result.append()

print(property_type)
