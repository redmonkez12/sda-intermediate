import random

number = random.randint(1, 20)  # 1-20 vcetne 1 i 20

player_name = input("Jake je tvoje jmeno?\n")  # \n -> novy radek


MAX_TRIES = 3  # VELKE PISMENA mohou znacit konstantu

print(f"Cauvec {player_name}. Myslim si cislo od 1 do 20, zkus ho uhodnout mas {MAX_TRIES} pokusy")

# vnejsi smycka
# nastavuje data ve hre
# pripadne se zeptate chces pokracovat
while True:
    guess_taken = 0

    # hlavni smycku
    # dokud je tato podminka splnena tak hrajeme,
    # jinak vyskakujeme z while smycky do vnejsi smycky (while True radek 14)
    while guess_taken < MAX_TRIES:
        try:
            user_guess = input(f"Zkus uhodnout cislo. Pokus: {guess_taken + 1}\n")  # ziskej cislo od uzivatele
            guess = int(user_guess)  # transformuj na integer - pokud user_guess bude napr. slunicko, dostaneme ValueError

            if guess < 0 or guess > 20:
                print("Napis cislo ktere je v rozmezi 1 az 20")
                continue  # ukonci aktualni pruchod a pokracuje novou smyckou
        except ValueError:
            print("Spatne cislo. zkus to znovu")
        else:  # pokud v try bloku probehne v poradku tak pokracuj do else
            guess_taken += 1

            if number == guess:
                break

            if guess < number:  # 5 < 20
                print("Tvoje cislo je prilis male")

            if guess > number:  # 10 > 5
                print("Tvoje cislo je prilis velke")

    # Pokud uzivatel napise pismeno nebo slovo ktere zacina
    # necim jinym nez y tak ukoncite hru
    # Y
    # y
    # yes
    if guess == number:
        print("Super, vyhral si!")
    else:
        print(f"Nevadi, muzes to zkusit znovu. Myslel jsem si cislo {number}.")

    user_input = input("Chces hrat znovu?\n").lower()

    if user_input not in ["y", "yes"]:
        break
