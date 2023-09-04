class UsernameDuplication(Exception):
    pass


class AuthService:

    def register(self, username: str):
        if username == "tomas":
            raise UsernameDuplication(f"Toto uzivatelske jmeno [{username}] uz v databazi existuje")

        if len(username) < 5:
            raise Exception("tvoje uzivatelske jmeno je prilis kratke")

        print("Vytvareni dat na databazi")

    def login(self, username: str, password: str):
        if username == "tomas" and password == "123456":
            return {
                "id": 1,
                "first_name": "Tomas",
                "last_name": "Svojanovsky",
            }

        raise Exception("Invalid password or email")
