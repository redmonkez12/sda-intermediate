switchers = [
    {
        "name": "vlevo_u_okna",
        "switch_is_on": False,
    },
    {
        "name": "hned_u_dveri",
        "switch_is_on": False,
    },
]

# Proceduralni programovani


# def to_lowercase(text: str):
#     if len(text) > 10:
#         return text[:10].lower() + "..."
#
#     return text.lower()
#
#
# print(to_lowercase("Pepicek jde do lesa"))


def turn_off(switch_data):
    switch_data["switch_is_on"] = False


def turn_on(switch_data):
    switch_data["switch_is_on"] = True


vlevo_u_okna = switchers[0]

turn_on(vlevo_u_okna)
turn_off(vlevo_u_okna)

print(vlevo_u_okna)
