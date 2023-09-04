greetings = []


def register(func):
    print(f"running register({func})")
    greetings.append(func)
    return func


@register
def friend():
    print("hey buddy")


@register
def foreigner():
    print("Good day sir")


def girlfriend():
    print("Hey honey")


def main():
    print("Let's begin")
    print("greetings", greetings)
    foreigner()
    friend()
    girlfriend()


if __name__ == "__main__":
    main()
