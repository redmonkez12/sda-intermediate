class LightSwitch:
    def __init__(self):
        self.switch_is_on = False
        self.brightness = 0

    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False

    def show(self):
        if self.switch_is_on:
            print("Aktualne svitim")
        else:
            print("Aktualne nesvitim")

    def raise_level(self):
        if self.brightness < 10:
            self.brightness += 1

    def lower_level(self):
        if self.brightness > 0:
            self.brightness -= 1

#
switchers = []

for _ in range(10):
    switchers.append(LightSwitch())

switchers[0].switch_is_on = True

data_source_1 = [
    {
        "id": 1,
        "property_type": "LAND",
        "owner_id": 1,
    }
]

data_source_2 = [
    {
        "id": 1,
        "first_name": "Jozka",
    }
]

for item in data_source_2:
    for item_1 in data_source_1:
        if item["id"] == item_1["id"]:
            person = {
                  "id": item["id"],
                  "first_name": item["first_name"]
            }

            # ulozite do databaze
            # request.

# dictionary - objekt
# objekt

# person = dict()
