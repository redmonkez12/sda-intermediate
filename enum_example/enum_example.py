from enum import Enum


class Direction(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    TOP = "NECO JINEHO"
    BOTTOM = "DOWN"

    @classmethod
    def to_list(cls):
        return [item.value for item in cls]


print(Direction.to_list())

# my_enum = Direction("ahoj")
# print(my_enum)


def move(direction: Direction):
    if direction == Direction.RIGHT:
        print("jdu do prava")
    elif direction == Direction.LEFT:
        print("jdu vlevo")


# fn + control + space
# alt + enter nebo ctrl + enter


# move(Direction.RIGHT)