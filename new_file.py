import requests

URL_API = "https://api.api-ninjas.com/v1/animals"
API_KEY = "qxnYeyzdqUCF16UH1BUTYugjvZvw9EmOAEo048O6"


def get_animal_info():
    user_input = input("Introduce the name of the animal: ").strip()
    url = f"{URL_API}?name={user_input}"
    params = {
        "X-Api-Key": API_KEY,
    }
    response = requests.get(url, params=params)
    animals_data = response.json()
    for animal in animals_data:
        print(animal)


get_animal_info()