import requests

# GET -> ziskavani dat
# POST
# PUT
# DELETE

# co je cpu-bound a co je i/o bound operace?

response = requests.get("https://www.example.com")  # i/o bound - operace vazana na i/o

items = response.headers.items()  # cpu-bound

headers = [f"{key}, {header}" for key, header in items]  # cpu-bound

formatted_headers = "\n".join(headers)  # cpu-bound

with open("headers.txt", "w") as file:  # i/o - bound
    file.write(formatted_headers)
