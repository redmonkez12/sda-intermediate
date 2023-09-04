import random
import time


def display_intro():
    print("""a""")

    print("""You are in a land full of dragons. In front of you,
      you see two caves. In one cave, the dragon is friendly
      and will share his treasure with you. The other dragon
      is greedy and hungry, and will eat you on sight.""")


def choose_cave():
    cave = ""

    # while cave != "1" and cave != "2":
    while cave not in ["1", "2"]:
        cave = input("Do jake jeskyne chces jit? (1 nebo 2)")

    return cave


def check_cave(option):
    print("Jdes do jeskyne....")
    time.sleep(2)
    print("Vypada to tady divne...")
    time.sleep(2)
    print("Vyskocil na tebe obrovsky drak a ....")
    time.sleep(2)

    friendly_cave = random.randint(1, 2)

    if option == str(friendly_cave):
        print("Juchuuu, dostal si poklad!")
    else:
        print("Drak te sezral! Muzes to zkusit priste.")


if __name__ == "__main__":
    play_again = "yes"

    while play_again == "yes" or play_again == "y":
        display_intro()
        option = choose_cave()
        check_cave(option)

        print("Chces hrat jeste jednou??? (yes or no)")
        play_again = input()
