from app.services.auth_service import AuthService, UsernameDuplication

user_data = {
    "username": "tomas",
    "password": "123456",
}

auth_service = AuthService()


def user_register(request_data):
    try:
        auth_service.register(request_data["username"])
    except UsernameDuplication as e:
        print(str(e))
    except Exception as e:
        # if isinstance(e, DataIntegrityError):
        #     print

        print("fallback", e)


def user_login(request_data):
    pass


user_register({
    "username": "tomas"
})

# user_login(user_data)

# FastAPI je framework

# app = FastAPI()

# http://localhost:3000/

# GET, POST, PUT, PATCH, DELETE
# GET - slouzi pro ziskavani da
# POST - login, register nebo vytvareni dat

# @measure_time
# def get_users():
#     pass


# @app.get("/users")
# def get_users():
#     return []
#
#
# @app.post("/users")
# def create_user():
#     print("Neco udelej")
