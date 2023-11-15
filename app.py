import requests

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    data = response.json()
    return data["setup"], data["delivery"]

if name == "main":
    setup, delivery = get_joke()
    print(f"{setup}\n{delivery}")
